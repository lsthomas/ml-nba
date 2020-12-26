from ttlf.dicos_utiles import dico_inputs_train

df = dico_inputs_train['2018']
df2 = dico_inputs_train['2019']

columns = df.columns

for colonne in list(df.columns):
    print(colonne + ' : ' + str(df[colonne].corr(df['Target'])) + ' ; ' + str(df2[colonne].corr(df2['Target'])))