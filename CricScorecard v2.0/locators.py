class Locators:
    # Utilities
    chromedriver_path = 'C:/Users/SAUDI/Documents/seleniumdrivers/chromedriver.exe'   
    tournament_xpath = "//div[@class='ds-mb-4']/div/div/div/div[{match_no}]/div/div[2]"
    tournament_len_xpath = "//div[@class='ds-mb-4']/div/div/div/div/div/div[2]"
    first_match_no = 1
    tournament = {
        "ipl_24" : {
            "url" : "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results",
            "abandoned_matches" : [63, 66, 70]
        },
        "ipl_23" : {
            "url" : "https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results",
            "abandoned_matches" : [45]
        },
        "t20WC_2024" : {
            "url" : "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/match-schedule-fixtures-and-results",
            "abandoned_matches" : [6, 23, 30, 33]
        },
        "SL_vs_IND_2024" : {
            "url" : "https://www.espncricinfo.com/series/india-in-sri-lanka-2024-1442984/match-schedule-fixtures-and-results",
            "abandoned_matches" : []
        }
    }
    sheet_to_tab = {
        "match_stats" : ("Scorecard", "get_match_stats"),
        "bat_stat" : ("Scorecard", "get_batting_stats"),
        "innings_wkfall" : ("Scorecard", "get_inns_wkfall_stats"),
        "bowl_stat" : ("Scorecard", "get_bowling_stats"),
        "player_info" : ("Scorecard", "get_player_info"),
        "mvp" : ("MVP", "get_mvp_stats"),
        "commentary" : ("Commentary", "get_commentary_stats"),
        "overs" : ("Overs", "get_over_stats")            
    }
    tabs = {
        "Scorecard" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/a/span",
        "MVP" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[3]/a/span",
        "Commentary" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[5]/a/span",
        "Overs" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[7]/a/span"
        # "Scorecard" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/a/span",
        # "Commentary" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[4]/a/span",
        # "Overs" :"//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[2]/div/div[6]/a/span"
    }
    excel_sheets = {
        'match_stats' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'toss', 'team_batting_first', 'first_innings_score',
            'team_batting_second', 'second_innings_score', 'match_result', 'first_innings_overs_completed', 'second_innings_overs_completed'], 
        'bat_stat' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'team_name', 'team_score', 'vs_team', 'innings', 'batting_pos', 'batsman_name', 'wicket_taker', 'runs_scored', 'balls_faced', 'mins_played', 'fours_hit', 'sixes_hit', 's/r'], 
        'innings_wkfall' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'team_name', 'team_score', 'vs_team', 'innings', 'wickets_fall'], 
        'bowl_stat' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'team_name', 'vs_team', 'vs_team_score', 'innings', 'bowler_name', 'overs_bowled', 'maiden_bowled', 'runs_conceded', 'wickets_taken', 'bowler_econ', 'dot_balls_bowled', 'fours_conceded', 'sixes_conceded', 'wide_balls_bowled', 'no_balls_bowled'], 
        'player_info' :
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'player_known_name', 'player_full_name', 'player_born', 'player_role', 'player_batting_style', 'player_bowling_style'],
        'mvp' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'mvp_no', 'mvp_player_name', 'mvp_team', 'total_impact', 'mvp_run', 'impact_runs', 'batting_impact', 'mvp_bowl', 'impact_wkts', 'bowler_impact'],
        'commentary' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'innings', 'team', 'commentary_type', 'over_status', 'ball_status', 'bowler_batsman'],
        'overs' : 
            ['series_name', 'series_season', 'series_format', 'match_date', 'match_no', 'match_ground', 'bowling_team', 'innings', 'over_no', 'over_score', 'run_rate', 'bowler_name', 'over_balls']        
    }
    avoid_char = ['', ' ']
    inns_list = ['first_inns', 'second_inns']

    # SCORECARD TAB -------------------------------------------------------------------------
    # Match Stats 
    common_stats_xpath = {
        'series_name' : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/a/span",
        'series_season' : "//div[@class='ds-mt-3']/div[1]/div[last()]/div[2]/table/tbody/tr[4]/td[2]/a/span",
        'series_format' : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[1]/div/span/span[2]",
        'match_date' : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]",
        'match_no' : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]", 
        'match_ground' : "//div[@class='ds-mt-3']/div[1]/div[last()]/div[2]/table/tbody/tr[1]/td/a/span",
    }    
    match_stats_xpath = {
        'toss' : "//div[@class='ds-mt-3']/div[1]/div[last()]/div[2]/table/tbody/tr[2]/td[2]/span",
        "team_batting_first" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a//span",
        "first_innings_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/strong",
        "team_batting_second" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/a//span",
        "second_innings_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/strong",
        "match_result" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/p/span",
        'first_innings_overs_completed' : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr[last()-2]/td[2]/div/span[1]",
        "second_innings_overs_completed" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr[last()-2]/td[2]/div/span[1]",
    }
    alt_over_match_stat = {
        'first_innings_overs_completed' : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr[last()-1]/td[2]/div/span[1]",
        "second_innings_overs_completed" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr[last()-1]/td[2]/div/span[1]",
    }
    
    # Batsman Stat Xpath
    batsmen_xpath = {
        "first_inns": {
            "batsman_name": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[1]",
            "wicket_taker": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[2]",
            "runs_scored": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[3]",
            "balls_faced": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[4]",
            "mins_played": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[5]",
            "fours_hit": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[6]",
            "sixes_hit": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[7]",
            "s/r": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[8]"
        },
        "second_inns": {
            # "batsman_name": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[1]",
            "batsman_name": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[1]/div/div/a",
            "wicket_taker": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[2]",
            "runs_scored": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[3]",
            "balls_faced": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[4]",
            "mins_played": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[5]",
            "fours_hit": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[6]",
            "sixes_hit": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[7]",
            "s/r": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[8]"
        }
    }
    common_bat_xpath = {
        "first_inns" : {
            "team_name" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a//span",
            "team_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/strong",
            "vs_team" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/a//span"  
        },
        "second_inns" : {
            "team_name" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/a//span",
            "team_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/strong",
            "vs_team" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a//span"
        }
    }

    # Innings Wicketfall Xpath 
    innings_wkfall_xpath = {
        "first_inns" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr[last()]/td[1]",
        "second_inns" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr[last()]/td[1]"
    }

    # Bowler Stat Xpath
    bowling_xpath = {
        "first_inns" : {
            "bowler_name" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[1]/div/div/a/span",
            "overs_bowled" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[2]",
            "maiden_bowled" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[3]",
            "runs_conceded" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[4]",
            "wickets_taken" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[5]",
            "bowler_econ" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[6]",
            "dot_balls_bowled" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[7]",
            "fours_conceded" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[8]",
            "sixes_conceded" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[9]",
            "wide_balls_bowled" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[10]",
            "no_balls_bowled" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[11]"
        },
        "second_inns" : {
            "bowler_name" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[1]/div/div/a/span",
            "overs_bowled" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[2]",
            "maiden_bowled" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[3]",
            "runs_conceded" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[4]",
            "wickets_taken" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[5]",
            "bowler_econ" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[6]",
            "dot_balls_bowled" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[7]",
            "fours_conceded" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[8]",
            "sixes_conceded" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[9]",
            "wide_balls_bowled" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[10]",
            "no_balls_bowled" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[11]"
        }
    }
    common_bowl_xpath = {
        "first_inns" : {
            "team_name" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/a//span",
            "vs_team" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a//span",
            "vs_team_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/strong"
        },
        "second_inns" : {
            "team_name" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a//span",
            "vs_team" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/a//span",
            "vs_team_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/strong"
        }
    }

    # Player Info Xpath 
    player_info_xpath = "//div[@class='ds-grow']/div[2]/div/div/div[1]/div/span/p"
    player_known_name_xpath = "//div[@class='ds-flex-none']/div[1]/div/div/div/div[1]/div/div[1]/h1"
    player_info_header = ['FULL NAME', 'BORN', 'PLAYING ROLE', 'BATTING STYLE', 'BOWLING STYLE']
    value_header = "//div[@class='ds-grow']/div[2]/div/div/div[1]/div[{i}]/p"
    value_xpath = "//div[@class='ds-grow']/div[2]/div/div/div[1]/div[{i}]/span/p"  


    # MVP TAB --------------------------------------------------------------------------------
    mvp_xpath = {
        "mvp_player_name" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[1]/div/a/span",
        "mvp_team" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[2]",
        "total_impact" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[3]",
        "mvp_run" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[4]",
        "impact_runs" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[5]",
        "batting_impact" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[6]",
        "mvp_bowl" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[7]",
        "impact_wkts" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[8]",
        "bowler_impact" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[9]"
    }


    # COMMENTARY TAB ---------------------------------------------
    commentary_xpath = {
        "teams_dropdown_btn" : '//div[@class="ds-mt-3"]/div[1]/div[1]/div/div[2]/div/div/i',
        "commentary_type_dropdown_btn" : '//div[@class="ds-mt-3"]/div[1]/div[1]/div/div[3]/div/div/i',
        "teams_commentary" : '//div[@class="tippy-content"]/div/div/div/ul/li',
        "wickets_commentary" : '//div[@class="tippy-content"]/div/div/div/ul/li[2]',
        "boundaries_commentary" : '//div[@class="tippy-content"]/div/div/div/ul/li[3]',
        "overs_status" : '//div[@class="ds-mt-3"]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div[1]/span',
        "balls_status" : '//div[@class="ds-mt-3"]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/div/span',
        "baller_batsman_info" : '//div[@class="ds-mt-3"]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/span',
    }
    commentary_dropdown_values = ["wickets_commentary", "boundaries_commentary"]


    # OVERS TAB --------------------------------------------------------------------------------
    overs_xpath = {
        "first_inns" : {
            "bowling_team" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/thead/tr/th[3]",
            "over_no" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/div",
            "over_score" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/div[1]/div",
            "run_rate" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/div[2]/div[last()]",
            "bowler_name" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/div[2]/div[1]",
            "over_balls" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/div[2]/div[2]",
        },
        "second_inns" : {
            "bowling_team" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/thead/tr/th[2]",
            "over_no" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/div",
            "over_score" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div/div[1]/div",
            "run_rate" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div/div[2]/div[last()]",
            "bowler_name" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div/div[2]/div[1]",
            "over_balls" : "/html/body/div[1]/section/section/div[5]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div/div[2]/div[2]",
        }
    }
