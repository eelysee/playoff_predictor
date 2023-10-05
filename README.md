# playoff_predictor
Machine learning model to predict winners of first round of the 2022 nba playoffs.

**Project Summary: Predicting NBA Playoff Winners Using Machine Learning**

**Objective:**  
Predict the outcome of NBA playoff games using team performance metrics from the regular season (2022-2023).


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

Stats not available or missing values were updated by api.



### nbastats


| Field                      | Description                                          |
|----------------------------|------------------------------------------------------|
| **GAME_ID**                | Game ID                                              |
| **EVENTNUM**               | Sequence number of the event                         |
| **EVENTMSGTYPE**           | Type of event (e.g., shot, rebound, foul)            |
| **EVENTMSGACTIONTYPE**     | Subtype or specific action of the event              |
| **PERIOD**                 | Quarter number                                       |
| **WCTIMESTRING**           | Wall-clock time when the event occurred              |
| **PCTIMESTRING**           | Time remaining in the quarter                        |
| **HOMEDESCRIPTION**        | Description of the home team action                  |
| **NEUTRALDESCRIPTION**     | Description of a neutral action (e.g., start of period) |
| **VISITORDESCRIPTION**     | Description of the visitor team action               |
| **SCORE**                  | Current game score at the time of the event          |
| **SCOREMARGIN**            | Score margin at the time of the event                |
| **PERSON1TYPE**            | Type identifier for the first person involved        |
| **PLAYER1_ID**             | ID of the player who performed the main action       |
| **PLAYER1_NAME**           | Name of the player who performed the main action     |
| **PLAYER1_TEAM_ID**        | Team ID of the player who performed the main action  |
| **PLAYER1_TEAM_CITY**      | Team city of the player who performed the main action|
| **PLAYER1_TEAM_NICKNAME**  | Team nickname of the player who performed the main action |
| **PLAYER1_TEAM_ABBREVIATION**| Team abbreviation of the player who performed the main action|
| **PERSON2TYPE**            | Type identifier for the second person involved       |
| **PLAYER2_ID**             | ID of the player who performed a side action         |
| **PLAYER2_NAME**           | Name of the player who performed a side action       |
| **PLAYER2_TEAM_ID**        | Team ID of the player who performed a side action    |
| **PLAYER2_TEAM_CITY**      | Team city of the player who performed a side action  |
| **PLAYER2_TEAM_NICKNAME**  | Team nickname of the player who performed a side action |
| **PLAYER2_TEAM_ABBREVIATION**| Team abbreviation of the player who performed a side action|
| **PERSON3TYPE**            | Type identifier for the third person involved        |
| **PLAYER3_ID**             | ID of the player who performed a second side action  |
| **PLAYER3_NAME**           | Name of the player who performed a second side action|
| **PLAYER3_TEAM_ID**        | Team ID of the player who performed a second side action|
| **PLAYER3_TEAM_CITY**      | Team city of the player who performed a second side action|
| **PLAYER3_TEAM_NICKNAME**  | Team nickname of the player who performed a second side action|
| **PLAYER3_TEAM_ABBREVIATION**| Team abbreviation of the player who performed a second side action|
| **VIDEO_AVAILABLE_FLAG**   | Indicates if a video of the event is available       |



### nbadata

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



| Team Name                 | team_id       |
|---------------------------|---------------|
| Atlanta Hawks            | **1610612737** |
| Boston Celtics           | **1610612738** |
| Brooklyn Nets            | **1610612751** |
| Charlotte Hornets        | **1610612766** |
| Chicago Bulls            | **1610612741** |
| Cleveland Cavaliers      | **1610612739** |
| Dallas Mavericks         | **1610612742** |
| Denver Nuggets           | **1610612743** |
| Detroit Pistons          | **1610612765** |
| Golden State Warriors    | **1610612744** |
| Houston Rockets          | **1610612745** |
| Indiana Pacers           | **1610612754** |
| LA Clippers              | **1610612746** |
| Los Angeles Lakers       | **1610612747** |
| Memphis Grizzlies        | **1610612763** |
| Miami Heat               | **1610612748** |
| Milwaukee Bucks          | **1610612749** |
| Minnesota Timberwolves   | **1610612750** |
| New Orleans Pelicans     | **1610612740** |
| New York Knicks          | **1610612752** |
| Oklahoma City Thunder    | **1610612760** |
| Orlando Magic            | **1610612753** |
| Philadelphia 76ers       | **1610612755** |
| Phoenix Suns             | **1610612756** |
| Portland Trail Blazers   | **1610612757** |
| Sacramento Kings         | **1610612758** |
| San Antonio Spurs        | **1610612759** |
| Toronto Raptors          | **1610612761** |
| Utah Jazz                | **1610612762** |
| Washington Wizards       | **1610612764** |


**Key Features:**
1. **Recent Performance Metrics:** Investigated the significance of a team's performance in the most recent games (`home_last5`, `vlast`, `hlast`) as predictors for upcoming playoff games.
2. **Statistical Analysis:** Conducted exploratory data analysis (EDA) to understand the distributions, correlations, and potential predictors from the dataset.
3. **Feature Engineering:** Developed features based on the win-loss records from the past games to encapsulate a team's recent momentum.

**Machine Learning Workflow:**
1. **Data Preprocessing:** Handled missing values, outliers, and transformed data into a format suitable for machine learning.
2. **Model Selection:** Chose the Random Forest Classifier due to its ability to handle large datasets with higher dimensionality and its robustness against overfitting.
3. **Model Training & Testing:** Utilized 80% of the data for training and validated the model on the remaining 20%.
4. **Results:** Achieved an accuracy score of 54% on the test data, indicating a strong potential for the model to predict playoff game outcomes based on regular season performance metrics.

