# -*- encoding: utf-8 -*-

#################################################################
######## Introduçao a Biblioteca matplotlib - Exemplo 01 ########
#################################################################

## Gráfico Simples

# Neste primeiro exemplo será demonstrado como utilizar a biblioteca matplotlib para gerar um gráfico simples
# Inicialmente vamos importar a biblioteca
from matplotlib import pyplot as plt

# Inicializar vetor com anos e vetor com PIB
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Plotar grágico com anos relacionado com o pib
# A cor da linha do gráfico gerado será verde e será uma linha continua
# Nos pontos onde est?o os pontos so vetor será posta uma marcaç?o 'o'
plt.plot(years, pib, color='green', marker='o',linestyle='solid')

# Colocar título no gráfico
plt.title("Produto Interno Bruto")

# O eixo Y será rotulado com o comando ylabel
plt.ylabel("Bilhoes de $")

# Salvar o gráfico gerado no nome de "Fig01.png"
plt.savefig("Fig01.png")

# Mostrar o gráfico na tela
plt.show()