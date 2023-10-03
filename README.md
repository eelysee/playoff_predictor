# playoff_predictor
Machine learning model to predict winners of first round of the 2022 nba playoffs.

## File explanation

os_helper.py - untitly module to move files around, see contents or zipped files, unzip bulk files.

API - API and directions to updating data or downloading data from the three sources. <https://github.com/shufinskiy/nba_apiv3/tree/master>

csv - file that contains all the relevant dataset


## Data Source
This dataset comprises NBA play-by-play data and shot details spanning from the 1996/1997 to 2022/23 seasons, with the latest update on 2023-07-11 incorporating playoff data for all seasons. The data is sourced from three platforms: 
* stats.nba.com 
* data.nba.com
* pbpstats.com 

Each of the datasets have a differnt start season and minor inconsistencies toughout the datasets. For this project we will only be using 2021-2022 , and 2022,2023 seanons and the first round of the playoff.



### nbastats

| Field           | Description                                             |
|-----------------|---------------------------------------------------------|
| **evt**         | Sequence number of the event in the game                |
| **wallclk**     | Wall clock time when the event occurred                 |
| **cl**          | Time until end of the quarter                           |
| **de**          | Description of the action                               |
| **locX**        | Coordinate of shot along the width of the court relative to its central axis |
| **locY**        | Coordinate of shot along the length of the court relative to its central axis |
| **opt1**        | Points                                                  |
| **opt2**        | Additional option (context-dependent)                   |
| **opt3**        | Additional option (context-dependent)                   |
| **opt4**        | Additional option (context-dependent)                   |
| **tid**         | Team ID                                                 |
| **pid**         | Player ID                                               |
| **hs**          | Home team score                                         |
| **vs**          | Visitor team score                                      |
| **epid**        | Extra player ID (context-dependent)                     |
| **oftid**       | Team ID in offense                                      |
| **ord**         | Order number (context-dependent)                        |
| **pts**         | Points scored in the event                               |
| **PERIOD**      | Quarter number                                          |
| **GAME_ID**     | Game ID                                                 |


### pbpstats
| Field                           | Description                                              |
|---------------------------------|----------------------------------------------------------|
| **ENDTIME**                     | Time until end of the quarter at time of end of possession |
| **EVENTS**                      | Description of all actions in possession                 |
| **FG2A**                        | Count of 2PT Field Goal attempts in possession           |
| **FG2M**                        | Count of 2PT Field Goals made in possession              |
| **FG3A**                        | Count of 3PT Field Goal attempts in possession           |
| **FG3M**                        | Count of 3PT Field Goals made in possession              |
| **GAMEDATE**                    | Game date                                                |
| **GAMEID**                      | Game ID                                                  |
| **NONSHOOTINGFOULSTHATRESULTEDINFTS** | Non-shooting fouls that resulted in free throws    |
| **OFFENSIVEREBOUNDS**           | Count of offensive rebounds in possession                |
| **OPPONENT**                    | Abbreviation of the team in defense                      |
| **PERIOD**                      | Quarter number                                           |
| **SHOOTINGFOULSDRAWN**          | Shooting fouls drawn                                     |
| **STARTSCOREDIFFERENTIAL**      | Difference in score at the start of possession           |
| **STARTTIME**                   | Time until end of the quarter at time of start of possession |
| **STARTTYPE**                   | Type of start (context-dependent)                        |
| **TURNOVERS**                   | Turnovers                                                |
| **DESCRIPTION**                 | Description of action                                    |
| **URL**                         | Link to video                                            |



### datanba

| Field           | Description                                             |
|-----------------|---------------------------------------------------------|
| **evt**         | Sequence number of the event in the game                |
| **wallclk**     | Wall clock time when the event occurred                 |
| **cl**          | Time until end of the quarter                           |
| **de**          | Description of the action                               |
| **locX**        | Coordinate of shot along the width of the court relative to its central axis |
| **locY**        | Coordinate of shot along the length of the court relative to its central axis |
| **opt1**        | Points                                                  |
| **opt2**        | Additional option (context-dependent)                   |
| **mtype**       | Type of the move (context-dependent)                    |
| **etype**       | Type of the event (context-dependent)                   |
| **opid**        | Opponent player ID (context-dependent)                  |
| **tid**         | Team ID                                                 |
| **pid**         | Player ID                                               |
| **hs**          | Home team score                                         |
| **vs**          | Visitor team score                                      |
| **epid**        | Extra player ID (context-dependent)                     |
| **oftid**       | Team ID in offense                                      |
| **ord**         | Order number (context-dependent)                        |
| **PERIOD**      | Quarter number                                          |
| **GAME_ID**     | Game ID                                                 |




### shotdetail

| Field                 | Description                                               |
|-----------------------|-----------------------------------------------------------|
| **GRID_TYPE**         | Shot Chart Detail                                         |
| **GAME_ID**           | Game ID                                                   |
| **GAME_EVENT_ID**     | Sequence number of the event in the game                  |
| **PLAYER_ID**         | ID of player who made the shot                            |
| **PLAYER_NAME**       | Name of player who made the shot                          |
| **TEAM_ID**           | Team ID of player who made the shot                       |
| **TEAM_NAME**         | Team name of player who made the shot                     |
| **PERIOD**            | Quarter number                                            |
| **MINUTES_REMAINING** | Minutes remaining until end of the quarter                |
| **SECONDS_REMAINING** | Seconds remaining until end of the quarter                |
| **EVENT_TYPE**        | Made or Missed shot                                       |
| **ACTION_TYPE**       | Type of shot                                              |
| **SHOT_TYPE**         | 2PT or 3PT shot                                           |
| **SHOT_ZONE_BASIC**   | General area on the court where the shot was taken        |
| **SHOT_ZONE_AREA**    | Specific area on the court where the shot was taken       |
| **SHOT_ZONE_RANGE**   | Distance range of the shot                                |
| **SHOT_DISTANCE**     | Distance to the rim                                       |
| **LOC_X**             | Coordinate of the shot along the width of the court relative to its central axis |
| **LOC_Y**             | Coordinate of the shot along the length of the court relative to its central axis |
| **SHOT_ATTEMPTED_FLAG**| Shot execution flag (always 1)                           |
| **SHOT_MADE_FLAG**    | Shot made flag (0 or 1)                                   |
| **GAME_DATE**         | Game date                                                 |
| **HTM**               | Abbreviation of home team                                 |
| **VTM**               | Abbreviation of away team                                 |




