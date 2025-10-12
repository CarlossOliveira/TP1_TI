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

def create_bar_graph(x, x_data, y_data):
    plt.figure(layout="tight", num=f'Número de ocorrências representado em gráfico de barras - {x}')
    positions = np.arange(len(x_data)) # Create an array with positions for each bar
    plt.bar(positions, y_data, color='red', align='center') # Create the bar graph
    plt.xticks(positions, x_data, fontsize=6) 
    plt.xlabel(x)
    plt.ylabel("Count")

def main():
    data = pd.read_excel('data/CarDataSet.xlsx') # Read the Excel file
    matrix = data.values # Convert the DataFrame to a matrix
    var_names = data.columns.values.tolist() # Get the column names

    # Create plot window, give it a title and configure grid layout
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(15,10))
    
    # Create scatter plots for MPG vs each of the other variables
    for i in range(6):
        create_plot(var_names[6], var_names[i], data[var_names[6]], data[var_names[i]], i + 1)
    
    # Convert all the data in matrix to uint16
    matrix_uint16 = matrix.astype(np.uint16)
    
    # Create an alphabet for matrix_uint16
    alphabet = np.unique(matrix_uint16)
    
    # Calculate the number of occurrences of each element of the alphabet in each variable (column)
    total_occurrences = np.zeros((len(var_names), len(alphabet)), dtype=np.uint16) # Creates a 2 axis array (matrix) filled with 0s with the number of rows equal to the number of variables (columns in the original matrix) and the number of columns equal to the number of unique elements in the alphabet. This matrix will be used to store the count of occurrences of each element of the alphabet in each variable (column).
    for col in range(len(var_names)):
        for symbol in range(len(alphabet)):
            occurrences = matrix_uint16[:, col] == alphabet[symbol] # Creates a boolean array where the symbol is found in the column. Example case: We are searching for the number of occurences of the symbol 5 in column 0 (column 0 = [5,2,5,6,0,89,5]). The occurrences array will be [True, False, True, False, False, False, True] where True indicates the presence of the symbol.
            total_occurrences[col, symbol] = np.sum(occurrences) # Sum the boolean array to get the number of occurrences of the symbol. NOTE: It's important to remember that in Python, True is equivalent to 1 and False is equivalent to 0. So, summing the boolean array gives the count of True values, which corresponds to the number of occurrences of the symbol in the column.

    # Create bar graphs for each variable
    for var in range(len(var_names)):
        indice_nonzero = total_occurrences[var].nonzero()[0] 
        create_bar_graph(var_names[var], alphabet[indice_nonzero], total_occurrences[var][indice_nonzero])
    plt.show()

if __name__ == "__main__":
    main()