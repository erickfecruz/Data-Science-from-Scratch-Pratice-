#################################################################
########## Curso "Não Tão" Básico de Python - Parte 02 ##########
#################################################################

# Este código irá apresentar diversos subtemas sobre o aprendizado de programação 
# em Python. Não será apresentado um código baseado em um subtema em especifico, 
# como os apresentados no capitulo anterior.

## Programação Orientada a Objeto

# Para ilustrar a criação de classes em Python, iremos criar nossa propria classe conjunto
class Conjunto:
	
	# Construtor que pode receber valores ou não
	def __init__(self, values = None):
		
		# Inicia conjunto vazio
		self.dict = {}
		
		# Adicionar valores iniciais
		if values is not None:
			for i in values:
				self.adicionar(i)
	
	# Funcao adicionar
	def adicionar(self, valor):
		self.dict[valor] = True
	
	# Funcao verificar (verificar se a chave ja esta cadastrada)
	def verificar(self, valor):
		return valor in self.dict
		
	# Remover valor da lista
	def remover(self, valor):
		del self.dict[valor]
		
s = Conjunto([1,3,5])
print ("POO - Teste Classe Conjunto")
print ("Verificar 3: ",s.verificar(3))
print ("Verificar 4: ",s.verificar(4))
s.adicionar(4)
print ("Verificar 4: ",s.verificar(4))
s.remover(4)
print ("Verificar 4: ",s.verificar(4),"\n")

## Ferramentas Funcionais

# Podemos criar funções utilizando como parametro outras funções com valores parciais, como no exemplo abaixo:
def exp(base, power):
	return (base ** power)
	
def two_to_the(power):
	return (exp(2,power))

print("Ferramentas Funcionais")
print("two_to_the 3: ",two_to_the(3))

# Python possui a biblioteca functools.partial que apresenta ferramentas interessantes para realizarmos tal tarefa
from functools import partial
two_to_the = partial(exp,2)
print("two_to_the 3: ",two_to_the(3))

# Esse tipo de estrutura é muito util quando combinado com as funções map, filter, reduce, que serão mais utilizadas mais adiante
def double(x):
	return (x*2)

xs = [1, 2, 3, 4]
twice_xs = map(double, xs)
print("twice_xs: ",list(twice_xs))
list_double = partial(map, double)
twice_xs = list_double(xs)
print("twice_xs: ",list(twice_xs), "\n")
	
## Enumeração

# A função enumerate cria tuplas com os elementos de uma lista contendo os indices e seus respectivos valores
print("Enumerate")
vet = [2, 4, 5, 3, 3, 2, 3, 2, 1]
enum = enumerate(vet)
print(list(enum),"\n")

## Descompactação de ZIP e Argumentos

# Com a função ZIP podemos transformar multiplas listas em uma única lista de tuplas com os elementos correspondentes
print("Função ZIP em listas")
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
lfinal = zip(lista1, lista2)
print("l1: ", list(lista1),"\nl2: ",list(lista2),"\nzip(l1,l2): ",list(lfinal))

# Para descompactar uma lista basta colocar um * antes da lista e utilizar o mesmo comando zip
lzip = [('a',1),('b',2),('c',3)]
print("Descompactar: ",list(zip(*lzip)),"\n")

## args e kwargs

# Se tentarmos criar uma função de ordem alta, caso esta função possua mais de um argumento teremos problemas.
# Uma maneira de contornar este tipo de problema é utilizando os args e kwargs
def soma(x,y):
	return (x + y)

def dobrar_func(f):
	def g(*args, **kwargs):
		return 2 * f(*args, **kwargs)
	return g
	
dobra_soma = dobrar_func(soma)
print("Args e Kwargs")
print ("Dobrar soma de 2 + 3: ", dobra_soma(2,3))