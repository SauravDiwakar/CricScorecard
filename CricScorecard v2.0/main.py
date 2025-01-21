from actions.ui_action import UIAction
from locators import Locators

class CricScorecard:
    def __init__(self):
        # tournament_name  = "ipl_24"
        # url = Locators.tournament[tournament_name]["url"]
        # abandoned_matches = Locators.tournament[tournament_name]["abandoned_matches"]
        series_data = {
            # "West Indies in Pakistan T20I Series": "https://www.espncricinfo.com/series/west-indies-in-pakistan-t20is-2021-22-1287767/match-schedule-fixtures-and-results",
            # "Namibia in Zimbabwe T20I Series": "https://www.espncricinfo.com/series/namibia-in-zimbabwe-t20is-2022-1310916/match-schedule-fixtures-and-results",
            # "Afghanistan in Zimbabwe T20I Series": "https://www.espncricinfo.com/series/afghanistan-in-zimbabwe-t20is-2022-1310920/match-schedule-fixtures-and-results",
            # "Bangladesh in West Indies T20I Series": "https://www.espncricinfo.com/series/bangladesh-in-west-indies-t20is-2022-1317145/match-schedule-fixtures-and-results",
            # "India in England T20I Series": "https://www.espncricinfo.com/series/india-in-england-t20is-2022-1276894/match-schedule-fixtures-and-results",
            # "New Zealand in Ireland T20I Series": "https://www.espncricinfo.com/series/new-zealand-in-ireland-t20is-2022-1303303/match-schedule-fixtures-and-results",
            # "New Zealand in Scotland T20I Series": "https://www.espncricinfo.com/series/new-zealand-in-scotland-t20is-2022-1307473/match-schedule-fixtures-and-results",
            # "South Africa in England T20I Series": "https://www.espncricinfo.com/series/south-africa-in-england-t20is-2022-1276898/match-schedule-fixtures-and-results",
            # "Bangladesh in Zimbabwe T20I Series": "https://www.espncricinfo.com/series/bangladesh-in-zimbabwe-t20is-2022-1323291/match-schedule-fixtures-and-results",
            # "New Zealand in Netherlands T20I Series": "https://www.espncricinfo.com/series/new-zealand-in-netherlands-t20i-series-2022-1310900/match-schedule-fixtures-and-results",
            # "South Africa v Ireland T20I Series (in England)": "https://www.espncricinfo.com/series/south-africa-v-ireland-t20is-2022-1303306/match-schedule-fixtures-and-results",
            # "West Indies v India T20I Series (in United States of America/West Indies)": "https://www.espncricinfo.com/series/west-indies-v-india-t20i-series-2022-1317887/match-schedule-fixtures-and-results",
            # "New Zealand in West Indies T20I Series": "https://www.espncricinfo.com/series/new-zealand-in-west-indies-t20is-2022-1317889/match-schedule-fixtures-and-results",
            # "Afghanistan in Ireland T20I Series": "https://www.espncricinfo.com/series/afghanistan-tour-of-ireland-t20is-2022-1307158/match-schedule-fixtures-and-results",
            # "Men's T20 Asia Cup": "https://www.espncricinfo.com/series/men-s-t20-asia-cup-2022-1327237/match-schedule-fixtures-and-results",
            # "Australia in India T20I Series": "https://www.espncricinfo.com/series/australia-in-india-t20is-2022-1327498/match-schedule-fixtures-and-results",
            # "Bangladesh in United Arab Emirates T20I Series": "https://www.espncricinfo.com/series/bangladesh-in-united-arab-emirates-t20is-2022-1336022/match-schedule-fixtures-and-results",
            # "England in Pakistan T20I Series": "https://www.espncricinfo.com/series/england-in-pakistan-t20is-2022-1327227/match-schedule-fixtures-and-results",
            # "South Africa in India T20I Series (2022-23)": "https://www.espncricinfo.com/series/south-africa-in-india-t20is-2022-23-1327501/match-schedule-fixtures-and-results",
            # "West Indies in Australia T20I Series": "https://www.espncricinfo.com/series/west-indies-in-australia-t20is-2022-23-1317466/match-schedule-fixtures-and-results",
            # "New Zealand T20I Tri-Series": "https://www.espncricinfo.com/series/new-zealand-t20i-tri-series-2022-23-1322281/match-schedule-fixtures-and-results",
            "Indian Premier League (in India)": "https://www.espncricinfo.com/series/indian-premier-league-2012-520932/match-schedule-fixtures-and-results"
        }


        for series_name, series_url in series_data.items():
            print(f"--------------CURRENT SERIES ==={series_name}--------------")
            tournament_name  = series_name
            url = series_url
            # if series_name in ("South Africa in India T20I Series"):
            #     abandoned_matches = [5]
            # else:
            #     abandoned_matches = []
            abandoned_matches = [32, 34]
            ui_action = UIAction(tournament_name, url, abandoned_matches)
            ui_action.open_web_page()


if __name__ == '__main__':
    CricScorecard()

