#################################################################
############### Curso Básico de Python - Parte 02 ###############
#################################################################

# Este código irá apresentar diversos subtemas sobre o aprendizado de programação 
# em Python. Não será apresentado um código baseado em um subtema em especifico, 
# como os apresentados no capitulo anterior.

## Listas

# As listas em python apresentam algumas propriedades especiais, como o fato de podermos criar facilmente
# arrays com diferentes tipos de elementos e até mesmo uma lista de listas, como mostrado abaixo:
integer_list = [1, 2, 3]
heterogeneous_list = [1, "ola", True]
list_of_lists = [integer_list, heterogeneous_list]

# Agora algumas maneias de obter os valores de uma lista
x = range(10) # Lista de 0 a 9
print("x[0] = ",x[0])
print("x[1] = ",x[1])
print("x[-1] = ",x[-1])
print("x[-2] = ",x[-2])

# Existem outras formas de retornar os valores das listas como:
print("x[:3] = ",x[:3])
print("x[3:] = ",x[3:])
print("x[1:5] = ",x[1:5])
print("x[-3:] = ",x[-3:], "\n")

# Verificar se um elemento está na lista
print(1 in [1, 2, 3])
print(4 in [1, 2, 3], "\n")

# Formas de adicionar um elemento a uma lista:
x1 = [1, 2, 3]
x1.extend([4, 5, 6])

x2 = [1, 2, 3]
x2.append(0)

## Tuplas

# Para gerar um tupla basta colocar dois elementos separados por uma virgula entre colchetes (Ou sem o colchetes)
tuple = (1, 2)

# As tuplas são muito parecidas com as listas, porém não é possível modificar uma tupla, como visto a seguir
try:
	tuple[1] = 4
except TypeError:
	print ("Não pode se modificar uma tupla \n")

## Dicionários

# Os dicionários são estruturas que possuem uma chave única e um valor correspondente a ela. Ele pode ser
# utilizado para conseguir recuperar rapidamente o valor correspondente a chave que outros métodos encontrados
empty_dict = {}
other_dict = {"Erick" : 30, "Roger" : 25}
print("Valor da chave 'Erick': ", other_dict["Erick"],"\n")

# Perguntar se existe uma chave no dicionário
print("'Roger' é uma chave? ","Roger" in other_dict, "\n")

# Para adicionar uma nova chave basta declarar da seguinte forma:
other_dict["Teste"] = 25

# Para visualizar as informações do dicionário temos os seguintes métodos:
print("Chaves: ", other_dict.keys())
print("Valores: ", other_dict.values())
print("Itens: ", other_dict.items(), "\n")

## defaultdict

# Um defaultdict é uma variação do dicionário mostrado anteriormente, porém ao tentar acessar uma chave que ainda não 
# existe no dicionário, ela cria um valor default previsamente criado pelo usuário
from collections import defaultdict
str_dd = "a b c d e a c a d"
word_count = defaultdict(int)
for word in str_dd:
	word_count[word] += 1
	
print(word_count.items(), "\n")

## Contador

# O contador auxilia quando queremos contar a frequência de repetição de elementos em uma lista e estuturas semelhantes
from collections import Counter
c = Counter(str_dd)
print(c, "\n")

# O contador apresenta a função most_common(n) que retorna os 'n' elementos com maior frequencia
print("Most Commom 3: ", c.most_common(3), "\n")

## Conjuntos

# Os conjuntos é um estrutura que possuem elementos distintos
s = set()
s.add(1)
s.add(2)
s.add(2)
print("Tamanho do conjunto ", len(s))

# Para checar se um elemento está no conjunto temos a operação 'in', que é uma operação muito eficiente
print("2 está no conjunto? ", 2 in s, "\n")

## Controle de Fluxo

# O laço 'for' possui os comandos 'continue' e 'break' que controlam o fluxo de execução do programa, como podemos ver no exemplo abaixo
for x in range(10):
	if x == 3:
		continue
	if x == 5:
		break
	print (x)