import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import libraries.huffmancodec as huffc

# Function to create plots
def create_plot(x, y, x_data, y_data, num_plot, comp):
    plt.subplot(comp//2,2,num_plot) #grafico 3 linhas 2 colunas
    plt.scatter(x_data,y_data,color="m") #O eixo x recebe os valores de x_data, O eixo y recebe os valores de y_data.
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs. {x}')
    plt.autoscale() #ajusta automaticamente os limites dos eixos (X e Y) com base nos dados que foram desenhados no gráfico. 

# Function to plot bars
def create_plot_bar(alphabet, numberOccurrences, VAR_NAMES):
    plt.figure(layout = "tight", num = f"Numero de {VAR_NAMES}")
    plt.bar(alphabet.astype('str'), numberOccurrences, color='red', align= "center")
    plt.title('Distribuição ' + VAR_NAMES)
    plt.xlabel(VAR_NAMES)
    plt.ylabel("Count")
    plt.xticks(rotation = 90)
    plt.show()

# Function to calculate number of occurrences
def extractAlphabetCounts(matrix_uint16, LEN_VAR_NAMES):
    alphabet = [None] * LEN_VAR_NAMES
    numberOccurrences = [None] * LEN_VAR_NAMES
    
    for i in range (LEN_VAR_NAMES):
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
        # Agora o loop so cobre o intrevalo relevante
        
        values_in_interval = colunaVar[intervalo]
        if len(values_in_interval) == 0: # O argmax exige pelo menos um argumento
            continue
        
        unique_values, counts = np.unique(values_in_interval, return_counts=True)
        replacement_value = unique_values[np.argmax(counts)]

        colunaVar = np.where(intervalo, replacement_value, colunaVar)

    matrix[:, indice] = colunaVar
    return matrix

# Function to calculate entrophy
def calcularEntropia(p):
    H = -np.sum(p * np.log2(p))
    return H

# Huffman
def huffman(data, p):
    codec = huffc.HuffmanCodec.from_data(data)
    symbols, lengths = codec.get_code_len() # Retorna os símbolos e as lenghts organizadas como no alphabet

    # Comprimento médio (L) = soma(p_i * l_i)
    comprimento_medio = np.sum(p * lengths)
    
    # Variância = soma(p_i * (l_i - L)^2)
    variancia = np.sum(p * (lengths - comprimento_medio) ** 2)

    return comprimento_medio, variancia

# Correlação de Pearson
def correlacaoPearson(MATRIX, LEN_VAR_NAMES):
    person_values = [None] * (LEN_VAR_NAMES - 1)

    person_values = np.corrcoef(MATRIX[:, -1], MATRIX[:, :], rowvar=False)[0,1:] # Calcular a correlação entre a última coluna (MPG) e todas as outras colunas, começando a partir da segunda coluna de forma a não incluir a correlação do MPG consigo mesmo.

    return person_values

# Informação Mútua
def informacaoMutua(x, y):
    # I(X;Y) = H(X) + H(Y) - H(X,Y)
    
    # Probabilidade de X
    _, counts_x = np.unique(x, return_counts=True)
    p_x = counts_x / np.sum(counts_x)
    
    # Probabilidade de Y
    _, counts_y = np.unique(y, return_counts=True)
    p_y = counts_y / np.sum(counts_y)
    
    x_y = np.array(list(zip(x, y)))
    _, counts_xy = np.unique(x_y, axis=0, return_counts=True)
    p_xy = counts_xy / np.sum(counts_xy)

    Hx = calcularEntropia(p_x)
    Hy = calcularEntropia(p_y)
    Hxy = calcularEntropia(p_xy)
    
    Ixy = Hx + Hy - Hxy
    
    return Ixy

# Estimar MPG
def MPGpred(matrix, var_names, aceleracao_value, weight_value):
    MPG_estim = (-5.5241
                - 0.146 * aceleracao_value
                - 0.4909 * matrix[:, var_names.index('Cylinders')]
                + 0.0026 * matrix[:, var_names.index('Displacement')] 
                - 0.0045 * matrix[:, var_names.index('Horsepower')]
                + 0.6725 * matrix[:, var_names.index('ModelYear')] 
                - 0.0059 * weight_value)
    MAE = np.mean(np.abs(MPG_estim - (matrix[:, var_names.index('MPG')]))) # Mean Absolute Error
    RMSE = np.sqrt(np.mean((MPG_estim - (matrix[:, var_names.index('MPG')])) ** 2)) # Root Mean Square Error

    return MPG_estim, MAE, RMSE

def main():
    # Ex1: ler dados
    
    DATA = pd.read_excel('./data/CarDataset.xlsx')
    MATRIX = DATA.values # Convert the DataFrame to a matrix, funcao de pandas
    VAR_NAMES = DATA.columns.values.tolist() # Get the column names
    LEN_VAR_NAMES = len(VAR_NAMES)
    COMP_VAR = LEN_VAR_NAMES - 1

    # Ex2: Create scatter plots for MPG vs each of the other variables
    
    plt.figure(layout="tight", num="Relação entre MPG e as diferentes variáveis (características do carro)", figsize=(10,6))
    for i in range(COMP_VAR):
        create_plot(VAR_NAMES[i], VAR_NAMES[COMP_VAR], DATA[VAR_NAMES[i]], DATA[VAR_NAMES[COMP_VAR]], i + 1, COMP_VAR)
    plt.show()
    
    # Ex3: Convert all the data in matrix to uint16
    
    matrix_uint16 = MATRIX.astype(np.uint16) 
    
    # Ex4: Calculate occurrences
    
    alphabet, numberOccurrences = extractAlphabetCounts(matrix_uint16, LEN_VAR_NAMES)

    # Ex5: Plot bars
    
    for i in range (COMP_VAR):
        create_plot_bar(alphabet[i], numberOccurrences[i], VAR_NAMES[i])

    # Ex6: apply binning to some variables
    
    for variavel, step in [('Weight', 40), ('Displacement', 5), ('Horsepower', 5)]:
        idx = VAR_NAMES.index(variavel)
        matrix_uint16 = binning(matrix_uint16, step, idx)
    
    alphabet, numberOccurrences = extractAlphabetCounts(matrix_uint16, LEN_VAR_NAMES)
    for variavel in ['Weight', 'Displacement', 'Horsepower']:
        idx = VAR_NAMES.index(variavel)
        create_plot_bar(alphabet[idx], numberOccurrences[idx], variavel)

    # Ex7: calculate entrophy
    
    p = [None] * LEN_VAR_NAMES
    print("Valor médio (teórico) de bits por símbolo:")
    
    for i in range (LEN_VAR_NAMES):
        # Calcular a probabilidade de cada símbolo
        p[i] = numberOccurrences[i] / np.sum(numberOccurrences[i])
        
        entropia = calcularEntropia(p[i])
        print(f"H{VAR_NAMES[i][:3]}= {entropia}")

    # Ex8: Huffman coding - número médio de bits por símbolo
    
    print("\nNúmero médio de bits por símbolo e variância ponderada dos comprimentos:")
    for i in range(LEN_VAR_NAMES):
        comprimento_medio, variancia = huffman(matrix_uint16[:, i], p[i])
        print(f"L{VAR_NAMES[i][:3]}= {comprimento_medio} bits/simbolo, Var= {variancia:}")

    # Ex9: Correlação de Pearson

    print("\nCoeficiente de correlação:")
    pearson_values = correlacaoPearson(MATRIX, LEN_VAR_NAMES)
    for i in range(COMP_VAR):
        print(f"Correlação entre MPG e {VAR_NAMES[i]}: {pearson_values[i]:.3f}")
        
    # Ex10: Cálculo da Informação Mútua

    print("\nInformação mútua:")
    mi_values = [None] * (COMP_VAR)
    for i in range(COMP_VAR):
        x = matrix_uint16[:, i]
        y = matrix_uint16[:, -1]  # MPG
        mi_values[i] = informacaoMutua(x, y)
        print(f"MI entre MPG e {VAR_NAMES[i]}: {mi_values[i]:.4f}")
        
    #Ex11: Modelo de regressão linear para estimar MPG

    # Aplicar o modelo de regressão linear no conjunto de dados completo
    MPG_pred, mae, rmse = MPGpred(matrix_uint16, VAR_NAMES, matrix_uint16[:, VAR_NAMES.index('Acceleration')], matrix_uint16[:, VAR_NAMES.index('Weight')])
    print("\nMétricas de avaliação do modelo:")
    print(f"MAE = {mae}")
    print(f"RMSE = {rmse}")
    
    # Avaliar o modelo usando a média de aceleração
    media_accel = np.mean(matrix_uint16[:, VAR_NAMES.index("Acceleration")])
    MPG_pred_acc, mae_acc, rmse_acc = MPGpred(matrix_uint16, VAR_NAMES, media_accel, matrix_uint16[:, VAR_NAMES.index('Weight')])
    print("\nSubstituindo Acc pelo seu valor médio:")
    print(f"MAE = {mae_acc}")
    print(f"RMSE = {rmse_acc}")

    # Avaliar o modelo usando a média de peso
    media_weight = np.mean(matrix_uint16[:, VAR_NAMES.index("Weight")])
    MPG_pred_wght, mae_wght, rmse_wght = MPGpred(matrix_uint16, VAR_NAMES, matrix_uint16[:, VAR_NAMES.index('Acceleration')], media_weight)
    print("\nSubstituindo Weight pelo seu valor médio:")
    print(f"MAE = {mae_wght}")
    print(f"RMSE = {rmse_wght}")

if __name__ == "__main__":
    main()