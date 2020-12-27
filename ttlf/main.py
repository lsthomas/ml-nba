from sklearn.metrics import mean_squared_error

from dicos_utiles import dico_inputs_train, nom_a_abrev, dico_schedule, dico_box, dataset_test, dataset_train
import numpy as np
from process import build_train, input_total, Y_total, build_test, input_equipes, clean_DNP, input_joueur
import pandas as pd

from ttlf.recup_dataset import recup_tout_box, recup_schedule, recup_tout_roster, corriger

print(mean_squared_error(dataset_train['Target'],dataset_train['TTFL.1']))

#corriger('PHI','Elton Brand','2017')