import pandas as pd

nom_a_abrev_old = {'Atlanta Hawks': 'ATL',
                    'Boston Celtics': 'BOS',
                   'Brooklyn Nets': 'BRK',
                   'Charlotte Bobcats': 'CHA',
                   'Charlotte Hornets': 'CHO',
                   'Chicago Bulls': 'CHI',
                   'Cleveland Cavaliers': 'CLE',
                   'Dallas Mavericks': 'DAL',
                   'Denver Nuggets': 'DEN',
                   'Detroit Pistons': 'DET',
                   'Golden State Warriors': 'GSW',
                   'Houston Rockets': 'HOU',
                   'Indiana Pacers': 'IND',
                   'Los Angeles Clippers': 'LAC',
                   'Los Angeles Lakers': 'LAL',
                   'Memphis Grizzlies': 'MEM',
                   'Miami Heat': 'MIA',
                   'Milwaukee Bucks': 'MIL',
                   'Minnesota Timberwolves': 'MIN',
                   'New Jersey Nets': 'NJN',
                   'New Orleans Hornets': 'NOH',
                   'New Orleans Pelicans': 'NOP',
                   'New York Knicks': 'NYK',
                   'Oklahoma City Thunder': 'OKC',
                   'Orlando Magic': 'ORL',
                   'Philadelphia 76ers': 'PHI',
                   'Phoenix Suns': 'PHO',
                   'Portland Trail Blazers': 'POR',
                   'Sacramento Kings': 'SAC',
                   'San Antonio Spurs': 'SAS',
                   'Seattle Supersonics': 'SEA',
                   'Toronto Raptors': 'TOR',
                   'Utah Jazz': 'UTA',
                   'Washington Bullets': 'WAS',
                   'Washington Wizards': 'WAS'}

nom_a_abrev = {'Atlanta Hawks': 'ATL',
               'Boston Celtics': 'BOS',
               'Brooklyn Nets': 'BRK',
               'Charlotte Hornets': 'CHO',
               'Chicago Bulls': 'CHI',
               'Cleveland Cavaliers': 'CLE',
               'Dallas Mavericks': 'DAL',
               'Denver Nuggets': 'DEN',
               'Detroit Pistons': 'DET',
               'Golden State Warriors': 'GSW',
               'Houston Rockets': 'HOU',
               'Indiana Pacers': 'IND',
               'Los Angeles Clippers': 'LAC',
               'Los Angeles Lakers': 'LAL',
               'Memphis Grizzlies': 'MEM',
               'Miami Heat': 'MIA',
               'Milwaukee Bucks': 'MIL',
               'Minnesota Timberwolves': 'MIN',
               'New Orleans Pelicans': 'NOP',
               'New York Knicks': 'NYK',
               'Oklahoma City Thunder': 'OKC',
               'Orlando Magic': 'ORL',
               'Philadelphia 76ers': 'PHI',
               'Phoenix Suns': 'PHO',
               'Portland Trail Blazers': 'POR',
               'Sacramento Kings': 'SAC',
               'San Antonio Spurs': 'SAS',
               'Toronto Raptors': 'TOR',
               'Utah Jazz': 'UTA',
               'Washington Wizards': 'WAS'}

#deja_fait = ['Atlanta Hawks', 'Boston Celtics','Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks','Denver Nuggets','Detroit Pistons'
             #,'Golden State Warriors','Houston Rockets','Indiana Pacers', 'Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies','Miami Heat','Milwaukee Bucks','Minnesota Timberwolves'
             #,'New Orleans Pelicans','New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers','Phoenix Suns','Portland Trail Blazers']

deja_fait = []

dico_dates = {
    '2019': ('2018-10-16', '2019-04-10'),
    '2018': ('2017-10-17', '2018-04-11'),
    '2017': ('2016-10-25', '2017-04-12'),
    '2016': ('2015-10-27', '2016-04-13'),
    '2015': ('2014-10-28', '2015-04-15'),
    '2014': ('2013-10-29', '2014-04-16'),
    '2013': ('2012-10-30', '2013-04-17'),
    '2012': ('2011-12-25', '2012-04-26'),
    '2011': ('2010-10-26', '2011-04-13'),
    '2010': ('2009-10-27', '2010-04-14')
}

dico_box_2019 = {}
for equipe in list(nom_a_abrev):
    dico_box_2019[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Recup_Raw/' + nom_a_abrev[equipe] + '2019.csv'))

del dico_box_2019['LAC']['Unnamed: 0.1']
del dico_box_2019['MIN']['Unnamed: 0.1']
del dico_box_2019['MIL']['Unnamed: 0.1']

dico_box_2018 = {}
for equipe in list(nom_a_abrev):
    dico_box_2018[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Recup_Raw/' + nom_a_abrev[equipe] + '2018.csv'))

dico_box_2017 = {}
for equipe in list(nom_a_abrev):
    dico_box_2017[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Recup_Raw/' + nom_a_abrev[equipe] + '2017.csv'))

dico_box = {'2019': dico_box_2019,
            '2018': dico_box_2018,
            '2017': dico_box_2017}

# Importer les rosters :

dico_roster_2020 = {}

dico_roster_2019 = {}
for equipe in list(nom_a_abrev):
    dico_roster_2019[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Rosters/Roster_' + nom_a_abrev[equipe] + '2019.csv'))

dico_roster_2018 = {}
for equipe in list(nom_a_abrev):
    dico_roster_2018[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Rosters/Roster_' + nom_a_abrev[equipe] + '2018.csv'))

dico_roster_2017 = {}
for equipe in list(nom_a_abrev):
    dico_roster_2017[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Rosters/Roster_' + nom_a_abrev[equipe] + '2017.csv'))

dico_roster = {'2019': dico_roster_2019,
               '2018': dico_roster_2018,
               '2017': dico_roster_2017}

# Importer les schedules :

dico_schedule = {'2019': pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Schedules/Schedule2019.csv')),
                 '2018': pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Schedules/Schedule2018.csv')),
                 '2017': pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Schedules/Schedule2017.csv'))}

dico_inputs_train = {'2019' : pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Inputs/dataset_train2019.csv')),
                     '2018' : pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Inputs/dataset_train2018.csv')),
                     '2017' : pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Inputs/dataset_train2017.csv'))}

dico_inputs_test = {'2019' : pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Inputs/dataset_test2019.csv'))}


dataset_train = pd.concat([dico_inputs_train['2019'],dico_inputs_train['2018'],dico_inputs_train['2017']])
del dataset_train['Unnamed: 0']
dataset_train = dataset_train.loc[dataset_train['MP'] >= 600 ]

dataset_test = dico_inputs_test['2019']
del dataset_test['Unnamed: 0']