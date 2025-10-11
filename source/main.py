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

def numberOfOccurrences(alphabet, matrix_uint16):
    list_alphabet = alphabet.tolist()
    occurrences_list = [0] * len(list_alphabet)  # Inicializa com zeros

    for symbol in range(len(list_alphabet)):
        occurrences = 0
        for row in range(len(matrix_uint16)):
            for col in range(len(matrix_uint16[0])):
                if matrix_uint16[row][col] == list_alphabet[symbol]:
                    occurrences += 1
        occurrences_list[symbol] = occurrences  # Substitui o valor na posição correta
        
    occurrences_alphabet = np.array(occurrences_list, dtype=np.uint16)

    return occurrences_alphabet 

def main():
    data = pd.read_excel('data/CarDataSet.xlsx') # Read the Excel file
    matrix = data.values # Convert the DataFrame to a matrix
    var_names = data.columns.values.tolist() # Get the column names

    # Create plot window, give it a title and configure grid layout
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(15,10))
    
    # Create scatter plots for MPG vs each of the other variables
    for i in range(6):
        create_plot(var_names[6], var_names[i], data[var_names[6]], data[var_names[i]], i + 1)
    
    
    # 3)
    # Convert all the data in matrix to uint16
    matrix_uint16 = matrix.astype(np.uint16) 
    
    # Create an alphabet for matrix_uint16
    alphabet = np.array([], dtype=np.uint16)
    alphabet = np.unique(matrix_uint16)
    
    
    #Versao Bernardo 3)
    matrix_uint16 = matrix.astype(np.uint16)
    alphabet = np.unique(matrix_uint16)

        
    # 4)
    print("Alphabet:\n", alphabet)
    print("Total occurrences of each element of the alphabet in each variable (column):\n", numberOfOccurrences(alphabet, matrix_uint16))
    
    #plt.show()


if __name__ == "__main__":
    main()