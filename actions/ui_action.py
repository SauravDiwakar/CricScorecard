from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from locators import Locators
from actions.excel_action import ExcelAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UIAction:
    def __init__(self, url):
        self.url = url
        chromedriver_path = Locators.chromedriver_path 
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.excel_action = ExcelAction()

    def wait_time(self):
        try:
            wait = WebDriverWait(self.driver, 30)  
            button = wait.until(EC.element_to_be_clickable((By.ID, 'wzrk-cancel')))    
            button.click()       
            return True
        except:
            return False

    def open_web_page(self):   
        self.driver.get(self.url)
        time.sleep(1)
        for i in range(1, 75): # ipl24 tournament match range (min=1, max=74)
            if i in Locators.abandoned_matches:
                pass
            else:
                tournament_xpath = f"//div[@class='ds-mb-4']/div/div/div/div[{i}]/div/div[2]"
                matches = self.driver.find_element(By.XPATH, tournament_xpath)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", matches)
                for _ in range(5):
                    ActionChains(self.driver).send_keys(Keys.ARROW_UP).perform()
                time.sleep(1)
                ActionChains(self.driver).key_down(Keys.CONTROL).click(matches).key_up(Keys.CONTROL).perform()
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.wait_time()
                self.action_flow()
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                if i == 1:
                    self.wait_time()
        self.driver.quit()

    def action_flow(self):
        self.get_match_details()
        action_to_call = [
            lambda: self.get_inns_details(Locators.excel_sheets[0]), 
            lambda: self.get_mvp_details(Locators.excel_sheets[1]), 
            lambda: self.get_over_details(Locators.excel_sheets[2])
        ]
        for i in range(3): 
            btn = self.driver.find_element(By.XPATH, Locators.tabs[i]) 
            btn.click()
            time.sleep(1)  
            action_to_call[i]() 

    def get_match_details(self):    
        match_details_elements = Locators.match_details_elements
        match_details_list = [self.driver.find_element(By.XPATH, Locators.match_details_xpath[element]).text for element in match_details_elements]
        self.excel_action.write_match_details(match_details_list)
        return True

    def get_over_details(self, sheetname):
        self.sheetname = sheetname       
        container_open = True
        for inns in Locators.inns_list:
            over_nos = self.driver.find_elements(By.XPATH, Locators.overs_xpath[inns]['over_no'])
            if inns == 'first_inns':
                for over_no in over_nos:
                    if container_open == True:
                        container_open = False
                    else:
                        over_no.click()  
                        time.sleep(2) 
            overs_elements = Locators.overs_elements
            overs_list = [
                [element.text for element in self.driver.find_elements(By.XPATH, Locators.overs_xpath[inns][xpath_key])]
                for xpath_key in overs_elements.values()
            ]
            overs_list[-1] = [
                ','.join(ball.replace('•', '0') for ball in ball_score.split('\n'))
                for ball_score in overs_list[-1]
            ]
            overs_list.insert(1, [no.text for no in over_nos])
            self.excel_action.write_match_stats(overs_list, sheetname)

    def get_mvp_details(self, sheetname):
        self.sheetname = sheetname
        mvp_elements = Locators.mvp_elements
        mvp_list = [
                    [element.text for element in self.driver.find_elements(By.XPATH, Locators.mvp_xpath[xpath_key]) 
                    if element.text not in Locators.avoid_char]
                    for xpath_key in mvp_elements.values()
                    ]
        self.excel_action.write_match_stats(mvp_list, sheetname)

    def get_inns_details(self, sheetname):
        self.sheetname = sheetname
        inns_list = Locators.inns_list
        for inns in inns_list:
            self.inns_details(inns, sheetname)

    def inns_details(self, inns, sheetname):
        self.sheetname = sheetname
        self.inns = inns  
        for i in range(2):
            scorecard_elements = Locators.scorecard_elements[i] 
            if i == 0:
                scorecard_stat_list = [
                    [element.text for element in self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns][scorecard_element]) 
                    if element.text not in Locators.avoid_char]
                    for scorecard_element in scorecard_elements
                ]
            else:
                scorecard_stat_list = [
                    [element.text for element in self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns][scorecard_element])
                    if element.text not in Locators.avoid_char]
                    for scorecard_element in scorecard_elements
                ]
            self.excel_action.write_match_stats(scorecard_stat_list, sheetname)

