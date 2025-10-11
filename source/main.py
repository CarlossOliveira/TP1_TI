import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import time as t


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
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] Scatter plots created successfully.")
    
    # Convert all the data in matrix to uint16
    matrix_uint16 = matrix.astype(np.uint16)
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] Data converted to uint16 successfully.")
    
    # Create an alphabet for matrix_uint16
    alphabet = np.unique(matrix_uint16)
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] Alphabet created successfully.")
    
    # Calculate the number of occurrences of each element of the alphabet in each variable (column)
    total_occurrences = np.zeros((len(var_names), len(alphabet)), dtype=np.uint16) # Creates a 2 axis array (matrix) filled with 0s with the number of rows equal to the number of variables (columns in the original matrix) and the number of columns equal to the number of unique elements in the alphabet. This matrix will be used to store the count of occurrences of each element of the alphabet in each variable (column).
    for col in range(len(var_names)):
        for symbol in range(len(alphabet)):
            occurrences = matrix_uint16[:, col] == alphabet[symbol] # Creates a boolean array where the symbol is found in the column. Example case: We are searching for the number of occurences of the symbol 5 in column 0 (column 0 = [5, 2, 5, 6, 0, 89, 5]). The occurrences array will be [True, False, True, False, False, False, True] where True indicates the presence of the symbol.
            total_occurrences[col, symbol] = np.sum(occurrences) # Sum the boolean array to get the number of occurrences of the symbol. NOTE: It's important to remember that in Python, True is equivalent to 1 and False is equivalent to 0. So, summing the boolean array gives the count of True values, which corresponds to the number of occurrences of the symbol in the column.
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] Total occurrences matrix created successfully.")

    # Create bar charts for each variable using the total_occurrences matrix and filters out the zero occurrences
    for var in range(len(var_names)):
        indices_nonzero = total_occurrences[var].nonzero()[0]
        create_bar_chart(var_names[var], total_occurrences[var][indices_nonzero], alphabet[indices_nonzero])
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] Bar charts created successfully.")

    plt.show()
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] --> Program ended successfully.")


if __name__ == "__main__":
    print(f"[{t.strftime('%Y-%m-%d %H:%M:%S')}] --> Program started.")
    main()