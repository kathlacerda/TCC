import pandas as pd

df2018 = pd.read_csv(r'C:\Users\kathl\Documents\Unicap\TCC\Censo2018\situacaofinalalunos_2018.csv', sep=';',
                     low_memory=False)
# print(df2018)

df2018escolas = pd.read_csv(r'C:\Users\kathl\Documents\Unicap\TCC\Censo2018\escolasMUNICIPAIS2018.csv', sep=';',
                            low_memory=False)

# df2019 = pd.read_csv(r'C:\Users\kathl\PycharmProjects\TCC\alunos_2019.csv', sep=';',low_memory=False)
# print(df2019)

# df2020 = pd.read_csv(r'C:\Users\kathl\Documents\Unicap\TCC\Censo 2020\alunos_2020.csv', sep=';', low_memory=False)

data = pd.merge(df2018, df2018escolas, how='left', on=['NO_ENTIDADE'])
print(data)

# converting to CSV file
# data.to_csv("tabelaAlunosEscolas.csv")

data = pd.DataFrame(data)

data_fundamental = data.loc[['modens'] == '1']
print(data_fundamental)
