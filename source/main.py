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
    plt.bar(alphabet.astype('str'), numberOccurrences, color='red', align= "center") #alphabet_str = alphabet.astype(str) 25.0 -> 25 mas estraga os outros graficos
    plt.title('Distribuição ' + var_names)
    plt.xlabel(var_names)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.autoscale()
    plt.show()
    
def extractAlphabetCounts(matrix_uint16, var_names):
    
    alphabet = [None] * len(var_names)
    numberOccurrences = [None] * len(var_names)

    for i in range(len(var_names)):
        unique_vals, counts = np.unique(matrix_uint16[:, i], return_counts=True)
        alphabet[i] = unique_vals.astype(np.uint16)
        numberOccurrences[i] = counts.astype(np.uint16)

    return alphabet, numberOccurrences
    
    
def binning(matrix, step, indice):
    colunaVar = matrix[:, indice].copy()
    valorMin = np.min(colunaVar)
    valorMax = np.max(colunaVar)

    for i in range(valorMin, valorMax + 1, step):
        intervalo = (colunaVar >= i) & (colunaVar < i + step)
        if not np.any(intervalo):
            continue
        # Use bincount to find the most frequent value in the interval
        values_in_interval = colunaVar[intervalo]
        if len(values_in_interval) == 0:
            continue
        unique_values, counts = np.unique(values_in_interval, return_counts=True)
        replacement_value = unique_values[np.argmax(counts)]
        colunaVar[intervalo] = replacement_value

    matrix[:, indice] = colunaVar
    return matrix

def mudar_coluna(matriz, coluna, n_col):
    matriz[:, n_col] = coluna
    return matriz

def calcularEntropia(numberOccurrences):
    p = numberOccurrences / np.sum(numberOccurrences)
    H = -np.sum(p * np.log2(p))
    return H

# Huffman
# def huffman(numberOccurrences, list_num):
#     codec = huffc.HuffmanCodec.from_data(list_num)
#     symbols, lenghts = codec.get_code_len()
    
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
    
    alphabet, numberOccurrences = extractAlphabetCounts(matrix_uint16, var_names)
    
    
    # 5)
    
    for i in range(comp_var):    
        create_plot_bar(alphabet[i], numberOccurrences[i], var_names[i])

    #6 
    
    colunasVariveis = ['Displacement', 'Horsepower', 'Weight']
    steps = [5, 5, 50] 
    var_names_arr = np.array(var_names) #where so trabalha com arr

    for i in range(len(colunasVariveis)):
        var = colunasVariveis[i]
        step = steps[i]
                
        index = np.where(var_names_arr == var)[0][0] #np.where(var_names_arr == var)[0] → retorna: array([3]) 
                                                     #np.where(var_names_arr == var)[0][0] → retorna: 3
        # Extrair a coluna de dados como uint16
        list_num = matrix[:, index].astype(np.uint16)
        list_binning = binning(list_num, alphabet, numberOccurrences, step, index)
        matrix = mudar_coluna(matrix, list_binning, index)
    
    alphabet, numberOccurrences = extractAlphabetCounts(matrix, var_names)
    create_plot_bar(alphabet, numberOccurrences, var_names)
        
    
    
if __name__ == "__main__":
    main()