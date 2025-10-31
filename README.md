# Relatório TP1 - Análise de Dados de Veículos

##### Trabalho realizado por:

- Bernardo Machado (2024223574)
- Carlos Oliveira (2024202355)
- Miguel Gaspar (2024208558)

## Índice

- [Resoluções](#resoluções)
  - [2.](#2)
    - [2.b) Análise dos gráficos de relação entre MPG e outras variáveis](#2b)
  - [7.](#7)
    - [7.c) Análise dos valores da entropia](#7c)
  - [8.](#8)
    - [8.c) Como e porquê reduzir a variância dos comprimentos dos códigos](#8c)
  - [10.](#10)
    - [10.b) Análise do Modelo de Regressão Linear](#10b)
  - [11.](#11)
    - [11.b) INSERT](#11b)
    - [11.f) INSERT](#11f)

## Resoluções

### 2.

#### 2.b)

Através da análise dos gráficos, podemos ver como o MPG (milhas por galão) se relaciona com diferentes características dos veículos. Primeiro, há uma relação positiva entre MPG e o Ano do Modelo. Isso indica que carros mais novos tendem a ser mais eficientes. Também é evidente a relação negativa entre MPG e peso, potência, cilindrada e número de cilindros indicando que veículos mais pesados com motores maiores e mais potentes geralmente têm menor eficiência de combustível, consumindo mais combustível por milha. De entre todos os fatores, o peso tem o efeito mais negativo sobre o MPG. Para a variável Aceleração, a relação com o MPG é ligeiramente positiva, sugerindo que o impacto direto da aceleração é menor no que toca à eficiência de combustível em comparação com os todos os outros fatores.

### 7.

#### 7.c)

### 8.

#### 8.c)

A variância dos comprimentos indica o quão diferentes são os tamanhos dos códigos atribuídos aos símbolos. Para reduzi-la, uniformizamos os comprimentos dos códigos, agrupamos símbolos semelhantes ou usamos códigos de comprimento quase fixo. Reduzir essa variância é importante porque torna a codificação mais previsível, facilitando a descodificação, mesmo que, eventualmente, reduza ligeiramente a eficiência média de compressão.

### 10.

#### 10.b)

A comparação entre os coeficientes de correlação e a informação mútua permite identificar as variáveis que mais influenciam o consumo de combustível. O coeficiente de correlação avalia apenas a relação linear entre as variáveis, enquanto que a informação mútua mede a dependência.
Observa-se que as variáveis Weight, Displacement, Horsepower e Cylinders apresentam maiores valores tanto na correlação quanto informação mútua, indicando que são as variáveis que influenciam mais o consumo de combustível.
Por outro lado, as variáveis Acceleration e ModelYear mostram correlações moderadas, mas também valores de informação mutua relevantes, o que sugere que estão relacionados ao consumo, embora essa relação não seja proporcional de forma constante, ou seja, não linear
Em resumo, a correlação de Pearson só capta dependências lineares, enquanto a informação mútua consegue identificar qualquer tipo de relação, linear ou não linear, proporcionando uma análise mais completa das variáveis que afetam o consumo de combustível.

### 11.

![Gráfico MPG](./guide/Comparação_entre_valores_reais_e_previstos_de_MPG.pdf)

#### 11.b)

#### 11.f)
