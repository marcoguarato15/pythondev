import statistics
st = statistics

## 1 - Aplicando a Média 
# também possui 
# geometric_mean e harmonic_mean
print("Média de [3, 2, 3, 8, 9]é: ",st.mean([3, 2, 3, 8, 9])) # 25 / 5 = 5

## 2 - Aplicando a mediana
# median_group, median_high, median_low
print("Mediana de [1, 2, 4, 8, 9, 10]: é:", st.median([1, 2, 4, 8, 9, 100]))

## 3 - Aplicando a moda (valor que mais se repete)
print("A moda de [1, 2, 2, 4, 4, 4, 4, 3, 3, 3] é:",st.mode([1, 2, 2, 4, 4, 4, 4, 3, 3, 3]))

## 4 - Desvio padrão
# Quanto mais próximo de 0 o resultado for, menos dispersos os valores do conjunto passado está
print("Desvio padrão de [1, 1.5, 2, 5] é:", st.stdev([1, 1.5, 2, 5]))

# st.kde() # kernel density estimation (KDE (estatística) em portugues)
# st.variance() # Variância