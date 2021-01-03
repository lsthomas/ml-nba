from ttlf.dicos_utiles import nom_a_abrev, deja_fait, dico_box
from ttlf.process import date_to_saison, clean_DNP, enlever_totals, input_total
import pandas as pd

from ttlf.recup_dataset import recup_matchs

def Y_total_paris(joueur,date,equipe) :
    saison = date_to_saison()




def build_train(date_debut_build):
    annee = date_to_saison(date_debut_build)
    dataset = pd.DataFrame()
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
                input = input_total(joueur, date, nom_a_abrev[equipe], nom_a_abrev[equipe_opp])
                input['Target'] = [Y_total_paris(joueur, date, nom_a_abrev[equipe])]
                if not (input.isnull().values.any()):
                    dataset = pd.concat((dataset, input))
    dataset.to_csv('dataset' + annee + '.csv')
    return dataset