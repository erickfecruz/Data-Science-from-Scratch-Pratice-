#################################################################
############### Curso Básico de Python - Parte 01 ###############
#################################################################

# Este código irá apresentar diversos subtemas sobre o aprendizado de programação 
# em Python. Não será apresentado um código baseado em um subtema em especifico, 
# como os apresentados no capitulo anterior.

## Formatação de Espaços em Branco

for i in [1, 2, 3, 4, 5]: 
	print ("i: ", i)
	for j in [1, 2, 3, 4, 5]:
		print ("j: ", j)
		print ("i + j: ", i + j)
	print ("i: ", i)
print ("Done Looping")

# Os espaços em branco dentro dos parenteses e colchetes são ignorados, facilitando assim
# uma melhor organização visual dos elementos para facilitar a leitura do código.
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 +
						   11 + 12 + 13 + 14 + 15)
					
# Outro exemplo com uma lista de listas
lista_de_listas = [ [1, 2, 3],
					[4, 5, 6],
					[7, 8, 9] ]
					
## Módulos

#import re
import re
my_regex = re.compile("[0-9]+", re.I)

# Importar módulo utilizando um alias
import matplotlib.pyplot as plt

# É possível importar uma sessão especifica de um módulo
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# Cuidado ao importar módulos inteiros pois podem conter váriaveis iguais as utilizadas no projeto anteriormente
match = 10
from re import *
print (match)

## Aritmética

# Divisão de números reais
print("5/2: ", 5/2)

# Divisão de números inteiros
print("5//2: ", 5//2)

## Funções

# Função para dobrar valor
def double(n):
	return (n*2)
	
print("Dobro de 3: ",double(3), "\n")

# É possível passar uma função como argumento, como no exemplo abaixo
def use_function_in_2(func):
	return (func(2))
	
print("Aplicar dobro em 2: ", use_function_in_2(double), "\n")

# Uma função especial que podemos utilizar é a função lambda, ela permite utilizarmos uma pequena função anonima
print("Função anonima para triplicar valor: ",use_function_in_2(lambda x: x * 3),"\n")

# Função com valor default
def default_function(message = "default function"):
	print(message)
	
print("Mensagem default: ")
default_function()
print("Mensagem hello world ")
default_function("Hello World\n")

## Strings

# Existem duas formas que podemos criar uma String, com aspas duplas e com aspas simples
str1 = 'Hello World'
str2 = "Hello World"

# Uma String de múltiplas linhas pode ser criada por 3 aspas simples ou duplas
multstr = """Linha 01
Linha 02
Linha 03\n"""

print(multstr)

## Exceções

# Também é possível tratar as exceções que acontecem no Python, como no exemplo a seguir
try:
	print (0 / 0)
except ZeroDivisionError:
	print ("Cannot Divide by Zero")






