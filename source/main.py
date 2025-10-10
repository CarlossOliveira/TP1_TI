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
    matrix = data.values.tolist() # Convert the DataFrame to a matrix
    var_names = data.columns.values.tolist() # Get the column names

    # Create plot window, give it a title and configure grid layout
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(15,10))
    
    
    for i in range(6):
        create_plot(var_names[6], var_names[i], data[var_names[6]], data[var_names[i]], i + 1)
    
    
    # Convert all the data in data (type: DataFrame) to uint16 then extracts column values to a nparray to then convert it to a matrix as I've done to matrix
    matrix_uint16 = (data.astype(np.uint16)).values
    print(matrix_uint16)
    # Create an alphabet for matrix_uint16 and sort it
    alphabet = []
    for line in matrix_uint16:
        for col in range(len(line)):
            if (line[col] not in alphabet):
                alphabet.append(line[col])

    
    # if (matrix_uint16[:][:] not in alphabet):
    #     alphabet.append(matrix_uint16[:][:])
    alphabet.sort()
    print(alphabet)
    # Calculate the number of occurrences of each element of the alphabet in each variable of matrix_uint16s
    
    plt.show()


if __name__ == "__main__":
    main()