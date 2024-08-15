# CricScorecard README

## Description

- This python based project creates an excel file data of each cricket match from a tournament. 
- Its purpose is to automate data fetch and storage in local.

## Features

- Reads all matches in the tournament. 
- Generates excel files for each match.
- Quality data like scorecard, mvp and overs. 
- The program jumps off the abandoned matches. 
- The tournament link and abandoned matches number are hard coded. 
- Each file represents respective match. 
- Data consists of scorecard, mvp and overs details in respective sheets.

## Requirements

1. Python version 
 - Python 3.0 or above

2. Drivers 
 - chromedriver (version same as google chrome browser version) 

3. Libraries
 - Internal = time
 - External = selenium, // pip install selenium
	      openpyxl // pip install openpyxl

4. Tournament link and abandoned matches number in the tournament.

## How to use

1. Download the project zip file. 
2. Open your IDE and create folder workspace.
3. Install all the external libraries. 
4. Open locators.py and add tournament link under 'url' variable. (The file also contains various xpaths. The ones in this file have been removed for generic reasons.) 
5. Under the same file, there is a python list 'abandoned_matches'. Add the match numbers which were abandoned in the tournament. Furthermore, add the installed chromedriver path under "chromedriver_path" variable.  
6. Switch to ui_action.py file and navigate to line 33. Add one number greater than the total number of matches in the tournament. 
7. Run main.py.

## Output

- If a tournament has 25 matches and match number 2 and 17 were abandoned, then the program will create 23 excel files each from the 23 played matches in the tournament. 
- Each file will have three sheets, named 'Scorecard', 'MVP' and 'Overs'. 
- Refer to the sample output excel file for more information. (tournament = ipl24)

## Versions

- This is CricScorecard version 1.0.

## Contributing
Contributions are welcome! Follow these steps to contribute:

 - Fork the repository
 - Create a new branch (git checkout -b feature-branch)
 - Make your changes
 - Commit your changes (git commit -m 'Add feature')
 - Push to the branch (git push origin feature-branch)
 - Open a pull request

## License
- Currently, the project does not have license.  