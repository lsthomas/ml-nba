
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.layers import BatchNormalization

from dicos_utiles import nom_a_abrev, dico_box
from process import date_to_saison, build_test, input_total
from recup_dataset import recup_matchs

import numpy as np


def train(X_train, Y_train):
    model = Sequential()

    model.add(Dense(125, activation='relu', input_dim=125))
    model.add(BatchNormalization())

    model.add(Dense(15, activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    # model.add(Dense(200, activation='relu'))
    # model.add(Dropout(0.2))
    # model.add(BatchNormalization())

    model.add(Dense(15, activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(15, activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(15, activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(15, activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())

    model.add(Dense(1, activation='relu'))

    model.compile(loss="mean_squared_error", optimizer='adam')
    model.fit(X_train, Y_train, epochs=100, batch_size=64, verbose=2)
    return model


def corriger_nan(X, Y):
    i = 0
    while i < X.shape[0]:
        nan = False
        for j in range(125):
            if np.isnan(X[i][j]):
                nan = True
        if nan:
            X = np.delete(X, i, 0)
            Y = np.delete(Y, i, 0)
        i += 1
    return X, Y


def check_nan(df):
    df.isnull().values.any()



def baseline(X):
    """"X : """
    m, n = dico_inputs_train.shape
    Y_base = np.empty([m, 1])
    for i in range(m):
        Y_base[i, 0] = X[i, 67]
    return Y_base




