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

dico_box_2017 = {}

dico_box = {'2019': dico_box_2019,
            '2018': dico_box_2018,
            '2017': dico_box_2017}

# Importer les rosters :

dico_roster_2019 = {}
for equipe in list(nom_a_abrev):
    dico_roster_2019[nom_a_abrev[equipe]] = pd.read_csv(
        open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Rosters/Roster_' + nom_a_abrev[equipe] + '2019.csv'))

dico_roster_2018 = {}

dico_roster_2017 = {}

dico_roster = {'2019': dico_roster_2019,
               '2018': dico_roster_2018,
               '2017': dico_roster_2017}

# Importer les schedules :

dico_schedule = {'2019': pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Schedules/Schedule2019.csv'))}

dico_inputs_train = {'2019' : (pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Inputs/X2019.csv')), pd.read_csv(open('/Users/thomaslouis/Documents/Documents/Projet/TTFL/Inputs/Y2019.csv')))}

deja_fait = []
