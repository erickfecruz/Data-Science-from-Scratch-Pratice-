# -*- encoding: utf-8 -*-

#################################################################
######## Introdu�ao a Biblioteca matplotlib - Exemplo 01 ########
#################################################################

## Gr�fico Simples

# Neste primeiro exemplo ser� demonstrado como utilizar a biblioteca matplotlib para gerar um gr�fico simples
# Inicialmente vamos importar a biblioteca
from matplotlib import pyplot as plt

# Inicializar vetor com anos e vetor com PIB
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Plotar gr�gico com anos relacionado com o pib
# A cor da linha do gr�fico gerado ser� verde e ser� uma linha continua
# Nos pontos onde est?o os pontos so vetor ser� posta uma marca�?o 'o'
plt.plot(years, pib, color='green', marker='o',linestyle='solid')

# Colocar t�tulo no gr�fico
plt.title("Produto Interno Bruto")

# O eixo Y ser� rotulado com o comando ylabel
plt.ylabel("Bilhoes de $")

# Salvar o gr�fico gerado no nome de "Fig01.png"
plt.savefig("Fig01.png")

# Mostrar o gr�fico na tela
plt.show()