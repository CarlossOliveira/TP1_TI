import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def create_plot(x, y, x_data, y_data, num_plot, comp):
    plt.subplot(comp//2,2,num_plot) #grafico 3 linhas 2 colunas
    plt.scatter(x_data,y_data,color="m") #O eixo x recebe os valores de x_data, O eixo y recebe os valores de y_data.
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs. {x}')
    plt.autoscale() #ajusta automaticamente os limites dos eixos (X e Y) com base nos dados que foram desenhados no gráfico.    


def create_plot_bar(alphabet, numberOccurrences, var_names):
        
    plt.figure(layout = "tight", num = f"Nuemro de - {var_names}")
    plt.bar(alphabet.astype("str"), numberOccurrences, color='red', align= "center")
    plt.title('Distribuição ' + var_names)
    plt.xlabel(var_names)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.autoscale()
    plt.show()

    
def main():
    data = pd.read_excel('data/CarDataSet.xlsx') # Read the Excel file
    matrix = data.values # Convert the DataFrame to a matrix, funcao de pandas
    var_names = data.columns.values.tolist() # Get the column names
    
    # Create plot window, give it a title and configure grid layout
    
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(10,6)) 
    
    
    # Create scatter plots for MPG vs each of the other variables
    
    comp_var = len(var_names) - 1
    
    for i in range(comp_var):
        create_plot(var_names[i], var_names[comp_var], data[var_names[i]], data[var_names[comp_var]], i + 1, comp_var)
    #plt.show()
    
    
    # 3)
    
    # Convert all the data in matrix to uint16
    matrix_uint16 = matrix.astype(np.uint16) 
    
            
    # 4)
    
    alphabet = [None] * len(var_names)
    numberOccurrences = [None] * len(var_names)

    for i in range(len(var_names)):
        unique_vals, counts = np.unique(matrix_uint16[:, i], return_counts=True)
        alphabet[i] = unique_vals.astype(np.uint16)
        numberOccurrences[i] = counts.astype(np.uint16)
    
    
    # 5)
    
    for i in range(comp_var):    
        create_plot_bar(alphabet[i], numberOccurrences[i], var_names[i])

    #6 
    
    # np.where(minimo intrevalo e max intrevalo, TRUE acontecimento, False acontecimento) depois devol usar no exercicio 6



if __name__ == "__main__":
    main()