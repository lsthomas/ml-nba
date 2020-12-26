from sklearn.metrics import mean_squared_error

from dicos_utiles import dico_inputs_train, nom_a_abrev, dico_schedule, dico_box, dataset_test
import numpy as np
from process import build_train, input_total, Y_total, build_test, input_equipes, clean_DNP, input_joueur
import pandas as pd

from ttlf.recup_dataset import recup_tout_box, recup_schedule, recup_tout_roster, corriger

#recup_schedule('2017')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified alsocorr
    print(input_joueur('Joe Harris','2018-11-02'))



#corriger('PHI','Elton Brand','2017')