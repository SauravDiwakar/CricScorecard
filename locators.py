class Locators:

    # MATCH DETAILS -------------------------------------------------------------------------
    chromedriver_path = 'C:/path/chromedriver.exe'   
    url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results"
    tabs = ["write xpath here", #scorecardbtn_xpath
        "write xpath here", #mvpbtn_xpath
        "write xpath here" #oversbtn_xpath
        ]
    excel_sheets = ['Scorecard', 'MVP', 'Overs']
    avoid_char = ['', ' ']
    inns_list = ['first_inns', 'second_inns']
    abandoned_matches = [63, 66, 70] #ipl24
    match_details_elements = ["match_details", "team_a", "team_a_score", "team_b", "team_b_played_overs_target", "team_b_score", "match_result"]
    match_details_xpath = {
        "match_details" : "write xpath here",
        "team_a" : "write xpath here",
        "team_a_score" : "write xpath here",
        "team_b" : "write xpath here",
        "team_b_played_overs_target" : "write xpath here",
        "team_b_score" : "write xpath here",
        "match_result" : "write xpath here"
    }
    
    # SCORECARD ---------------------------------------------------------------------------
    scorecard_elements = [
        ['batting_header', 'batsmen', 'status', 'runs', 'played_balls', 'played_mins', '4s', '6s', 'sr'], 
        ['bowling_header', 'bowler', 'bowler_over', 'bowler_maiden', 'bowler_run', 'bowler_wicket', 'bowler_econ', 'bowler_0s', 'bowler_4s', 'bowler_6s', 'bowler_wide', 'bowler_nb']
        ]
    bowlers_xpath = {
        "first_inns" : {
            "bowling_header" : "write xpath here",
            "bowler" : "write xpath here",
            "bowler_over" : "write xpath here",
            "bowler_maiden" : "write xpath here",
            "bowler_run" : "write xpath here",
            "bowler_wicket" : "write xpath here",
            "bowler_econ" : "write xpath here",
            "bowler_0s" : "write xpath here",
            "bowler_4s" : "write xpath here",
            "bowler_6s" : "write xpath here",
            "bowler_wide" : "write xpath here",
            "bowler_nb" : "write xpath here"
        },
        "second_inns" : {
            "bowling_header" : "write xpath here",
            "bowler" : "write xpath here",
            "bowler_over" : "write xpath here",
            "bowler_maiden" : "write xpath here",
            "bowler_run" : "write xpath here",
            "bowler_wicket" : "write xpath here",
            "bowler_econ" : "write xpath here",
            "bowler_0s" : "write xpath here",
            "bowler_4s" : "write xpath here",
            "bowler_6s" : "write xpath here",
            "bowler_wide" : "write xpath here",
            "bowler_nb" : "write xpath here"
        }
    }

    batsmen_xpath = {
        "first_inns": {
            "batting_header": "write xpath here",
            "batsmen": "write xpath here",
            "status": "write xpath here",
            "runs": "write xpath here",
            "played_balls": "write xpath here",
            "played_mins": "write xpath here",
            "4s": "write xpath here",
            "6s": "write xpath here",
            "sr": "write xpath here"
        },
        "second_inns": {
            "batting_header": "write xpath here",
            "batsmen": "write xpath here",
            "status": "write xpath here",
            "runs": "write xpath here",
            "played_balls": "write xpath here",
            "played_mins": "write xpath here",
            "4s": "write xpath here",
            "6s": "write xpath here",
            "sr": "write xpath here"
        }
    }

    # MVP --------------------------------------------------------------------------------
    mvp_elements = {
        'mvp_headers': 'mvp_header',
        'mvp_players': 'mvp_player',
        'mvp_teams': 'mvp_team',
        'mvp_tis': 'mvp_ti',
        'mvp_runs': 'mvp_run',
        'mvp_i_runs': 'mvp_i_run',
        'mvp_b_impacts': 'mvp_b_impact',
        'mvp_bowls': 'mvp_bowl',
        'mvp_i_wkts': 'mvp_i_wkt',
        'mvp_bo_impacts': 'mvp_bo_impact'
        }
    mvp_xpath = {
        "mvp_header" : "write xpath here",
        "mvp_player" : "write xpath here",
        "mvp_team" : "write xpath here",
        "mvp_ti" : "write xpath here",
        "mvp_run" : "write xpath here",
        "mvp_i_run" : "write xpath here",
        "mvp_b_impact" : "write xpath here",
        "mvp_bowl" : "write xpath here",
        "mvp_i_wkt" : "write xpath here",
        "mvp_bo_impact" : "write xpath here"
    }

    # OVERS --------------------------------------------------------------------------------
    overs_elements = {
                'overs_headers': 'overs_header',
                'over_scores': 'over_score',
                'over_rrs': 'over_rr',
                'bowlers': 'bowler',
                'ball_to_balls': 'ball_to_ball'
            }
    overs_xpath = {
        "first_inns" : {
            "overs_header" : "write xpath here",
            "over_no" : "write xpath here",
            "over_score" : "write xpath here",
            "bowler" : "write xpath here",
            "ball_to_ball" : "write xpath here",
            "over_rr" : "write xpath here",
        },
        "second_inns" : {
            "overs_header" : "write xpath here",
            "over_no" : "write xpath here",
            "over_score" : "write xpath here",
            "bowler" : "write xpath here",
            "ball_to_ball" : "write xpath here",
            "over_rr" : "write xpath here"
        }
    }