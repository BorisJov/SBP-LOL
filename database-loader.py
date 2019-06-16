import csv
import pymongo
import pdb
import pprint
import ast

match_dict = dict()

with open('matchinfo.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            matchinfo = dict()
            matchinfo['address'] = row['Address']
            matchinfo['league'] = row['League']
            matchinfo['year'] = row['Year']
            matchinfo['season'] = row['Season']

            matchinfo['blueResult'] = row['bResult']
            matchinfo['redResult'] = row['rResult']
            matchinfo['gamelength'] = row['gamelength']

            blue_team = dict()
            red_team = dict()
            blue_team['blueTeamTag'] = row['blueTeamTag']
            blue_team['topPlayer'] = row['blueTop']
            blue_team['topChampion'] = row['blueTopChamp']
            blue_team['jgPlayer'] = row['blueJungle']
            blue_team['jgChampion'] = row['blueJungleChamp']
            blue_team['midPlayer'] = row['blueMiddle']
            blue_team['midChampion'] = row['blueMiddleChamp']
            blue_team['adcPlayer'] = row['blueADC']
            blue_team['adcChampion'] = row['blueADCChamp']
            blue_team['supPlayer'] = row['blueSupport']
            blue_team['supChampion'] = row['blueSupportChamp']

            red_team['redTeamTag'] = row['redTeamTag']
            red_team['topPlayer'] = row['redTop']
            red_team['topChampion'] = row['redTopChamp']
            red_team['jgPlayer'] = row['redJungle']
            red_team['jgChampion'] = row['redJungleChamp']
            red_team['midPlayer'] = row['redMiddle']
            red_team['midChampion'] = row['redMiddleChamp']
            red_team['adcPlayer'] = row['redADC']
            red_team['adcChampion'] = row['redADCChamp']
            red_team['supPlayer'] = row['redSupport']
            red_team['supChampion'] = row['redSupportChamp']

            matchinfo['blueTeam'] = blue_team
            matchinfo['redTeam'] = red_team

            # pdb.set_trace()
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(matchinfo)
            match_dict[matchinfo['address']] = matchinfo
    print(f'Matchinfo: Processed {line_count} lines.')

with open('bans.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1

            address = row['Address']
            if address in match_dict:
                match = match_dict[address]
                bans = []
                for i in range(1, 6):
                    if row['ban_' + str(i)] != '':
                        bans.append(row['ban_' + str(i)])

                if row['Team'] == 'blueBans':
                    match['blueBans'] = bans
                else:
                    match['redBans'] = bans
    print(f'Bans: Processed {line_count} lines.')

with open('kills.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1

            address = row['Address']
            if address in match_dict:
                match = match_dict[address]
                
                kills = []
                if 'kills' in match:
                    kills = match['kills']
                
                kill = dict()
                kill['side'] = 'blue' if row['Team'] == 'bKills' else 'red'
                kill['victim'] = row['Victim']
                kill['killer'] = row['Killer']
                kill['time'] = row['Time']

                kills.append(kill)
                match['kills'] = kills
    print(f'Kills: Processed {line_count} lines.')

with open('structures.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1

            address = row['Address']
            if address in match_dict:
                match = match_dict[address]

                structures = []
                if 'structures' in match:
                    structures = match['structures']
                
                structure = dict()
                structure['side'] = 'blue' if row['Team'][0] == 'b' else 'red'
                structure['time'] = row['Time']
                structure['lane'] = row['Lane']
                structure['type'] = row['Type']

                structures.append(structure)
                match['structures'] = structures
    print(f'Structures: Processed {line_count} lines.')

with open('monsters.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1

            address = row['Address']
            if address in match_dict:
                match = match_dict[address]

                neutral_objectives = dict()
                if 'neutral_objectives' in match:
                    neutral_objectives = match['neutral_objectives']
                else:
                    neutral_objectives['dragons'] = []
                    neutral_objectives['heralds'] = []
                    neutral_objectives['barons'] = []
                
                where = []
                if row['Type'].endswith('DRAGON'):
                    where = neutral_objectives['dragons']
                elif row['Type'] == 'RIFT_HERALD':
                    where = neutral_objectives['heralds']
                elif row['Type'] == 'BARON_NASHOR':
                    where = neutral_objectives['barons']
                else:
                    print(row['Type'])
                
                slay = dict()
                slay['side'] = 'blue' if row['Team'][0] == 'b' else 'red'
                slay['time'] = row['Time']
                where.append(slay)

                match['neutral_objectives'] = neutral_objectives
    print(f'Monsters: Processed {line_count} lines.')

with open('LeagueofLegends.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1

            address = row['Address']
            if address in match_dict:
                match = match_dict[address]

                gold = dict()
                
                gold['difference'] = ast.literal_eval(row['golddiff'])
                gold['blueTeam'] = ast.literal_eval(row['goldblue'])
                gold['redTeam'] = ast.literal_eval(row['goldred'])
                gold['blueTop'] = ast.literal_eval(row['goldblueTop'])
                gold['redTop'] = ast.literal_eval(row['goldredTop'])
                gold['blueJG'] = ast.literal_eval(row['goldblueJungle'])
                gold['redJG'] = ast.literal_eval(row['goldredJungle'])
                gold['blueMid'] = ast.literal_eval(row['goldblueMiddle'])
                gold['redMid'] = ast.literal_eval(row['goldredMiddle'])
                gold['blueADC'] = ast.literal_eval(row['goldblueADC'])
                gold['redADC'] = ast.literal_eval(row['goldredADC'])
                gold['blueSup'] = ast.literal_eval(row['goldblueSupport'])
                gold['redSup'] = ast.literal_eval(row['goldredSupport'])

                match['gold'] = gold
    print(f'Gold: Processed {line_count} lines.')


pdb.set_trace()
client = pymongo.MongoClient('localhost', 27017)
db = client['LeagueOfLegends_TEST']
collection = db['everything']
result = collection.insert_many(match_dict.values())
