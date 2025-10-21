import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def create_plot(y, x, y_data, x_data, num_plot=1):
    plt.subplot(3,2,num_plot)
    plt.scatter(x_data,y_data,color="m")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs. {x}')
    plt.autoscale()


def create_bar_chart(x, y_data, x_data):
    name = f"Número de ocorrências representado em gráfico de barras - {x}"
    positions = np.arange(len(x_data))  # The label locations [0, 1, 2, ..., len(x_data)-1]
    plt.figure(layout="tight", num=name)
    plt.bar(positions, y_data, color="red", align="center") # NOTE: The positions array is used to position the bars on the x-axis based on the number of unique elements in x_data.
    plt.xticks(positions, x_data) # The xticks function is used to set the labels on the x-axis to the unique elements in x_data and to position them correctly under the bars.
    plt.ylabel("Count")
    plt.xlabel(x)


def main():
    data = pd.read_excel(r"data/CarDataSet.xlsx") # Read the Excel file
    matrix = data.values # Convert the DataFrame to a matrix
    var_names = data.columns.values.tolist() # Get the column names

    # Create plot window, give it a title and configure grid layout for the 6 scatter plots
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(15,10))
    
    # Create scatter plots for MPG vs each of the other variables
    for i in range(6):
        create_plot(var_names[6], var_names[i], data[var_names[6]], data[var_names[i]], i + 1)
    
    # Convert all the data in matrix to uint16
    matrix_uint16 = matrix.astype(np.uint16)
    
    # Create alphabet and symbol count arrays for each variable
    alphabet = [None] * len(var_names)
    symbol_count = [None] * len(var_names)
    for col in range(len(var_names)):
        # Get unique values and their counts for each column
        unique_vals, counts = np.unique(matrix_uint16[:, col], return_counts=True)
        
        # Create an alphabet for matrix_uint16
        alphabet[col] = unique_vals
        
        # Create a symbol count array initialized to zeros
        symbol_count[col] = np.zeros(len(alphabet[col]), dtype=np.uint16)
        symbol_count[col] = counts
        
        # Criar gráficos de barras para cada variável, filtrando ocorrências zero
        indices_nonzero = np.nonzero(symbol_count[col])[0]
        create_bar_chart(var_names[col], symbol_count[col][indices_nonzero], alphabet[col][indices_nonzero])

        plt.show()


if __name__ == "__main__":
    main()