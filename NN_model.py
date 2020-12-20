
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.python.keras.layers import BatchNormalization

from dicos_utiles import nom_a_abrev, dico_box
from process import date_to_saison
from recup_dataset import recup_matchs


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


model = train(X, Y)


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


array_sum = np.sum(X_test)
array_has_nan = np.isnan(array_sum)
print(array_has_nan)

"""## Test"""


def build_test(date_debut, date_fin):
    annee = date_to_saison(date_debut)
    X = np.empty([125, 1])
    Y = np.empty([1, 1])
    for equipe in list(nom_a_abrev):
        if not (equipe in deja_fait):
            print(equipe)
            schedule = recup_matchs(equipe, annee)
            box_score_total = dico_box[annee][nom_a_abrev[equipe]]
            box = clean_DNP(enlever_totals(box_score_total))
            box = box.loc[box['DATE'] >= date_debut].reset_index(drop=True)
            box = box.loc[box['DATE'] <= date_fin].reset_index(drop=True)
            for match in range(box.shape[0]):
                date = box['DATE'][match]
                joueur = box['PLAYER'][match]
                if schedule.loc[schedule['DATE'] == date]['VISITOR'].reset_index(drop=True)[0] == equipe:
                    equipe_opp = schedule.loc[schedule['DATE'] == date].reset_index(drop=True)['HOME'][0]
                else:
                    equipe_opp = schedule.loc[schedule['DATE'] == date].reset_index(drop=True)['VISITOR'][0]
                X = np.concatenate((X, input_total(joueur, date, nom_a_abrev[equipe], nom_a_abrev[equipe_opp])), axis=1)
                Y = np.concatenate((Y, Y_total(joueur, date, nom_a_abrev[equipe])), axis=1)
    X = np.delete(X, 0, 1)
    Y = np.delete(Y, 0, 1)
    X, Y = corriger_nan(X, Y)
    return X, Y


X_test, Y_test = build_test('2018-10-29', '2018-10-31')

model.evaluate(X_test, Y_test)

model.predict([input_total('DeMar DeRozan', '2018-10-31', 'SAS', 'PHO').T])

Y_test


def baseline(X):
    m, n = X.shape
    Y_base = np.empty([m, 1])
    for i in range(m):
        Y_base[i, 0] = X[i, 67]
    return Y_base


def MSE(Y, Y_pred):
    return np.mean(np.square(Y - Y_pred))


X[0:10][0:5]
