import requests
import lxml.html as lh
import pandas as pd
import numpy


'''
__________
IMPORTANT 
__________
TODO 
To update the draft every new year, input the playoff teams and the new stats url into the getStats function. 
Then, delete all the current player objects and run the code in players.py to input the new players into the draft. 
'''

def getStats(statName):
    teams = ['PHI', 'BKN', 'MIL', 'NYK', 'ATL', 'MIA', 'BOS', 'CHA', 'UTA', 'PHX', 'LAC', 'DEN', 'DAL', 'POR', 'LAL', 'GSW']
    url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)

    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    # file = open("sample.html","w")
    # file.write((lh.tostring(doc).decode('utf-8')))
    # file.close()

    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    # All per game stats
    # These columns go with the table at this link: https://www.basketball-reference.com/leagues/NBA_2020_per_game.html
    mapStatToColumnIndex = {
        "name": 1,
        "position": 2,
        "age": 3,
        "team": 4,
        "gamesPlayed": 5,
        "gamesStarted": 6,
        "minutesPlayed": 7,
        "fieldGoals": 8,
        "fieldGoalsAttempted": 9,
        "fieldGoalPercentage": 10,
        "threePointsMade": 11,
        "threePointsAttempted": 12,
        "threePointPercentage": 13,
        "twoPointsMade": 14,
        "twoPointsAttempted": 15,
        "twoPointPercentage": 16,
        "effectiveFieldGoalPercentage": 17,
        "freeThrowsMade": 18,
        "freeThrowsAttempted": 19,
        "freeThrowPercentage": 20,
        "offensiveRebounds": 21,
        "defensiveRebounds": 22,
        "totalRebounds": 23,
        "assists": 24,
        "steals": 25,
        "blocks": 26,
        "turnovers": 27,
        "fouls": 28,
        "points": 29
    }

    dataSet = []

    for T in tr_elements[1:]:
        validRow = True
        row = []
        for i, t in enumerate(T.iterchildren()):
            if(str(t.text_content())=='Rk'):
                validRow = False
                break
            elif(str(t.text_content())==''):
                row.append(0.0)
            else:
                if(i==1 or i==2 or i==4):
                    row.append(str(t.text_content()))
                else:
                    row.append(float(t.text_content()))
        if validRow:
            dataSet.append(row)

    def getColumn(col, data):
        column = [row[col] for row in data]
        return column

    d = {
        "name": getColumn(1, dataSet),
        "position": getColumn(2, dataSet),
        "age": getColumn(3, dataSet),
        "team": getColumn(4, dataSet),
        "gamesPlayed": getColumn(5, dataSet),
        "gamesStarted": getColumn(6, dataSet),
        "minutesPlayed": getColumn(7, dataSet),
        "fieldGoals": getColumn(8, dataSet),
        "fieldGoalsAttempted": getColumn(9, dataSet),
        "fieldGoalPercentage": getColumn(10, dataSet),
        "threePointsMade": getColumn(11, dataSet),
        "threePointsAttempted": getColumn(12, dataSet),
        "threePointPercentage": getColumn(13, dataSet),
        "twoPointsMade": getColumn(14, dataSet),
        "twoPointsAttempted": getColumn(15, dataSet),
        "twoPointPercentage": getColumn(16, dataSet),
        "effectiveFieldGoalPercentage": getColumn(17, dataSet),
        "freeThrowsMade": getColumn(18, dataSet),
        "freeThrowsAttempted": getColumn(19, dataSet),
        "freeThrowPercentage": getColumn(20, dataSet),
        "offensiveRebounds": getColumn(21, dataSet),
        "defensiveRebounds": getColumn(22, dataSet),
        "totalRebounds": getColumn(23, dataSet),
        "assists": getColumn(24, dataSet),
        "steals": getColumn(25, dataSet),
        "blocks": getColumn(26, dataSet),
        "turnovers": getColumn(27, dataSet),
        "fouls": getColumn(28, dataSet),
        "points": getColumn(29, dataSet)
    }

    df = pd.DataFrame(data=d)

    onlyPlayoffTeams = df[df['team'].isin(teams)]

    onlyPlayoffTeams = onlyPlayoffTeams.reset_index(drop=True)

    croppedTotalData = onlyPlayoffTeams[['name', 'position', 'age', 'team', 'gamesPlayed', 'gamesStarted', 'minutesPlayed', 'points',
    'freeThrowsMade', 'threePointsMade', 'totalRebounds', 'blocks', 'assists', 'fouls']]

    croppedTotalData = croppedTotalData.sort_values(by=statName, ascending = False).reset_index(drop=True)
    # croppedTotalData.to_csv('tableData.csv')
    return croppedTotalData


def getPlayer(stat):
    top25 = getStats(stat)[['name','team', stat]]
    print(top25)
    print(len(top25))
    unwrapped_df = list(zip(*top25.values.tolist()))
    names, teams, _ = unwrapped_df
    players = dict(zip(names,teams))
    return players