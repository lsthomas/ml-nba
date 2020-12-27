import matplotlib
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, RandomizedSearchCV

from dicos_utiles import dico_inputs_train, dataset_train, dataset_test

pd.set_option('display.max_columns', None)

#dataset_train = dataset_train.head(100)

print(dataset_train.values.shape)

# Tout :
tout = list(set(dataset_train.columns[1:-1]))


tout_sauf_ttfl = list(set(dataset_train.columns[1:-1]).difference({'TTFL.1','TTFL'}))

tout_sauf_flop_50 = list(set(dataset_train.columns[1:-1]).difference({'ORB%', 'TRB%.2', '3PAr', 'TRB%', 'TRB%.3', 'TRB%.1', 'BLK%.3', 'ORB.2', '3PA.3', 'eFG%.2', 'eFG%.3', 'BLK%', '+/-', 'ORB', 'BLK.2', 'BLK%.1', 'PTS', '3PA.2', 'BLK', 'AST.1', 'eFG%.1', 'FTA.1', '3PAr.2', 'FG.2', 'FTr.2', 'FG', '3P.3', 'DRB.1', 'AST%.3', 'FTA', 'FTA.2', 'ORtg.2', 'FGA', 'AST.2', '3P.1', 'TRB', 'FT.2', 'TS%.2', '3P', 'TS%.3', 'TRB.1', '3PA', 'REP', 'BLK.1', 'ORB.1', 'FT', 'eFG%', 'STL.1', 'EQ/OPP', 'EQ/OPP.1'}))

tout_sauf_flop_50_et_TTFL = list(set(dataset_train.columns[1:-1]).difference({'TTFL','TTFL.1','ORB%', 'TRB%.2', '3PAr', 'TRB%', 'TRB%.3', 'TRB%.1', 'BLK%.3', 'ORB.2', '3PA.3', 'eFG%.2', 'eFG%.3', 'BLK%', '+/-', 'ORB', 'BLK.2', 'BLK%.1', 'PTS', '3PA.2', 'BLK', 'AST.1', 'eFG%.1', 'FTA.1', '3PAr.2', 'FG.2', 'FTr.2', 'FG', '3P.3', 'DRB.1', 'AST%.3', 'FTA', 'FTA.2', 'ORtg.2', 'FGA', 'AST.2', '3P.1', 'TRB', 'FT.2', 'TS%.2', '3P', 'TS%.3', 'TRB.1', '3PA', 'REP', 'BLK.1', 'ORB.1', 'FT', 'eFG%', 'STL.1', 'EQ/OPP', 'EQ/OPP.1'}))

top_30 = ['TTFL.1', 'ORtg.1', 'DRtg.3', 'MP.1', 'TS%.1', 'BPM.1', '+/-.1', 'DRB%.3', 'PTS.2', 'FGA.3', 'BLK.3', 'TOV%.1', 'PF.3', 'DRB%.1', '3PAr.3', 'TTFL', 'DRtg.1', 'DRB.2', 'DRtg.2', 'FGA.2', 'ORB%.2', 'ORtg.3', 'STL%.1', 'FTr.1', 'PF', 'AST.3', 'FG.3', 'PF.2', 'USG%.1', 'FT.3']

top_30_sans_ttfl = ['ORtg.1', 'DRtg.3', 'MP.1', 'TS%.1', 'BPM.1', '+/-.1', 'DRB%.3', 'PTS.2', 'FGA.3', 'BLK.3', 'TOV%.1', 'PF.3', 'DRB%.1', '3PAr.3','DRtg.1', 'DRB.2', 'DRtg.2', 'FGA.2', 'ORB%.2', 'ORtg.3', 'STL%.1', 'FTr.1', 'PF', 'AST.3', 'FG.3', 'PF.2', 'USG%.1', 'FT.3']

top_5 = ['TTFL.1', 'ORtg.1', 'DRtg.3', 'BPM.1', '+/-.1']

ttfl = ["TTFL.1"]

features = tout_sauf_flop_50

# x = dataset_train["TTFL.1"].values
x = dataset_train[features].values
y = dataset_train["Target"].values
x_test = dataset_test[features].values
y_test = dataset_test["Target"].values
print('fit')

GRID = True


if GRID:
    random_grid = {'bootstrap': [True, False],
                   'max_depth': [5, 7, 10, 12, 15, 17, 20],
                   'max_features': ['auto', 'sqrt'],
                   'min_samples_leaf': [1, 2, 4],
                   'min_samples_split': [2, 5, 10],
                   'n_estimators': [50, 70, 100, 120, 150]}
    # Use the random grid to search for best hyperparameters
    # First create the base model to tune
    rf = RandomForestRegressor()
    # Random search of parameters, using 3 fold cross validation,
    # search across 100 different combinations, and use all available cores
    clf = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=10, cv=3, verbose=2,
                                   random_state=42, n_jobs=-1)
    # Fit the random search model
    clf.fit(x, y)
    res = pd.DataFrame(clf.cv_results_)
    res =  res.sort_values('rank_test_score')

    clf = clf.best_estimator_

else:
    clf = RandomForestRegressor(n_estimators=15, bootstrap=True, max_depth=7)
    clf.fit(x, y)




print("train", mean_squared_error(clf.predict(x), y))
print("test", mean_squared_error(clf.predict(x_test), y_test))

feature_importance = dict(
    sorted(zip(features, clf.feature_importances_), key=lambda e: e[1], reverse=True)
)
print(list(feature_importance.keys())[:30])
print(feature_importance)
pd.DataFrame(feature_importance, index=[0]).head(10).plot.bar()
matplotlib.pyplot.show()


