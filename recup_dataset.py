# equipe = Nom Complet
# Annee = Année de fin de saison
# -> ['DATE', 'VISITOR', 'VISITOR_PTS', 'HOME', 'HOME_PTS'] de l'équipe demandée, dans l'année demandée indexé de 0 à 81
from dicos_utiles import dico_schedule


def recup_matchs(equipe, annee):
    planning = dico_schedule[annee]
    planning_equipe = planning.loc[(planning['VISITOR'] == equipe) | (planning['HOME'] == equipe), :].reset_index(
        drop=True)
    return planning_equipe


# equipe = nom complet
# annee = annee de fin de saison
# -> ['PLAYER', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', '+/-', DATE,
#  EQ/OPP,	TS%,	eFG%,	3PAr,	FTr,	ORB%,	DRB%,	TRB%,	AST%,	STL%,	BLK%,	TOV%,	USG%,	ORtg,	DRtg,	BPM]
# pour tous les matchs
# Se suivent : les données de chaque matchs avec le box score des deux équipes (équipe demandée / équipe opposée)
# EQ/OPP : 0 si equipe demandée 1 si equipe opposée.
#


def recup_box_scores(equipe, annee):
    planning_equipe = recup_matchs(equipe, annee)
    abr_equipe = nom_a_abrev[equipe]
    for i in range(82):
        date = planning_equipe['DATE'][i]
        if equipe == planning_equipe['VISITOR'][i]:  # définit l'abréviation de l'équipe opposée
            abr_equipe_opp = nom_a_abrev[planning_equipe['HOME'][i]]
        else:
            abr_equipe_opp = nom_a_abrev[planning_equipe['VISITOR'][i]]
        box_score_base = get_box_scores(date, abr_equipe, abr_equipe_opp, period='GAME', stat_type='BASIC')
        box_score_equipe_base = box_score_base[abr_equipe]
        box_score_equipe_opp_base = box_score_base[abr_equipe_opp]
        box_score_adv = get_box_scores(date, abr_equipe, abr_equipe_opp, period='GAME', stat_type='ADVANCED')
        box_score_equipe_adv = box_score_adv[abr_equipe]
        box_score_equipe_opp_adv = box_score_adv[abr_equipe_opp]
        del box_score_equipe_adv['MP']  # MP se retrouve dans les deux tableaux basic et adv. On l'enlève.
        del box_score_equipe_opp_adv['MP']
        box_score_equipe_base['DATE'] = date
        box_score_equipe_opp_base['DATE'] = date
        box_score_equipe_base['EQ/OPP'] = 0
        box_score_equipe_opp_base['EQ/OPP'] = 1
        box_score_equipe = pd.merge(box_score_equipe_base, box_score_equipe_adv, on='PLAYER')  # On merge basic et adv
        box_score_equipe_opp = pd.merge(box_score_equipe_opp_base, box_score_equipe_opp_adv, on='PLAYER')
        box_score = pd.concat(
            [box_score_equipe, box_score_equipe_opp])  # on concatène équipe demandee et equipe opposante
        if i == 0:
            box_score_total_equipe = box_score
        else:
            box_score_total_equipe = pd.concat(
                [box_score_total_equipe, box_score])  # On concatene le nouveau matche i avec les anciens
        if i % 10 == 0:
            print(i)
    return box_score_total_equipe


# Il y avait un bug dans le dataset des LAC :

def corriger_LAC_2019():
    LAC = dico_box_2019['LAC']
    sean = []
    reed = []
    for i in range(2269):
        if LAC['PLAYER'][i] == 'Sean Kilpatrick':
            sean.append(i)
        if LAC['PLAYER'][i] == 'Willie Reed':
            reed.append(i)
    for i in sean:
        LAC['PLAYER'][i] = 'Shai Gilgeous-Alexander'
    for i in reed:
        LAC = LAC.drop([i])
    del LAC['Unnamed: 0.1']
    LAC.to_csv('LAC2019.csv')
    return LAC


def corriger_MIL_2019():
    MIL = dico_box_2019['MIL']
    jason = []
    for i in range(2259):
        if MIL['PLAYER'][i] == 'Jason Terry':
            jason.append(i)
    for i in jason:
        MIL = MIL.drop([i])
    del MIL[['Unnamed: 0.1']]
    MIL.to_csv('MIL2019.csv')
    return MIL


def corriger_MIN_2019():
    MIN = dico_box_2019['MIN']
    cole = []
    brook = []
    for i in range(2259):
        if MIN['PLAYER'][i] == 'Cole Aldrich':
            cole.append(i)
        if MIN['PLAYER'][i] == 'Aaron Brooks':
            brook.append(i)
    for i in cole:
        MIN['PLAYER'][i] = 'C.J. Williams'
    for i in brook:
        MIN = MIN.drop([i])
    del MIN['Unnamed: 0.1']
    MIN.to_csv('MIN2019.csv')
    return MIN, brook


# -> ['PLAYER', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', '+/-', DATE,
#  EQ/OPP,	TS%,	eFG%,	3PAr,	FTr,	ORB%,	DRB%,	TRB%,	AST%,	STL%,	BLK%,	TOV%,	USG%,	ORtg,	DRtg,	BPM]
# de tous les matchs de chaque équipe + equipe_opp dans l'année donnée.

def recup_tout_box(annee):
    for equipe in list(nom_a_abrev):
        if not equipe in deja_fait:
            box_score_total_equipe = recup_box_scores(equipe, annee)
            box_score_total_equipe.to_csv(nom_a_abrev[equipe] + annee + '.csv')


# Tous les rosters de l'année

def recup_tout_roster(annee):
    for equipe in list(nom_a_abrev):
        roster = get_roster(nom_a_abrev[equipe], annee)
        roster.to_csv('Roster_' + nom_a_abrev[equipe] + annee + '.csv')
        print(equipe)


def recup_schedule(annee):
    schedule = get_schedule(annee)
    schedule.to_csv('Schedule' + annee + '.csv')
