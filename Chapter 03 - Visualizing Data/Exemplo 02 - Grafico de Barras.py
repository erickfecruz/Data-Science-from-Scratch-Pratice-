# -*- encoding: utf-8 -*-

#################################################################
######## Introdu�ao a Biblioteca matplotlib - Exemplo 01 ########
#################################################################

## Gr�fico de Barras

## Grafico 01

# Neste primeiro exemplo ser� demonstrado como utilizar a biblioteca matplotlib para gerar alguns gr�ficos de barras
# Inicialmente vamos importar a biblioteca
from matplotlib import pyplot as plt

# Inicializar vetor com filmes e vetor numero de oscars
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
 
#Gerar um grafico de barra em com as coordenadas e numero de oscars
plt.bar(movies, num_oscars)

# Colocar t�tulo e rotulo no eixo X e Y
plt.title("Filmes Favoritos X Premiacoes")
plt.xlabel("Meus Filmes Favoritos")
plt.ylabel("Numero de Premiacoes")

# Nomear no eixo X com os nomes dos filmes
plt.xticks(movies)

# Salvar o gr�fico gerado no nome de "Fig02.png"
plt.savefig("Fig02.png")

# Mostrar o gr�fico na tela
plt.show() 

## Grafico 02

from collections import Counter
# Neste segundo exemplo vamos criar um histograma com o gr�fico de barras
# Vamos inicializar o vetor de notas
notas = [83, 95, 91, 87, 70, 0 , 85, 82, 100, 67, 73, 77, 0]

# Vamos arredondar as notas e agrupar em grupos de 10 em 10, sendo que iremos arredondar sempre para baixo, ou seja,
# caso o n�mero seja 79 ele ser� agrupado com o grupo de 70
decile = lambda nota: nota // 10 * 10
histogram = Counter(decile(nota) for nota in notas)

# Plotar o grafico com os valores das chaves e valores e o tamanho da barra ser� de 8 unidades
plt.bar([x for x in histogram.keys()],
		 histogram.values(),
		 8)
		 
# Para centralizarmos os valores do gr�fico iremos aumentar o tamanho dos eixos em 5 unidades
plt.axis([-5, 105, 0, 5])

# Colocar os valores no eixo x de 0 at� 10
plt.xticks([10 * i for i in range(11)])

# Colocar t�tulo e rotulo no eixo X e Y
plt.title("Distribuicao de Notas")
plt.xlabel("Notas")
plt.ylabel("Numero de Alunos")

# Salvar o gr�fico gerado no nome de "Fig03.png"
plt.savefig("Fig03.png")

# Mostrar o gr�fico na tela
plt.show() 

## Grafico 03
