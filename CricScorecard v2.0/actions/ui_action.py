from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
from locators import Locators
from actions.excel_action import ExcelAction

class UIAction:
    def __init__(self, tournament_name, url, abandoned_matches):
        self.tournament_name = tournament_name
        self.url = url
        self.abandoned_matches = abandoned_matches
        chromedriver_path = Locators.chromedriver_path 
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.excel_action = ExcelAction(tournament_name)
        
    def open_web_page(self): 
        self.driver.get(self.url)
        self.excel_action.prepare_workbook_template()

        time.sleep(10) # this is temprary to avoid ads

        first_match_no = Locators.first_match_no
        last_match_no = len(self.driver.find_elements(By.XPATH, Locators.tournament_len_xpath))
        # first_match_no = 3
        # last_match_no = 3
        for match_no in range(first_match_no, last_match_no + 1): # tournament_last_match_no + 1
            if match_no in self.abandoned_matches:
                pass
            else:
                if match_no in (first_match_no + 1, first_match_no + 2):
                    self.wait_at_tournament()
                tournament_xpath = Locators.tournament_xpath.format(match_no=match_no)
                match = self.driver.find_element(By.XPATH, tournament_xpath)
                self.navigate_to_element(match)                
                # open match in new tab --- 
                ActionChains(self.driver).key_down(Keys.CONTROL).click(match).key_up(Keys.CONTROL).perform()
                self.driver.switch_to.window(self.driver.window_handles[1])

                time.sleep(12) # this is temprary to avoid ads
                
                self.wait_at_match()
                self.action_flow()
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])           
        self.driver.quit()

    def action_flow(self):
        common_stat_list = self.fetch_common_stats()
        for sheet_name, (tab_name, method_name) in Locators.sheet_to_tab.items():
            if tab_name in Locators.tabs:
                tab_xpath = Locators.tabs[tab_name]
                tab_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, tab_xpath)))
                if tab_name != list(Locators.tabs.keys())[0]:
                    self.navigate_to_element(tab_element)
                tab_element.click()
                method_to_call = getattr(self, method_name)
                method_to_call(sheet_name, common_stat_list)
    
    # Lead Actions ---

    def get_match_stats(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname    
        match_stats_xpath = Locators.match_stats_xpath
        alt_over_match_stat = Locators.alt_over_match_stat
        match_stats_list = [element for element in common_stat_list]
        data = ''
        for xpath_key in match_stats_xpath:
            # Exception used for innings where all batsmen got out. "Did not bat" rows disappears in this case
            try:
                element = self.driver.find_element(By.XPATH, match_stats_xpath[xpath_key])
            except:
                element = self.driver.find_element(By.XPATH, alt_over_match_stat[xpath_key])
            data = element.text
            match_stats_list.append(data)
        self.excel_action.write_stats(match_stats_list, sheetname)
    
    def get_batting_stats(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname
        for inns in Locators.inns_list:
            xpath_dict = dict(Locators.batsmen_xpath)
            key1 = inns
            key2 = list(Locators.batsmen_xpath[inns])[0]
            batsman_count = self.fetch_data_count(xpath_dict, key1, key2) # pass xpath dict, key1, key2
            # prepare main bat list 
            batting_stat_list = self.prepare_commonstat_list(common_stat_list, batsman_count)
            # common bat data ---
            #test part 

            #---
            element_list = [self.driver.find_element(By.XPATH, Locators.common_bat_xpath[inns][xpath_key]).text
            for xpath_key in Locators.common_bat_xpath[inns].keys()]
            print(element_list)
            for element in element_list:
                bowl_list = [element for _ in range(batsman_count)]
                batting_stat_list.append(bowl_list)
            # innings data ---
            current_inns = [1 if inns == Locators.inns_list[0] else 2 for _ in range(batsman_count) ]
            batting_stat_list.append(current_inns)
            # batting pos data ---
            batting_pos_list = list(range(1, batsman_count+1))
            batting_stat_list.append(batting_pos_list)
            # batting data ---
            batting_stats = [
                [element.text 
                for element in self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns][xpath_key])
                if element.text not in Locators.avoid_char]
                for xpath_key in Locators.batsmen_xpath[inns].keys()
            ]
            for batting_stat in batting_stats:
                batting_stat_list.append(batting_stat)
            self.excel_action.write_stats(batting_stat_list, sheetname)
    
    def get_inns_wkfall_stats(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname
        for inns in Locators.inns_list:
            # common data ---
            inns_stat_list = [element for element in common_stat_list]
            # common bat data ---
            element_list = [self.driver.find_element(By.XPATH, Locators.common_bat_xpath[inns][xpath_key]).text
            for xpath_key in Locators.common_bat_xpath[inns].keys()]
            for element in element_list:
                inns_stat_list.append(element)
            # innings data ---
            if inns == 'first_inns':
                current_inns = 1 
            else:
                current_inns = 2
            inns_stat_list.append(current_inns)
            # wkfll data
            raw_wkfall = self.driver.find_element(By.XPATH, Locators.innings_wkfall_xpath[inns]).text
            wkfall = raw_wkfall.replace("Fall of wickets:", "").replace("• \nDRS", "")
            inns_stat_list.append(wkfall)
            self.excel_action.write_stats(inns_stat_list, sheetname)

    def get_bowling_stats(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname 
        for inns in Locators.inns_list:
            xpath_dict = dict(Locators.bowling_xpath)
            key1 = inns
            key2 = list(Locators.bowling_xpath[inns])[0]
            bowler_count = self.fetch_data_count(xpath_dict, key1, key2) # pass xpath_dict, key1, key2
            bowling_stat_list = self.prepare_commonstat_list(common_stat_list, bowler_count)
            # common bowl data ---
            element_list = [self.driver.find_element(By.XPATH, Locators.common_bowl_xpath[inns][xpath_key]).text
            for xpath_key in Locators.common_bowl_xpath[inns].keys()]
            for element in element_list:
                bowl_list = [element for _ in range(bowler_count)]
                bowling_stat_list.append(bowl_list)
            # innings data ---
            current_inns = [1 if inns == Locators.inns_list[0] else 2 for _ in range(bowler_count) ]
            bowling_stat_list.append(current_inns)
            # bowling data ---
            bowling_stats = [
                [element.text 
                for element in self.driver.find_elements(By.XPATH, Locators.bowling_xpath[inns][xpath_key])
                if element.text not in Locators.avoid_char]
                for xpath_key in Locators.bowling_xpath[inns].keys()
            ]
            for bowling_stat in bowling_stats:
                bowling_stat_list.append(bowling_stat)
            self.excel_action.write_stats(bowling_stat_list, sheetname)
    
    def get_player_info(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname   
        for inns in Locators.inns_list:
            xpath_dict = dict(Locators.batsmen_xpath)
            key1 = inns
            key2 = list(Locators.batsmen_xpath[inns])[-1]
            batsman_count = self.fetch_data_count(xpath_dict, key1, key2) # pass xpath_dict, key1, key2 
            count = 0
            bat_bowl_xpaths = [
                self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['batsman_name']), 
                self.driver.find_elements(By.XPATH, Locators.bowling_xpath[inns]['bowler_name'])
            ]
            for i in range(len(bat_bowl_xpaths)):
                players_list = bat_bowl_xpaths[i]
                for players in players_list:
                    print(f"SAUDI ---{players.text}---")
                    if players.text not in Locators.avoid_char:
                        if i == 0:
                            if count < batsman_count:
                                try:
                                    ActionChains(self.driver).key_down(Keys.CONTROL).click(players).key_up(Keys.CONTROL).perform()
                                    self.driver.switch_to.window(self.driver.window_handles[2])
                                    time.sleep(2)
                                    self.fetch_player_info(sheetname, common_stat_list)
                                    self.driver.close()
                                    self.driver.switch_to.window(self.driver.window_handles[1])  
                                except:
                                    pass
                            count += 1
                        else:
                            ActionChains(self.driver).key_down(Keys.CONTROL).click(players).key_up(Keys.CONTROL).perform()
                            self.driver.switch_to.window(self.driver.window_handles[2])
                            time.sleep(2)
                            self.fetch_player_info(sheetname, common_stat_list)
                            self.driver.close()
                            self.driver.switch_to.window(self.driver.window_handles[1])  

    def get_mvp_stats(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname
        xpath_dict = dict(Locators.mvp_xpath)
        key1 = list(Locators.mvp_xpath)[0]
        key2 = ''
        total_mvps = self.fetch_data_count(xpath_dict, key1, key2) # pass xpath_dict, key1, key2 
        mvp_list = self.prepare_commonstat_list(common_stat_list, total_mvps)
        # Add the MVP sequence numbers (1, 2, 3, ...)
        mvp_list.append(list(range(1, total_mvps + 1)))
        # Gather MVP stats by iterating over the xpath keys
        mvp_stats = []
        for xpath_key in Locators.mvp_xpath.keys():
            elements = self.driver.find_elements(By.XPATH, Locators.mvp_xpath[xpath_key])
            mvp_stat = [element.text for element in elements if element.text not in Locators.avoid_char]
            mvp_stats.append(mvp_stat)
        # Append each MVP stat list to the main list
        mvp_list.extend(mvp_stats)
        # Print and write the final list to Excel
        self.excel_action.write_stats(mvp_list, sheetname)

    def get_commentary_stats(self, sheetname, common_stat_list):
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname 
        time.sleep(5) 
        # loop through teams
        for team_no in range(2):
            if team_no == 0:
                innings = 1
            else:
                innings = 2
            team_name = self.commentary_teams_dropdown_action(team_no)
            for dropdown_value in Locators.commentary_dropdown_values:
                c_type_text = self.commentary_type_dropdown_action(dropdown_value)
                self.expand_data_by_scroll(7)
                final_list = self.fetch_commentary_data(common_stat_list, innings, team_name, c_type_text)
                self.excel_action.write_stats(final_list, sheetname)

    def get_over_stats(self, sheetname, common_stat_list):
        self.sheetname = sheetname  
        self.common_stat_list = common_stat_list
        for inns in Locators.inns_list:
            dict_key2 = list(Locators.overs_xpath[inns])[1]
            over_nos = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, Locators.overs_xpath[inns][dict_key2])))
            self.open_overs(inns, over_nos)
            overs_list = self.prepare_commonstat_list(common_stat_list, len(over_nos))
            # team name list
            team_name_list = [self.driver.find_element(By.XPATH, Locators.overs_xpath[inns]['bowling_team']).text for over_no in over_nos]
            overs_list.append(team_name_list)
            # innings list
            current_inns = [1 if inns == 'first_inns' else 2 for over_no in over_nos]
            overs_list.append(current_inns)
            # overs stats
            over_stats = [
                [element.text 
                for element in self.driver.find_elements(By.XPATH, Locators.overs_xpath[inns][xpath_key])]
                for xpath_key in Locators.overs_xpath[inns].keys()
                if xpath_key != 'bowling_team'
            ]
            for over_stat in over_stats:
                overs_list.append(over_stat)
            overs_list[-1] = [
                ','.join(ball.replace('•', '0') 
                for ball in ball_score.split('\n'))
                for ball_score in overs_list[-1]
            ]
            self.excel_action.write_stats(overs_list, sheetname)

    # Support Actions ---

    def fetch_data_count(self, player_dict, key1, key2):
        count = 0
        if key2 != "":
            players = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, player_dict[key1][key2])))
        else:
            players = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, player_dict[key1])))
        for player in players:
            if player.text not in Locators.avoid_char:
                count += 1
        return count

    def fetch_common_stats(self):
        common_stat_list = []
        for c_stat_xpath_key, c_stat_xpath_value in Locators.common_stats_xpath.items():
            element = self.driver.find_element(By.XPATH, c_stat_xpath_value)
            data = element.text
            element_node = data.split()
            if c_stat_xpath_key == 'match_no':
                raw_data = data.split(',')
                data = raw_data[0]
                print(data)
            elif c_stat_xpath_key == 'series_format':
                raw_data = element_node[0]
                data = re.sub(r'\D', '', raw_data)
            elif c_stat_xpath_key == 'match_date':
                split_text = data.split(',')
                try:
                    index_2_data_temp = split_text[-3].strip()
                    parts = index_2_data_temp.split()
                    index_2_data = f"{parts[1]} {parts[0]}"
                except IndexError:
                    index_2_data_temp = split_text[-4].strip()
                    parts = index_2_data_temp.split()
                    index_2_data = f"{parts[1]} {parts[0]}"
                index_3_data = split_text[-2].strip()
                data = f"{index_2_data}, {index_3_data}"
            elif c_stat_xpath_key == 'match_session':
                raw_data = element_node[2]
                data = raw_data.replace("(", "").replace(")", "").replace(",", "")
            common_stat_list.append(data)
        return common_stat_list

    def fetch_commentary_data(self, common_stat_list, innings, team_name, c_type_text):
        self.common_stat_list = common_stat_list
        self.innings = innings
        self.team_name = team_name
        self.c_type_text = c_type_text
        overs_status = self.driver.find_elements(By.XPATH, Locators.commentary_xpath['overs_status'])
        balls_status = self.driver.find_elements(By.XPATH, Locators.commentary_xpath['balls_status'])
        baller_batsman_info = self.driver.find_elements(By.XPATH, Locators.commentary_xpath['baller_batsman_info'])
        data_col_length = len(overs_status)
        mylist = self.prepare_commonstat_list(common_stat_list, data_col_length)
        innings_list = [innings for _ in range(data_col_length)]
        mylist.append(innings_list)
        team_name_list = [team_name for _ in range(data_col_length)]
        mylist.append(team_name_list)
        c_type_text_list = [c_type_text for _ in range(data_col_length)]
        mylist.append(c_type_text_list)
        overs_list = [status.text for status in overs_status]
        balls_list = [status.text for status in balls_status]
        baller_batsman_list = [status.text for status in baller_batsman_info]
        mylist.append(overs_list)
        mylist.append(balls_list)
        mylist.append(baller_batsman_list)
        return mylist

    def fetch_player_info(self, sheetname, common_stat_list):
        player_info = self.driver.find_elements(By.XPATH, Locators.player_info_xpath)
        try:
            known_name_info = self.driver.find_element(By.XPATH, Locators.player_known_name_xpath).text
        except:
            known_name_info = 'NA'
        self.common_stat_list = common_stat_list
        self.sheetname = sheetname
        dict_keys, dict_values = [], []
        for i in range(1, len(player_info)+1):
            value_header = Locators.value_header.format(i=i)
            value_xpath = Locators.value_xpath.format(i=i)       
            dict_keys.append(self.driver.find_element(By.XPATH, value_header).text)
            try:
                dict_values.append(self.driver.find_element(By.XPATH, value_xpath).text)
            except:
                pass
        info_dict = dict(zip(dict_keys, dict_values))
        # Build the info_list based on known headers
        info_list = [info_dict.get(header, 'NA') for header in Locators.player_info_header]
        new_list = common_stat_list + [known_name_info] + info_list
        self.excel_action.write_stats(new_list, sheetname)
    
    def commentary_teams_dropdown_action(self, team_no):
        teams_dropdown_btn = self.driver.find_element(By.XPATH, Locators.commentary_xpath["teams_dropdown_btn"])
        teams_dropdown_btn.click()
        time.sleep(2)
        teams = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, Locators.commentary_xpath["teams_commentary"])))
        current_element = teams[team_no]
        team_name = current_element.text
        current_element.click()
        time.sleep(1) 
        return team_name

    def commentary_type_dropdown_action(self, xpath_key):
        self.xpath_key = xpath_key
        # commentary dropwdown open
        self.driver.find_element(By.XPATH, Locators.commentary_xpath['commentary_type_dropdown_btn']).click()
        time.sleep(1)
        # select wickets option
        commentary = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.commentary_xpath[xpath_key])))
        text = commentary.text
        commentary.click()
        time.sleep(1)
        return text

    def prepare_commonstat_list(self, common_stat_list, col_length):
        self.common_stat_list = common_stat_list
        self.col_length = col_length
        temp_list = []
        for element in common_stat_list:
            common_list = [element for _ in range(col_length)]
            temp_list.append(common_list)
        return temp_list
                
    def open_overs(self, inns, over_nos):
        # print('method called')
        self.inns = inns
        self.over_nos = over_nos
        container_open = True
        if self.inns == Locators.inns_list[0]:
            for over_no in self.over_nos:
                # print(over_no.text)
                if container_open == True:
                    container_open = False
                else:
                    over_no.click()  
                    time.sleep(2) 

    def wait_at_tournament(self):
        try:
            wait = WebDriverWait(self.driver, 15)  
            button = wait.until(EC.element_to_be_clickable((By.ID, 'wzrk-cancel')))    
            button.click()       
            return True
        except:
            print('No pop up appeared.')
            return True
    
    def wait_at_match(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            button =  wait.until(EC.element_to_be_clickable((By.XPATH, Locators.tabs[0])))
            button.click()
            return True
        except:
            print('No pop up appeared.')
            return True

    def navigate_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        for _ in range(5):
            ActionChains(self.driver).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        return True

    def expand_data_by_scroll(self, count):
        self.count = count
        for _ in range(count):
            ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1) 
        ActionChains(self.driver).send_keys(Keys.HOME).perform()
        return True
