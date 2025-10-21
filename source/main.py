import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import huffmancodec as huffc

# Function to create plots
def create_plot(x, y, x_data, y_data, num_plot, comp):
    plt.subplot(comp//2,2,num_plot) #grafico 3 linhas 2 colunas
    plt.scatter(x_data,y_data,color="m") #O eixo x recebe os valores de x_data, O eixo y recebe os valores de y_data.
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs. {x}')
    plt.autoscale() #ajusta automaticamente os limites dos eixos (X e Y) com base nos dados que foram desenhados no gráfico. 

# Function to plot bars
def create_plot_bar(alphabet, numberOccurrences, var_names):
    plt.figure(layout = "tight", num = f"Nuemro de - {var_names}")
    plt.bar(alphabet.astype('str'), numberOccurrences, color='red', align= "center")
    plt.title('Distribuição ' + var_names)
    plt.xlabel(var_names)
    plt.ylabel("Count")
    plt.xticks(rotation = 90)

    plt.show()

# Function to calculate number of occurrences
def extractAlphabetCounts(matrix_uint16, var_names):
    alphabet = [None] * len(var_names)
    numberOccurrences = [None] * len(var_names)
    
    for i in range (len(var_names)):
        unique_vals, counts = np.unique(matrix_uint16[:, i], return_counts=True)
        alphabet[i] = unique_vals.astype(np.uint16)
        numberOccurrences[i] = counts.astype(np.uint16)

    return alphabet, numberOccurrences

# Function of binning
def binning(matrix, step, indice):
    colunaVar = matrix[:, indice].copy()
    valorMax = int(np.max(colunaVar))

    for i in range(0, valorMax + 1, step):
        intervalo = (colunaVar >= i) & (colunaVar < i + step)
        if not np.any(intervalo):
            continue
        # Use bincount to find the most frequent value in the interval
        values_in_interval = colunaVar[intervalo]
        if len(values_in_interval) == 0:
            continue
        unique_values, counts = np.unique(values_in_interval, return_counts=True)
        replacement_value = unique_values[np.argmax(counts)]

        colunaVar = np.where(intervalo, replacement_value, colunaVar)

    matrix[:, indice] = colunaVar
    return matrix
 
# Functoin to calculate entrophy
def calcularEntropia(numberOccurrences):
    p = numberOccurrences / np.sum(numberOccurrences)
    H = -np.sum(p * np.log2(p))
    return H

# Huffman
def huffman(numberOccurrences, list_num):
    codec = huffc.HuffmanCodec.from_data(list_num)
    symbols, lenghts = codec.get_code_len()



def main():
    # Ex1: ler dados
    data = pd.read_excel('/Users/miguel/Desktop/GitHub/TP1_TI/data/CarDataset.xlsx')
    matrix = data.values # Convert the DataFrame to a matrix, funcao de pandas
    var_names = data.columns.values.tolist() # Get the column names

    # Ex2: Create scatter plots for MPG vs each of the other variables
    plt.figure(layout="tight", num="relação entre MPG e as diferentes variáveis (características do carro)", figsize=(10,6))
    comp_var = len(var_names) - 1
    for i in range(comp_var):
        create_plot(var_names[i], var_names[comp_var], data[var_names[i]], data[var_names[comp_var]], i + 1, comp_var)
    plt.show()
    
    # Ex3: Convert all the data in matrix to uint16
    matrix_uint16 = matrix.astype(np.uint16) 
           
    # Ex4: Calculate occurrences
    alphabet, numberOccurrences = extractAlphabetCounts(matrix_uint16, var_names)

    # Ex5: Plot bars
    for i in range (comp_var):
        create_plot_bar(alphabet[i], numberOccurrences[i], var_names[i])

    # Ex6: apply binning to some variables
    columnsVar = ['Displacement', 'Horsepower', 'Weight']
    step_sizes = [5, 5, 40]
    binned_data = matrix_uint16.copy() 
    var_names_arr = np.array(var_names)
    updated_counts = {}
    
    for i in range(len(columnsVar)):
        var = columnsVar[i]
        step = step_sizes[i]
        index = np.where(var_names_arr == var)[0][0]

        binned_data = binning(binned_data, step, index)

        # Visualize the distribution after binning
        unique_vals, counts = np.unique(binned_data[:, index], return_counts=True)
        updated_counts[var] = counts
        create_plot_bar(unique_vals, counts, var)

    # Ex7: calculate entrophy 
    for i in range (len(var_names)):
        var = var_names[i]
        
        if var in updated_counts:
            counts = updated_counts[var]
        else:
            counts = numberOccurrences[i]

        entropia = calcularEntropia(counts)
        print(f"H{var[:3]}= {entropia}")

if __name__ == "__main__":
    main()