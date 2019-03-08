#################################################################
############ Inicializar base de dados de interesses ############
#################################################################

# Adicionar interesses

interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
			 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
			 (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
			 (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
			 (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
			 (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
			 (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
			 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
			 (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
			 (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")]
			 

# O objetivo do presente código é inicialmente colocar todas as palavras em letras minusculas
# e realizar uma contagem sobre a frequencia de vezes que cada palavra aparece (neste exemplo
# serão separadas as strings que contém mais de uma palavra juntas.

from collections import Counter

words_to_lower_case = Counter(word
	for user, int in interests
	for word in int.lower().split())
	
print("Contagem de palavras na base de dados:")
print(words_to_lower_case, "\n")

# Vamos agora retornar uma lista com os valores mais frequentes a partir de uma valor 'n' de repetições

def commom_words(n, lista):
	for word in lista:
		if lista[word] >= n:
			print (word, lista[word])
			
print("Palavras com 2 ou mais ocorrencias:")
commom_words(2,words_to_lower_case)

print("\nPalavras com 3 ou mais ocorrencias:")
commom_words(3,words_to_lower_case)



