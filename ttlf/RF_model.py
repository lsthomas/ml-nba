import matplotlib
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from dicos_utiles import dico_inputs_train
clf = RandomForestRegressor(n_estimators=50, bootstrap=True, max_depth=10)

# dataset = dataset.head(1000)
dataset = dico_inputs_train['2019']
dataset_train, dataset_test = train_test_split(dataset, test_size=0.2)

print(dataset_train.values.shape)

#features = list(set(dataset_train.columns[1:-1]).difference({'TTFL.1','TTFL'}))
#features = list(set(dataset_train.columns[1:-1]).difference({'ORB%', 'TRB%.2', '3PAr', 'TRB%', 'TRB%.3', 'TRB%.1', 'BLK%.3', 'ORB.2', '3PA.3', 'eFG%.2', 'eFG%.3', 'BLK%', '+/-', 'ORB', 'BLK.2', 'BLK%.1', 'PTS', '3PA.2', 'BLK', 'AST.1', 'eFG%.1', 'FTA.1', '3PAr.2', 'FG.2', 'FTr.2', 'FG', '3P.3', 'DRB.1', 'AST%.3', 'FTA', 'FTA.2', 'ORtg.2', 'FGA', 'AST.2', '3P.1', 'TRB', 'FT.2', 'TS%.2', '3P', 'TS%.3', 'TRB.1', '3PA', 'REP', 'BLK.1', 'ORB.1', 'FT', 'eFG%', 'STL.1', 'EQ/OPP', 'EQ/OPP.1'}))
#features = ['TTFL.1', 'ORtg.1', 'DRtg.3', 'BPM.1', '+/-.1']
#features = ["TTFL.1"]
features = ['TTFL.1','DRtg.3','REP','EQ/OPP']



print(features)

# x = dataset_train["TTFL.1"].values
x = dataset_train[features].values
y = dataset_train["Target"].values
x_test = dataset_test[features].values
y_test = dataset_test["Target"].values
print('fit')
clf.fit(x, y)
print("train", mean_squared_error(clf.predict(x), y))
print("test", mean_squared_error(clf.predict(x_test), y_test))

feature_importance = dict(
    sorted(zip(features, clf.feature_importances_), key=lambda e: e[1], reverse=True)
)
print(list(feature_importance.keys())[:5])
print(feature_importance)
pd.DataFrame(feature_importance, index=[0]).head(10).plot.bar()
matplotlib.pyplot.show()