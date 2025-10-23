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
    plt.figure(layout = "tight", num = f"Numero de - {var_names}")
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
    valorMin = int(np.min(colunaVar))

    for i in range(valorMin, valorMax + 1, step): #nao comeca em 0 mas sim no valor min
        intervalo = (colunaVar >= i) & (colunaVar < i + step)
        #agora o loop so cobre o intrevalo relevante
        
        values_in_interval = colunaVar[intervalo]
        if len(values_in_interval) == 0:
            continue
        unique_values, counts = np.unique(values_in_interval, return_counts=True)
        replacement_value = unique_values[np.argmax(counts)]

        colunaVar = np.where(intervalo, replacement_value, colunaVar)

    matrix[:, indice] = colunaVar
    return matrix
 
# Function to calculate entrophy
def calcularEntropia(numberOccurrences):
    p = numberOccurrences / np.sum(numberOccurrences)
    H = -np.sum(p * np.log2(p))
    return H

# Huffman
def huffman(data, numberOccurrences):
    codec = huffc.HuffmanCodec.from_data(data)
    symbols, lenghts = codec.get_code_len() # retorna os símbolos e as lengths organizadas como no alphabet

    # Criar dicionário para mapear símbolo -> comprimento Huffman
    # Calcular probabilidades
    p = numberOccurrences / np.sum(numberOccurrences)

    # Comprimento médio (L) = soma(p_i * l_i)
    comprimento_medio = np.sum(p * lenghts)

    # Variância = soma(p_i * (l_i - L)^2)
    variancia = np.sum(p * (lenghts - comprimento_medio) ** 2)

    return comprimento_medio, variancia

def main():
    # Ex1: ler dados
    data = pd.read_excel('data/CarDataset.xlsx')
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
    for variavel, step in [('Weight', 40), ('Displacement', 5), ('Horsepower', 5)]:
        idx = var_names.index(variavel)
        matrix_uint16 = binning(matrix_uint16, step, idx)
    
    alphabet, numberOccurrences = extractAlphabetCounts(matrix_uint16, var_names)
    for variavel in ['Weight', 'Displacement', 'Horsepower']:
        idx = var_names.index(variavel)
        create_plot_bar(alphabet[idx], numberOccurrences[idx], variavel)

    # Ex7: calculate entrophy 
    print("Valor médio (teórico) de bits por símbolo:")
    for i in range (len(var_names)):
        counts = numberOccurrences[i]
        entropia = calcularEntropia(counts)
        print(f"H{var_names[i][:3]}= {entropia}")

    # Ex8: Huffman coding - número médio de bits por símbolo
    print("\nNúmero médio de bits por símbolo e variância ponderada dos comprimentos:")
    for i in range(len(var_names)):
        comprimento_medio, variancia = huffman(matrix_uint16[:, i], numberOccurrences[i])
        print(f"L{var_names[i][:3]}= {comprimento_medio} bits/simbolo, Var= {variancia:}")

if __name__ == "__main__":
    main()