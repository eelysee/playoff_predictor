# Comparision data in *nba_api* and *nba_apiv3* packages

## BoxScoreAdvancedV2 vs. BoxScoreAdvancedV3

### Player Stats

| BoxScoreAdvancedV3           | BoxScoreAdvancedV2 |
|------------------------------|--------------------|
| gameId                       | GAME_ID            |
| teamId                       | TEAM_ID            |
| teamCity                     | TEAM_CITY          |
| teamName                     |                    |
| teamTricode                  | TEAM_ABBREVIATION  |
| teamSlug                     |                    |
| personId                     | PLAYER_ID          |
| firstName                    |                    |
| familyName                   |                    |
| nameI                        | PLAYER_NAME        |
| playerSlug                   |                    |
| position                     | START_POSITION     |
| comment                      | COMMENT            |
| jerseyNum                    |                    |
| minutes                      | MIN                |
| estimatedOffensiveRating     | E_OFF_RATING       |
| offensiveRating              | OFF_RATING         |
| estimatedDefensiveRating     | E_DEF_RATING       |
| defensiveRating              | DEF_RATING         |
| estimatedNetRating           | E_NET_RATING       |
| netRating                    | NET_RATING         |
| assistPercentage             | AST_PCT            |
| assistToTurnover             | AST_TOV            |
| assistRatio                  | AST_RATIO          |
| offensiveReboundPercentage   | OREB_PCT           |
| defensiveReboundPercentage   | DREB_PCT           |
| reboundPercentage            | REB_PCT            |
| turnoverRatio                | TM_TOV_PCT         |
| effectiveFieldGoalPercentage | EFG_PCT            |
| trueShootingPercentage       | TS_PCT             |
| usagePercentage              | USG_PCT            |
| estimatedUsagePercentage     | E_USG_PCT          |
| estimatedPace                | E_PACE             |
| pace                         | PACE               |
| pacePer40                    | PACE_PER40         |
| possessions                  | POSS               |
| PIE                          | PIE                |

### Team Stats

| BoxScoreAdvancedV3              | BoxScoreAdvancedV2 |
|---------------------------------|--------------------|
| gameId                          | GAME_ID            |
| teamId                          | TEAM_ID            |
| teamCity                        | TEAM_CITY          |
| teamName                        | TEAM_NAME          |
| teamTricode                     | TEAM_ABBREVIATION  |
| teamSlug                        |                    |
| minutes                         | MIN                |
| estimatedOffensiveRating        | E_OFF_RATING       |
| offensiveRating                 | OFF_RATING         |
| estimatedDefensiveRating        | E_DEF_RATING       |
| defensiveRating                 | DEF_RATING         |
| estimatedNetRating              | E_NET_RATING       |
| netRating                       | NET_RATING         |
| assistPercentage                | AST_PCT            |
| assistToTurnover                | AST_TOV            |
| assistRatio                     | AST_RATIO          |
| offensiveReboundPercentage      | OREB_PCT           |
| defensiveReboundPercentage      | DREB_PCT           |
| reboundPercentage               | REB_PCT            |
| estimatedTeamTurnoverPercentage | E_TM_TOV_PCT       |
| turnoverRatio                   | TM_TOV_PCT         |
| effectiveFieldGoalPercentage    | EFG_PCT            |
| trueShootingPercentage          | TS_PCT             |
| usagePercentage                 | USG_PCT            |
| estimatedUsagePercentage        | E_USG_PCT          |
| estimatedPace                   | E_PACE             |
| pace                            | PACE               |
| pacePer40                       | PACE_PER40         |
| possessions                     | POSS               |
| PIE                             | PIE                |


## BoxScoreFourFactorsV2 vs. BoxScoreFourFactorsV3

### Player Stats

| BoxScoreFourFactorsV3           | BoxScoreFourFactorsV2 |
|---------------------------------|-----------------------|
| gameId                          | GAME_ID               |
| teamId                          | TEAM_ID               |
| teamCity                        | TEAM_CITY             |
| teamName                        |                       |
| teamTricode                     | TEAM_ABBREVIATION     |
| teamSlug                        |                       |
| personId                        | PLAYER_ID             |
| firstName                       |                       |
| familyName                      |                       |
| nameI                           | PLAYER_NAME           |
| playerSlug                      |                       |
| position                        | START_POSITION        |
| comment                         | COMMENT               |
| jerseyNum                       |                       |
| minutes                         | MIN                   |
| effectiveFieldGoalPercentage    | EFG_PCT               |
| freeThrowAttemptRate            | FTA_RATE              |
| teamTurnoverPercentage          | TM_TOV_PCT            |
| offensiveReboundPercentage      | OREB_PCT              |
| oppEffectiveFieldGoalPercentage | OPP_EFG_PCT           |
| oppFreeThrowAttemptRate         | OPP_FTA_RATE          |
| oppTeamTurnoverPercentage       | OPP_TOV_PCT           |
| oppOffensiveReboundPercentage   | OPP_OREB_PCT          |

### Team Stats
| BoxScoreFourFactorsV3           | BoxScoreFourFactorsV2 |
|---------------------------------|-----------------------|
| gameId                          | GAME_ID               |
| teamId                          | TEAM_ID               |
| teamCity                        | TEAM_CITY             |
| teamName                        | TEAM_NAME             |
| teamTricode                     | TEAM_ABBREVIATION     |
| teamSlug                        |                       |
| minutes                         | MIN                   |
| effectiveFieldGoalPercentage    | EFG_PCT               |
| freeThrowAttemptRate            | FTA_RATE              |
| teamTurnoverPercentage          | TM_TOV_PCT            |
| offensiveReboundPercentage      | OREB_PCT              |
| oppEffectiveFieldGoalPercentage | OPP_EFG_PCT           |
| oppFreeThrowAttemptRate         | OPP_FTA_RATE          |
| oppTeamTurnoverPercentage       | OPP_TOV_PCT           |
| oppOffensiveReboundPercentage   | OPP_OREB_PCT          |


## BoxScoreMiscV2 vs. BoxScoreMiscV3

### Player Stats

| BoxScoreMiscV3        | BoxScoreMiscV2     |
|-----------------------|--------------------|
| gameId                | GAME_ID            |
| teamId                | TEAM_ID            |
| teamCity              | TEAM_CITY          |
| teamName              |                    |
| teamTricode           | TEAM_ABBREVIATION  |
| teamSlug              |                    |
| personId              | PLAYER_ID          |
| firstName             |                    |
| familyName            |                    |
| nameI                 | PLAYER_NAME        |
| playerSlug            |                    |
| position              | START_POSITION     |
| comment               | COMMENT            |
| jerseyNum             |                    |
| minutes               | MIN                |
| pointsOffTurnovers    | PTS_OFF_TOV        |
| pointsSecondChance    | PTS_2ND_CHANCE     |
| pointsFastBreak       | PTS_FB             |
| pointsPaint           | PTS_PAINT          |
| oppPointsOffTurnovers | OPP_PTS_OFF_TOV    |
| oppPointsSecondChance | OPP_PTS_2ND_CHANCE |
| oppPointsFastBreak    | OPP_PTS_FB         |
| oppPointsPaint        | OPP_PTS_PAINT      |
| blocks                | BLK                |
| blocksAgainst         | BLKA               |
| foulsPersonal         | PF                 |
| foulsDrawn            | PFD                |

### Team Stats

| BoxScoreMiscV3        | BoxScoreMiscV2     |
|-----------------------|--------------------|
| gameId                | GAME_ID            |
| teamId                | TEAM_ID            |
| teamCity              | TEAM_CITY          |
| teamName              | TEAM_NAME          |
| teamTricode           | TEAM_ABBREVIATION  |
| teamSlug              |                    |
| minutes               | MIN                |
| pointsOffTurnovers    | PTS_OFF_TOV        |
| pointsSecondChance    | PTS_2ND_CHANCE     |
| pointsFastBreak       | PTS_FB             |
| pointsPaint           | PTS_PAINT          |
| oppPointsOffTurnovers | OPP_PTS_OFF_TOV    |
| oppPointsSecondChance | OPP_PTS_2ND_CHANCE |
| oppPointsFastBreak    | OPP_PTS_FB         |
| oppPointsPaint        | OPP_PTS_PAINT      |
| blocks                | BLK                |
| blocksAgainst         | BLKA               |
| foulsPersonal         | PF                 |
| foulsDrawn            | PFD                |
