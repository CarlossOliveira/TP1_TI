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
    plt.bar(positions, y_data, color='red', align='center') # Create the bar graph with bars centered at the positions
    plt.xticks(positions, x_data, fontsize=6) # Set x-ticks to the positions with corresponding labels from x_data
    plt.xlabel(x)
    plt.ylabel("Count")

def binning_to_var(data, var, bin_size):
    matrix_uint16 = data.values.astype(np.uint16)
    alphabet = np.unique(matrix_uint16)
    
    new_bin = np.zeros(len(alphabet), dtype=np.uint16)

    for i in range(0, len(alphabet), bin_size): 
        bin = alphabet[i:i + bin_size]
        bin_mode = np.bincount(bin).argmax()
        new_bin[i:i + bin_size] = bin_mode

    print(new_bin)
    
    var_index = data.columns.get_loc(var) # Get the index of the variable (column) in the DataFrame
    var_data = matrix_uint16[:, var_index] # Get the data of the variable (column) from the matrix
    print("-----------------")
    print(var_data)
    print("-----------------")
    print(alphabet)
    binned_var_data = np.zeros(len(var_data), dtype=np.uint16) # Create an array to store the binned data

    # Map each value in var_data to its corresponding binned value using the new_bin array
    for i in range(len(var_data)):
        symbol_index = np.where(alphabet == var_data[i])[0][0] # Find the index of the symbol in the alphabet
        binned_var_data[i] = new_bin[symbol_index] # Map the symbol to its binned value

    create_bar_graph(f'Binned {var}', np.unique(binned_var_data), np.bincount(binned_var_data)[np.unique(binned_var_data)])
    
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

    # Create bar graphs for each variable (column) showing the number of occurrences of each element of the alphabet
    for var in range(len(var_names)):
        indice_nonzero = total_occurrences[var].nonzero()[0] # Get the indices of non-zero occurrences to avoid plotting bars for elements that do not exist in the variable
        create_bar_graph(var_names[var], alphabet[indice_nonzero], total_occurrences[var][indice_nonzero])

    # Apply binning to some variables
    binning_to_var(data, 'Displacement', 5)
    binning_to_var(data, 'Horsepower', 5)
    binning_to_var(data, 'Weight', 40)

    plt.show()

if __name__ == "__main__":
    main()