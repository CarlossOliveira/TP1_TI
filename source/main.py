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
    plt.bar(alphabet, numberOccurrences, color='red', align= "center") #alphabet_str = alphabet.astype(str) 25.0 -> 25 mas estraga os outros graficos
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
    
    
def binning(list_num, alphabet, numberOccurrences, step, index):
    min_interval = np.min(list_num)
    limite = np.max(list_num)
    max_interval = min_interval + step

    list_binning = list_num.copy()
    
    
    while min_interval <= limite:
        # Máscara para valores no intervalo atual
        mask = (list_binning >= min_interval) & (list_binning <= max_interval)

        # Obter alfabeto e ocorrências no intervalo
        mask_alphabet = (alphabet[index] >= min_interval) & (alphabet[index] <= max_interval)
        alphabet_filtrado = alphabet[index][mask_alphabet]
        ocorrencias_filtradas = numberOccurrences[index][mask_alphabet]

        # Determinar valor de substituição
        if len(ocorrencias_filtradas) == 0:
            replacement_value = min_interval  # valor padrão
        else:
            idx_max = np.argmax(ocorrencias_filtradas)
            replacement_value = alphabet_filtrado[idx_max]

        # Aplicar substituição
        list_binning[mask] = replacement_value

        # Avançar intervalo
        min_interval = max_interval + 1
        max_interval = min_interval + step
        
    return list_binning
        
def mudar_coluna(matriz, coluna, n_col):
    matriz[:, n_col] = coluna
    return matriz
    
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

    for i in range(1):
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