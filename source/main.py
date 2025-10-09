import pandas as pd 

data = pd.read_excel('data/CarDataSet.xlsx') # Read the Excel file [1.a.]

matrix = data.values.tolist() # Convert the DataFrame to a matrix [1.b.]
parameters = data.columns.values.tolist() # Get the column names [1.c.]