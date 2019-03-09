#################################################################
########## Curso "Não Tão" Básico de Python - Parte 01 ##########
#################################################################

# Este código irá apresentar diversos subtemas sobre o aprendizado de programação 
# em Python. Não será apresentado um código baseado em um subtema em especifico, 
# como os apresentados no capitulo anterior.

## Ordenação

# Em Python é possível ordenar uma lista utilizando a função sort()
print("Testes de ordenacao:")
x = [4, 2, 3, 1]
x.sort()
print(x)

# Por default a lista será ordenada em ordem crescente, porém podemos inverter o padrão utilizando o parametro reverse = True
y = [4, 2, 3, 1]
y.sort(reverse = True)
print (y) 

# Além do parametro anterior podemos utilizar o parametro key, que permite criarmos uma função que será utilizada omo base para a
# ordenação dos elementos. No exemplo abaixo será utilizada a função abs para compararmos com o valor absoluto dos números da lista
z = [-2, 1, -4, 3]
z.sort(key = abs)
print(z,"\n")

## Compreensões de Lista

# Podemos transforma uma lista em outra transformando os elementos da lista em outros, selecionando alguns deles ou aplicando uma 
# combinação dos dois métodos. Uma das maneiras de realizar isso pode ser vista no exemplo a seguir:
print("Exemplos de compreensoes de listas:")
even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)
square_number = [x * x for x in range(5)] 
print (square_number, "\n")

# Além de listas, esse processo pode ser realizado em dicionários e conjuntos. 

## Geradores e Iteradores

# Os geradores permitem que iteremos uma lista de forma preguiçosa, desta forma podemos acessar apenas os valores que desejamos mesmo
# em uma lista muito grande. Visualmente o resultado é o mesmo, porém a maior mudança se encontra no processamento
print("Exemplo de geradores e iteradores:")
def odd_num(num):
	for i in num:
		if i % 2:
			yield i	
		
for x in odd_num(range(10)):
	print(x)
	
print()

## Aleatoriedade

print("Aleatoriedade:")
# A biblioteca random fornece uma serie de funções de aleatoriedade, que por sua vez são muito utéis em Data Science
import random

# A função abaixo gera um número aleatório entre 0 e 1
x = random.random()
print (x)

# Podemos determinar uma seed para nossa função de aleatoriedade, podendo assim refazer um teste com os mesmos resultados
random.seed(10)
x = random.random()
print (x)

# A função randrange fornece um número aleatório inteiro
x = random.randrange(10)
print (x)

# A função shuffle embaralha os elementos de uma lista
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(x)
print (x)

# Para obter elementos aleatoriamente de uma lista podemos utilizar o choice e o sample. A diferença entre eles é que o 
# choice seleciona apenas um elemento da lista, já o sample escolhe n elementos da lista.
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = random.sample(x, 9)
print (y)
y = random.choice(x)
print (y, "\n")

## Expressões Regulares

import re

# Expressoes regulares fornecem uma maneira de procurar informações em um texto
print("Expressoes Regulares:")
x = re.match("a","cat") # Verificar se cat começa com a
x = re.search("a","cat") # Verificar se cat contém a
x = re.split("[ab]", "carbs") # Separar string em a e b
print(x)
x = re.sub("[ab]","-","carbs") # Substituir a e b por -
print(x)
