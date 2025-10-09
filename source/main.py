import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def create_plot(y, x, y_data, x_data, num_plot=1):
    plt.subplot(2,3,num_plot)
    plt.scatter(x_data,y_data,color="darkmagenta")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs. {x}')
    plt.autoscale()


if __name__ == "__main__":
    data = pd.read_excel('data/CarDataSet.xlsx') # Read the Excel file
    matrix = data.values.tolist() # Convert the DataFrame to a matrix
    parameters = data.columns.values.tolist() # Get the column names
    
    # Create plot window, give it a title and configure grid layout
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(15,10))
    
    # MPG vs. Acceleration
    create_plot('MPG', 'Acceleration', data['MPG'], data['Acceleration'], 1)
    
    # MPG vs. Cylinders
    create_plot('MPG', 'Cylinders', data['MPG'], data['Cylinders'], 2)
    
    # MPG vs. Displacement
    create_plot('MPG', 'Displacement', data['MPG'], data['Displacement'], 3)
    
    # MPG vs. Horsepower
    create_plot('MPG', 'Horsepower', data['MPG'], data['Horsepower'], 4)

    # MPG vs. Model Year
    create_plot('MPG', 'Model Year', data['MPG'], data['ModelYear'], 5)

    # MPG vs. Weight
    create_plot('MPG', 'Weight', data['MPG'], data['Weight'], 6)

    # Convert all the data in data (type: DataFrame) to uint16 then extracts column values to a nparray to then convert it to a matrix as I've done to matrix
    matrix_uint16 = (data.astype(np.uint16)).values
    print(matrix_uint16)
    
    # Create an alphabet for matrix_uint16 and sort it
    alphabet = []
    for line in matrix_uint16:
        for col in range(len(line)):
            if (line[col] not in alphabet):
                alphabet.append(line[col])
    alphabet.sort()
    
    plt.show()