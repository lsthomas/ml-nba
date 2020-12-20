from NN_model import MSE
from dicos_utiles import dico_inputs_train
from process import build_train, input_total
import pandas as pd


X,Y = dico_inputs_train['2019']
Y_pred_base = X['TTFL'].values
pd.concat((None,pd.DataFrame))v
print(Y.shape)
print(X.shape)
print(MSE(Y,Y_pred_base))

