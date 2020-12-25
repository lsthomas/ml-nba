from dicos_utiles import dico_schedule, nom_a_abrev
import pandas as pd

from process import input_equipes


def build_paris(saison):
    """"Resu : 0 si l'équipe à domicile a perdu, 1 sinon."""
    dataset = pd.DataFrame()
    schedule = dico_schedule[saison]
    m,n = schedule.values.shape
    for i in range(m):
        equipe = nom_a_abrev[schedule['HOME'][i]]
        equipe_opp = nom_a_abrev[schedule['VISITOR'][i]]
        date = schedule['DATE'][i]
        input = input_equipes(date, equipe, equipe_opp)
        if schedule['HOME_PTS'][i] > schedule['VISITOR_PTS'][i]:
            input['Target'] = [1]
        else:
            input['Target'] = [0]
        if not (input.isnull().values.any()):
            dataset = pd.concat((dataset, input))
    dataset.to_csv('dataset' + saison + '.csv')
    return dataset




