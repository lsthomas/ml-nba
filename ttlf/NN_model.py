from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.layers import BatchNormalization

from dicos_utiles import nom_a_abrev, dico_box, dataset_train, dataset_test
from process import date_to_saison, build_test, input_total
from recup_dataset import recup_matchs

import numpy as np

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

optimizer = tf.keras.optimizers.RMSprop(
    learning_rate=0.0005
)

def train(X_train, Y_train):
    model = Sequential()

    model.add(Dense(X_train.shape[1], activation='relu', input_dim=X_train.shape[1]))
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

    #model.add(Dense(15, activation='relu'))
    #model.add(Dropout(0.2))
    #model.add(BatchNormalization())

    #model.add(Dense(15, activation='relu'))
    #model.add(Dropout(0.2))
    #model.add(BatchNormalization())

    model.add(Dense(1, activation='relu'))
    model.compile(loss="mean_squared_error", optimizer='adam', metrics = ['mean_absolute_error'])
    model.summary()
    model.fit(X_train, Y_train, epochs=20, batch_size=64, verbose=2, validation_data = (x_test,y_test) )
    return model

#Tout :
#features = list(set(dataset_train.columns[1:-1])

# Tout sauf TTFL :
#features = list(set(dataset_train.columns[1:-1]).difference({'TTFL.1','TTFL'}))

#Tout sauf flop 50:
#features = list(set(dataset_train.columns[1:-1]).difference({'ORB%', 'TRB%.2', '3PAr', 'TRB%', 'TRB%.3', 'TRB%.1', 'BLK%.3', 'ORB.2', '3PA.3', 'eFG%.2', 'eFG%.3', 'BLK%', '+/-', 'ORB', 'BLK.2', 'BLK%.1', 'PTS', '3PA.2', 'BLK', 'AST.1', 'eFG%.1', 'FTA.1', '3PAr.2', 'FG.2', 'FTr.2', 'FG', '3P.3', 'DRB.1', 'AST%.3', 'FTA', 'FTA.2', 'ORtg.2', 'FGA', 'AST.2', '3P.1', 'TRB', 'FT.2', 'TS%.2', '3P', 'TS%.3', 'TRB.1', '3PA', 'REP', 'BLK.1', 'ORB.1', 'FT', 'eFG%', 'STL.1', 'EQ/OPP', 'EQ/OPP.1'}))

# Top 30 :
#features = ['TTFL.1', 'ORtg.1', 'DRtg.3', 'MP.1', 'TS%.1', 'BPM.1', '+/-.1', 'DRB%.3', 'PTS.2', 'FGA.3', 'BLK.3', 'TOV%.1', 'PF.3', 'DRB%.1', '3PAr.3', 'TTFL', 'DRtg.1', 'DRB.2', 'DRtg.2', 'FGA.2', 'ORB%.2', 'ORtg.3', 'STL%.1', 'FTr.1', 'PF', 'AST.3', 'FG.3', 'PF.2', 'USG%.1', 'FT.3']

# Top 30 sans TTFL :
features = ['ORtg.1', 'DRtg.3', 'MP.1', 'TS%.1', 'BPM.1', '+/-.1', 'DRB%.3', 'PTS.2', 'FGA.3', 'BLK.3', 'TOV%.1', 'PF.3', 'DRB%.1', '3PAr.3','DRtg.1', 'DRB.2', 'DRtg.2', 'FGA.2', 'ORB%.2', 'ORtg.3', 'STL%.1', 'FTr.1', 'PF', 'AST.3', 'FG.3', 'PF.2', 'USG%.1', 'FT.3']


# Top 5:
#features = ['TTFL.1', 'ORtg.1', 'DRtg.3', 'BPM.1', '+/-.1']

#features = ["TTFL.1"]
#features = ['TTFL.1','DRtg.3','REP','EQ/OPP']

x = dataset_train[features].values
y = dataset_train["Target"].values
x_test = dataset_test[features].values
y_test = dataset_test["Target"].values

print(x.shape)

print("Train")

model = train(x,y)


print("train", mean_squared_error(model.predict(x), y))
print("test", mean_squared_error(model.predict(x_test), y_test))










