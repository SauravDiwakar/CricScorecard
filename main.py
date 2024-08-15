from actions.ui_action import UIAction
from locators import Locators

class CricScorecard:
    def __init__(self):
        ui_action = UIAction(Locators.url)
        ui_action.open_web_page()

if __name__ == '__main__':
    CricScorecard()
