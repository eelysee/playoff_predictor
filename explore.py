import pandas as pd
import numpy as np
import os


def import_nba():
    '''
    retrieves data from .csv files.
    assigns them to variables
    '''
    nbastats = pd.read_csv('csv/nbastats_2022.csv')
    nbapo = pd.read_csv('csv/datanba_po_2022.csv')
    nbadata = pd.read_csv('csv/datanba_2022.csv')
    nbastats_po = pd.read_csv('csv/nbastats_po_2022.csv')
    pbpstats = pd.read_csv('csv/pbpstats_2022.csv')
    shotdetail = pd.read_csv('csv/shotdetail_2022.csv')
    shotdetail_po = pd.read_csv('csv/shotdetail_po_2022.csv')
    
    return nbastats, nbapo, nbadata, nbastats_po, pbpstats, shotdetail, shotdetail_po


def mvp_team():
    '''
    creates a dataframe for a time series model
    '''
    # This dictionary will be used to make a home catagory 
    # and an away catagory
    team_id_dict = {
        1610612755: "Philadelphia 76ers",
        1610612738: "Boston Celtics",
        1610612747: "Los Angeles Lakers",
        1610612744: "Golden State Warriors",
        1610612753: "Orlando Magic",
        1610612765: "Detroit Pistons",
        1610612764: "Washington Wizards",
        1610612754: "Indiana Pacers",
        1610612737: "Atlanta Hawks",
        1610612745: "Houston Rockets",
        1610612740: "New Orleans Pelicans",
        1610612751: "Brooklyn Nets",
        1610612748: "Miami Heat",
        1610612741: "Chicago Bulls",
        1610612761: "Toronto Raptors",
        1610612739: "Cleveland Cavaliers",
        1610612752: "New York Knicks",
        1610612763: "Memphis Grizzlies",
        1610612760: "Oklahoma City Thunder",
        1610612750: "Minnesota Timberwolves",
        1610612766: "Charlotte Hornets",
        1610612759: "San Antonio Spurs",
        1610612762: "Utah Jazz",
        1610612743: "Denver Nuggets",
        1610612756: "Phoenix Suns",
        1610612742: "Dallas Mavericks",
        1610612757: "Portland Trail Blazers",
        1610612758: "Sacramento Kings",
        1610612749: "Milwaukee Bucks",
        1610612746: "LA Clippers",
    }
    
    # htm dictionary to be converted into a team_id number
    htm_data = {
        "BOS": 1610612738,
        "GSW": 1610612744,
        "DET": 1610612765,
        "IND": 1610612754,
        "ATL": 1610612737,
        "BKN": 1610612751,
        "MIA": 1610612748,
        "TOR": 1610612761,
        "MEM": 1610612763,
        "MIN": 1610612750,
        "SAS": 1610612759,
        "UTA": 1610612762,
        "PHX": 1610612756,
        "SAC": 1610612758,
        "PHI": 1610612755,
        "LAL": 1610612747,
        "CHA": 1610612766,
        "WAS": 1610612764,
        "HOU": 1610612745,
        "NYK": 1610612752,
        "MIL": 1610612749,
        "DAL": 1610612742,
        "DEN": 1610612743,
        "ORL": 1610612753,
        "CLE": 1610612739,
        "CHI": 1610612741,
        "POR": 1610612757,
        "NOP": 1610612740,
        "LAC": 1610612746,
        "OKC": 1610612760
    }

    nbastats, nbapo, nbadata, nbastats_po, pbpstats, shotdetail, shotdetail_po = import_nba()
    
    # assigns the dfs i need to iterate for next step
    sdf = nbastats, nbadata, pbpstats, shotdetail
    
    # makes all columns lowercase
    for i in sdf:
        i.columns = [col.lower() for col in i.columns]
    
    # creating final dataframe from team
    team = shotdetail[['game_id', 'team_id', 'team_name', 'htm']]    
    
    # drop duplicates
    team = team.drop_duplicates(subset=['team_id','game_id'])
    
    # sorts df by game_id to be used as an index later
    team = team.sort_values('game_id')
    
    # changes the htm to a number
    team['htm'] = team['htm'].replace(htm_data)
    
    # renames to home and visitor
    team = team.rename(columns={'team_id':'visitor','htm':'home'})
    
    # drops the second copy of the game_id 
    team = team.loc[team['visitor'] != team['home']]
    
    # dropping team_name column
    team = team.drop(columns=['team_name'])
    
    # seperating final scores by game_id
    final_scores = nbadata.groupby('game_id').agg({'hs':'last', 'vs':'last'}).reset_index()
    # merging final scores onto teams
    team = team.merge(final_scores, on='game_id', how='left')
    
    # assigns 1 if home team won and 0 if home team lost
    team['result'] = np.where(team['hs'] > team['vs'], 1, 0)
    
    # set 'game_id' as the index
    team.set_index('game_id', inplace=True)
    
    # Initialize the new columns with NaN values
    team['hlast'] = np.nan
    team['vlast'] = np.nan

    # Loop through the DataFrame to populate hlast and vlast
    for idx, row in team.iterrows():
        # Get the home and visitor team ids
        home_team = row['home']
        visitor_team = row['visitor']

        # Find the last game for the home team
        prev_home_game = team[((team['home'] == home_team) | (team['visitor'] == home_team)) & (team.index < idx)]
        if not prev_home_game.empty:
            # If home team was the home team in their last game and won
            if (prev_home_game.iloc[-1]['home'] == home_team) and (prev_home_game.iloc[-1]['result'] == 1):
                team.at[idx, 'hlast'] = 1
            # If home team was the visitor team in their last game and lost
            elif (prev_home_game.iloc[-1]['visitor'] == home_team) and (prev_home_game.iloc[-1]['result'] == 0):
                team.at[idx, 'hlast'] = 1
            else:
                team.at[idx, 'hlast'] = 0

        # Find the last game for the visitor team
        prev_visitor_game = team[((team['home'] == visitor_team) | (team['visitor'] == visitor_team)) & (team.index < idx)]
        if not prev_visitor_game.empty:
            # If visitor team was the visitor team in their last game and won
            if (prev_visitor_game.iloc[-1]['visitor'] == visitor_team) and (prev_visitor_game.iloc[-1]['result'] == 0):
                team.at[idx, 'vlast'] = 1
            # If visitor team was the home team in their last game and lost
            elif (prev_visitor_game.iloc[-1]['home'] == visitor_team) and (prev_visitor_game.iloc[-1]['result'] == 1):
                team.at[idx, 'vlast'] = 1
            else:
                team.at[idx, 'vlast'] = 0

    # filling first game with losses
    # it is 16 observations
    team['hlast'].fillna(0, inplace=True)
    team['vlast'].fillna(0, inplace=True)

    # makes columns int, after i drop the nulls         
    team['hlast'] = team['hlast'].astype(int)
    team['vlast'] = team['vlast'].astype(int)

    
    # Create functions to compute rolling wins for home and visitor
    def home_last5_wins(row):
        previous_games = team[(team['home'] == row['home']) & (team.index < row.name)]
        return previous_games['result'].tail(5).sum()

    def visitor_last5_wins(row):
        previous_games = team[(team['visitor'] == row['visitor']) & (team.index < row.name)]
        return (1 - previous_games['result']).tail(5).sum()

    # Apply the functions row-wise to compute the rolling wins and assign to the desired column names
    team['home_last5'] = team.apply(home_last5_wins, axis=1)
    team['visitor_last5'] = team.apply(visitor_last5_wins, axis=1)

    # Convert to integers
    team['home_last5'] = team['home_last5'].astype(int)
    team['visitor_last5'] = team['visitor_last5'].astype(int)
    
    
    return team

    
    
    
    