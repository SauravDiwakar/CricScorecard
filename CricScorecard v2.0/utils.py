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
import re

def get_common_stats(self):
        common_stat_list = []
        for c_stat_xpath_key, c_stat_xpath_value in Locators.common_stats_xpath.items():
            element = self.driver.find_element(By.XPATH, c_stat_xpath_value)
            data = element.text
            element_node = data.split()
            if c_stat_xpath_key == 'match_no':
                raw_data = element_node[3]
                data = re.sub(r'\D', '', raw_data)
            elif c_stat_xpath_key == 'series_format':
                raw_data = element_node[5]
                data = re.sub(r'\D', '', raw_data)
            elif c_stat_xpath_key == 'match_date':
                data = f'{element_node[0]} {element_node[1]} {element_node[2]}'
            common_stat_list.append(data)
        return common_stat_list

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