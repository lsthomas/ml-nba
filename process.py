"""# Process Data box_scores

## Process general
"""

import datetime as dt
import numpy as np

from dicos_utiles import dico_dates, nom_a_abrev, dico_roster, dico_box, dico_box_2019, deja_fait
import pandas as pd

from recup_dataset import recup_matchs


def date_to_saison(date):
    for saison in list(dico_dates):
        date_debut, date_fin = dico_dates[saison]
        if date_debut <= date and date <= date_fin:
            return saison


# Entrée : box_score_total comme renvoyé par recup_box_scores
# Sortie : le même sans les totaux d'équipes et les box des equipes adv.

def enlever_totals(box_score_total):
    return box_score_total.loc[(box_score_total['PLAYER'] != 'Team Totals') & (box_score_total['EQ/OPP'] == 0)]


# Entrée : box_score_total comme renvoyé par recup_box_scores
# Sortie : le même avec que les totaux d'équipes

def enlever_joueurs(box_score_total):
    return box_score_total.loc[box_score_total['PLAYER'] == 'Team Totals']


# Enlève les DNP etc...

def clean_DNP(box_score_total):
    return box_score_total.loc[
        (box_score_total['MP'] != 'Did Not Play') & (box_score_total['MP'] != 'Did Not Dress') & (
                    box_score_total['MP'] != 'Not With Team') & (box_score_total['AST%'] != 'Did Not Play') & (
                    box_score_total['AST%'] != 'Did Not Dress')]


# Transforme les Minutes played en secondes

def changer_MP(box_score_total_equipe):
    box_score_total_equipe['MP'] = pd.to_datetime(box_score_total_equipe['MP'], format='%M:%S')
    box_score_total_equipe['MP'] = box_score_total_equipe['MP'].dt.minute * 60 + box_score_total_equipe['MP'].dt.second
    return box_score_total_equipe


# Entrée : box_score_total_equipe renvoyé par box
# Sortie : box_score_total du joueur, avec les colonnes :
# Unnamed: 0	PLAYER	MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-	DATE	EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM

def box_score_joueur_propre(joueur, box_score_total):
    box_score_total_propre = changer_MP(clean_DNP(enlever_totals(box_score_total)))
    return box_score_total_propre.loc[box_score_total_propre['PLAYER'] == joueur]


# Entrée : box_score_total_equipe renvoyé par recup_box_scores
# Sortie : box_score_total des totaux de l'equipe, avec les colonnes :
# Unnamed: 0	PLAYER	MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-	DATE	EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM

def box_score_totaux_equipe_propre(box_score_total):
    box_score_total_propre = enlever_joueurs(box_score_total)
    box_score_total_propre = box_score_total_propre.loc[box_score_total_propre['EQ/OPP'] == 0]
    del box_score_total_propre['PLAYER']
    del box_score_total_propre['MP']
    del box_score_total_propre['+/-']
    del box_score_total_propre['EQ/OPP']
    del box_score_total_propre['BPM']
    del box_score_total_propre['USG%']
    del box_score_total_propre['Unnamed: 0']
    return box_score_total_propre


# Entrée : box_score_total_equipe renvoyé par recup_box_scores
# Sortie : box_score_total des totaux de l'equipe opposée, avec les colonnes :
# Unnamed: 0	PLAYER	MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-	DATE	EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM

def box_score_totaux_equipe_opp_propre(box_score_total):
    box_score_total_propre = enlever_joueurs(box_score_total)
    box_score_total_propre = box_score_total_propre.loc[box_score_total_propre['EQ/OPP'] == 1]
    del box_score_total_propre['PLAYER']
    del box_score_total_propre['MP']
    del box_score_total_propre['+/-']
    del box_score_total_propre['EQ/OPP']
    del box_score_total_propre['BPM']
    del box_score_total_propre['USG%']
    del box_score_total_propre['Unnamed: 0']
    return box_score_total_propre


"""## Input Joueur"""


# Entrée : joueur, saison :
# Sortie : Liste des équipes dans lesquelles le joueur a joué dans la saison. (Abréviation)
#

def liste_equipe_joueur(joueur, saison):
    resu = []
    for equipe in list(nom_a_abrev):
        roster = dico_roster[saison][nom_a_abrev[equipe]]
        if not (roster is None):
            if (joueur in roster['PLAYER'].values):
                resu.append(nom_a_abrev[equipe])
    return resu


# Entrée : joueur, saison
# Sortie : Tous les box scores des équipes dans lesquelles le joueur a joué (au format cleaned comme test_box_nets)

# Entrée : box_score_saison_joueur : df cleaned comme renvoyé par box_score_joueur_propre.
# Avec colonnes = Unnamed: 0	PLAYER	MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-	DATE	EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM
# Sortie : moyenne entre date de début et date de fin.
# Avec colonnes = MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-		EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM

def moyennes(date_debut, date_fin, box_score_saison_joueur):
    box_entre_dates = box_score_saison_joueur.loc[
        (box_score_saison_joueur['DATE'] <= date_fin) & (box_score_saison_joueur['DATE'] >= date_debut)]
    del box_entre_dates['PLAYER']
    del box_entre_dates['Unnamed: 0']
    del box_entre_dates['DATE']
    del box_entre_dates['FT%']  # Del les % qui n'ont aucun sens dans une moyenne
    del box_entre_dates['3P%']
    del box_entre_dates['FG%']
    box = box_entre_dates.astype(float)
    box['TTFL'] = box['PTS'] + box['TRB'] + box['AST'] + box['STL'] + box['BLK'] + 2 * (
                box['FG'] + box['3P'] + box['FT']) - (box['TOV'] + box['FGA'] + box['3PA'] + box['FTA'])
    return box.mean()


# Entrée : box_score_saison : df cleaned de recup_box_score, comme test_box_nets avec que les infos du joueur (par ex : test_box_nets['PLAYER' = 'Joe Harris']) sur une saison
# Besoin d'au moins x matchs pour rendre un résultat
# Avec colonnes = Unnamed: 0	PLAYER	MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-	DATE	EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM
# Sortie : moyenne dans les x derniers matchs. Si pas fait x matchs, renvoie None.
# Avec colonnes = MP	FG	FGA	3P	3PA	FT	FTA	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-		EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM

def moyennes_sur_x_derniers_matchs(x, date, box_score_saison_joueur, annee):
    date_debut_saison, date_fin_saison = dico_dates[annee]
    box_score_saison_avant_date = box_score_saison_joueur.loc[box_score_saison_joueur['DATE'] <= date]
    if box_score_saison_avant_date is None:  # Pas encore de matchs joués
        return pd.Series()
    if box_score_saison_avant_date.shape[0] < x:
        return moyennes(date_debut_saison, date, box_score_saison_joueur)
    else:
        date_match_moins_x = box_score_saison_avant_date['DATE'].iloc[-x]
        return moyennes(date_match_moins_x, date, box_score_saison_joueur)


def nombre_jours_repos(joueur, equipe, date):
    saison_date = date_to_saison(date)
    box_score = box_score_joueur_propre(joueur, dico_box[saison_date][equipe])
    box_score = box_score.loc[box_score['DATE'] < date]
    if box_score.empty:
        return 0
    return (dt.datetime.strptime(date, '%Y-%m-%d') - dt.datetime.strptime(box_score['DATE'].iloc[-1],
                                                                          '%Y-%m-%d')).total_seconds()


nombre_jours_repos('Joe Harris', 'BRK', '2018-11-05')


# Entrée : joueur,date
# Sortie : input du joueur au la date date. Contient un tableau de 99 lignes avec les stats habituelles de moyennes sur:
# Toute la saison,5 Matchs,

def input_joueur(joueur, date):
    saison_date = date_to_saison(date)
    liste_equipe = liste_equipe_joueur(joueur, saison_date)
    box_score_saison_joueur = pd.DataFrame()
    for equipe in liste_equipe:
        box_score_saison_joueur = pd.concat(
            [box_score_joueur_propre(joueur, dico_box[saison_date][equipe]), box_score_saison_joueur])
    # moyenne_3 = moyennes_sur_x_derniers_matchs(3,date,box_score_saison_joueur,saison_date)
    moyenne_5 = moyennes_sur_x_derniers_matchs(5, date, box_score_saison_joueur, saison_date)
    moyenne_saison = moyennes_sur_x_derniers_matchs(82, date, box_score_saison_joueur, saison_date)
    # X = pd.concat([moyenne_3,moyenne_5])
    # X = pd.concat([X,moyenne_saison])
    X = pd.concat([moyenne_saison, moyenne_5])
    return X


"""## Input Equipe """


# Entrée : equipe (abréviation), dates, box_score_equipe comme renvoyé par box_score_totaux_equipe_propre
# Sortie : moyennes entre date_debut et date_fin

def moyennes_equipe(date_debut, date_fin, box_score_equipe):
    box_entre_dates = box_entre_dates = box_score_equipe.loc[
        (box_score_equipe['DATE'] <= date_fin) & (box_score_equipe['DATE'] >= date_debut)]
    del box_entre_dates['DATE']
    del box_entre_dates['FT%']  # Del les % qui n'ont aucun sens dans une moyenne
    del box_entre_dates['3P%']
    del box_entre_dates['FG%']
    box_entre_dates = box_entre_dates.astype(float)
    return box_entre_dates.mean()


moyennes_equipe('2019-01-01', '2020-01-01', box_score_totaux_equipe_propre(dico_box_2019['BRK']))


# Entrée : box_score_saison : df cleaned de recup_box_score, comme test_box_nets avec que les infos du joueur (par ex : test_box_nets['PLAYER' = 'Joe Harris']) sur une saison
# Besoin d'au moins x matchs pour rendre un résultat
# Avec colonnes = Unnamed: 0	PLAYER	MP	FG	FGA	FG%	3P	3PA	3P%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-	DATE	EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM
# Sortie : moyenne dans les x derniers matchs. Si pas fait x matchs, renvoie None.
# Avec colonnes = MP	FG	FGA	3P	3PA	FT	FTA	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS	+/-		EQ/OPP	TS%	eFG%	3PAr	FTr	ORB%	DRB%	TRB%	AST%	STL%	BLK%	TOV%	USG%	ORtg	DRtg	BPM


def moyennes_sur_x_derniers_matchs_equipe(x, date, box_score_equipe, annee):
    date_debut_saison, date_fin_saison = dico_dates[annee]
    box_score_saison_avant_date = box_score_equipe.loc[box_score_equipe['DATE'] <= date]
    if box_score_saison_avant_date is None:  # Pas encore de matchs joués
        return None
    if box_score_saison_avant_date.shape[0] < x:
        return moyennes_equipe(date_debut_saison, date, box_score_equipe)
    else:
        date_match_moins_x = box_score_saison_avant_date['DATE'].iloc[-x]
        return moyennes_equipe(date_match_moins_x, date, box_score_equipe)


dt.datetime.strptime('2020-01-01', '%Y-%m-%d')


def input_equipes(date, equipe, equipe_opp):
    saison_date = date_to_saison(date)
    box_score_equipe = box_score_totaux_equipe_propre(dico_box[saison_date][equipe])
    box_score_equipe_opp = box_score_totaux_equipe_propre(dico_box[saison_date][equipe_opp])
    moyenne_saison = moyennes_sur_x_derniers_matchs_equipe(82, date, box_score_equipe, saison_date)
    moyenne_saison_opp = moyennes_sur_x_derniers_matchs_equipe(82, date, box_score_equipe_opp, saison_date)
    X = pd.concat([moyenne_saison, moyenne_saison_opp])
    return X


"""## Input Total"""


# Input d'un joueur, à un moment donné.
# Renvoie un pandas

def input_total(joueur, date, equipe, equipe_opp):
    repos = pd.Series({'REP': nombre_jours_repos(joueur, equipe, date)})
    X_joueur = input_joueur(joueur, date)
    X_equipe = input_equipes(date, equipe, equipe_opp)
    X = pd.concat([X_joueur, X_equipe, repos])
    return X



def Y_total(joueur, date, equipe):
    saison_date = date_to_saison(date)
    box_score_tot = box_score_joueur_propre(joueur, dico_box[saison_date][equipe])
    box = box_score_tot.loc[box_score_tot['DATE'] == date]
    del box['PLAYER']
    del box['Unnamed: 0']
    del box['DATE']
    box = box.astype(float)
    resu = box['PTS'] + box['TRB'] + box['AST'] + box['STL'] + box['BLK'] + 2 * (box['FG'] + box['3P'] + box['FT']) - (
                box['TOV'] + box['FGA'] + box['3PA'] + box['FTA'])
    return resu


"""## Build X_train, Y_train"""


def build(date_debut_build):
    annee = date_to_saison(date_debut_build)
    X = pd.Dataframe()
    Y = pd.Dataframe()
    for equipe in list(nom_a_abrev):
        if not (equipe in deja_fait):
            print(equipe)
            schedule = recup_matchs(equipe, annee)
            box_score_total = dico_box[annee][nom_a_abrev[equipe]]
            box = clean_DNP(enlever_totals(box_score_total))
            box = box.loc[box['DATE'] >= date_debut_build].reset_index(drop=True)
            for match in range(box.shape[0]):
                date = box['DATE'][match]
                joueur = box['PLAYER'][match]
                if schedule.loc[schedule['DATE'] == date]['VISITOR'].reset_index(drop=True)[0] == equipe:
                    equipe_opp = schedule.loc[schedule['DATE'] == date].reset_index(drop=True)['HOME'][0]
                else:
                    equipe_opp = schedule.loc[schedule['DATE'] == date].reset_index(drop=True)['VISITOR'][0]
                X = pd.merge((X, input_total(joueur, date, nom_a_abrev[equipe], nom_a_abrev[equipe_opp])), axis=1)
                Y = pd.merge((Y, Y_total(joueur, date, nom_a_abrev[equipe])), axis=1)
    X.to_csv('X' + annee + '.csv')
    Y.to_csv('Y' + annee)
    return X, Y