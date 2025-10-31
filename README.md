# Relatório TP1 - Análise de Dados de Veículos

### Trabalho realizado por:

- Bernardo Machado (Número de Estudante: 2024223574)
- Carlos Oliveira (Número de Estudante: 2024202355)
- Miguel Gaspar (Número de Estudante: 2024208558)

## Índice

- [Resoluções](#resoluções)
  - [2.b) Análise dos gráficos de relação entre MPG e outras variáveis](#2b)
  - [7.c) Análise dos valores da entropia](#7c)
  - [8.c) Como e porquê reduzir a variância dos comprimentos dos códigos](#8c)
  - [10.b) Análise do Modelo de Regressão Linear](#10b)
  - [11.b) INSERT](#11b)
  - [11.f) INSERT](#11f)

## Resoluções

### 2.b)

Através da análise dos gráficos, podemos observar como o MPG (milhas por galão) se relaciona com diferentes características dos veículos. Primeiro, há uma relação positiva entre MPG e o Ano do Modelo indicando que carros mais novos tendem a ser mais eficientes. De seguida é evidente a relação negativa entre MPG e, peso, potência, cilindrada e número de cilindros indicando que veículos mais pesados e/ou com motores maiores e/ou mais potentes geralmente têm menor eficiência de combustível, consumindo mais combustível por milha. De entre todos os fatores, o peso tem o efeito mais negativo sobre o MPG. Para a variável Aceleração, a relação com o MPG é ligeiramente positiva, sugerindo que o impacto direto na eficiência de combustível da aceleração é menor em comparação com os todos os outros fatores.

### 7.c)

### 8.c)

A variância dos comprimentos indica o quão diferentes são os tamanhos dos códigos atribuídos aos símbolos. Para reduzi-la, uniformizamos os comprimentos dos códigos, agrupamos símbolos semelhantes ou usamos códigos de comprimento quase fixo. Reduzir essa variância é importante porque torna a codificação mais previsível, facilitando a descodificação, mesmo que, eventualmente, reduza ligeiramente a eficiência média de compressão.

### 10.b)

A comparação entre os coeficientes de correlação e a informação mútua permite identificar as variáveis que mais influenciam o consumo de combustível. O coeficiente de correlação avalia apenas a relação linear entre as variáveis, enquanto que a informação mútua mede a dependência.
Observa-se que as variáveis Weight, Displacement, Horsepower e Cylinders apresentam maiores valores tanto na correlação quanto informação mútua, indicando que são as variáveis que influenciam mais o consumo de combustível.
Por outro lado, as variáveis Acceleration e ModelYear mostram correlações moderadas, mas também valores de informação mutua relevantes, o que sugere que estão relacionados ao consumo, embora essa relação não seja proporcional de forma constante, ou seja, não linear
Em resumo, a correlação de Pearson só capta dependências lineares, enquanto a informação mútua consegue identificar qualquer tipo de relação, linear ou não linear, proporcionando uma análise mais completa das variáveis que afetam o consumo de combustível.

### 11.b)

### 11.f)

![Gráfico Comparação MPG Real Vs. MPG Previsto](./guide/MPG%20Real%20Vs.%20MPG%20Previsto.jpg)

<img src="./guide/MPG%20Real%20Vs.%20MPG%20Previsto.jpg" alt="Gráficos MPG" width="600">
