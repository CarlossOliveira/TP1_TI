import pandas as pd 

data = pd.read_excel('data/CarDataSet.xlsx')

matrix = data.values.tolist()
print(matrix)
parameters = data.columns.values.tolist()
