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
    alphabet = np.array([], dtype=np.uint16)
    alphabet = np.unique(matrix_uint16)
    
    # Calculate the number of occurrences of each element of the alphabet in each variable (column) [ERRO]
    total_occurrences = np.zeros((len(alphabet), matrix_uint16.shape[1]), dtype=np.uint16)
    for num in alphabet:
        occurrences=0
        arr=np.where(matrix_uint16[:, None] == num, occurrences + 1, occurrences)
        total_occurrences += arr.astype(np.uint16)
    print("Alphabet:\n", alphabet)
    print("Total occurrences of each element of the alphabet in each variable (column):\n", total_occurrences)
    
    plt.show()


if __name__ == "__main__":
    main()