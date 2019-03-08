#################################################################
############# Inicializar base de dados de usuários #############
#################################################################

users = {
	0 : "Hero",
	1 : "Dunn",
	2 : "Sue",
	3 : "Chi",
	4 : "Thor",
	5 : "Clive",
	6 : "Hicks",
	7 : "Devin",
	8 : "Kate",
	9 : "Klein"
}
	
#################################################################
################## Adicionar lista de amizades ##################
#################################################################

# Inicializar losta de pares de amizade por ID

friendship = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

# Criar uma lista de listas, contendo os amigos de cada usuários

listUsers = []
for user in users:
	user = []
	listUsers.append(user)
	
for i, j in friendship:
	listUsers[i].append(users[j])
	listUsers[j].append(users[i])
	
#Teste para verificar se a lista está montada corretamente
	
print("Lista de amigos de cada usuário: ")
print(listUsers,"\n")

# Quantidade de amigos de um usuário

def number_of_friends(id):
	return len(listUsers[id])
	
# Quantidade de amigos usuário 0

print("Quantidade de amigos do usuário 0: ")
print(number_of_friends(0),"\n")

# Quantidade de amigos no total

totalFriends = sum(number_of_friends(user) for user in users)
print("Quantidade de amigos no total: ")
print(totalFriends,"\n")

# Média de amigos por usuário

meanFriends = totalFriends / len(listUsers)
print("Media de amigos por usuario: ")
print(meanFriends,"\n")

# Ordenar usuário pela quantidade de amigos de forma decrescente em formato de tupla (index, quantidade)

def order_friends_quantity():
	orderFriendlist = []
	idx = 0
	for x in listUsers :
		orderFriendlist.append((idx,len(x)))
		idx = idx+1
	
	orderFriendlist.sort(key=lambda a: a[1], reverse = True)
	nameOrderFriendlist = list(map(lambda x: (users[x[0]],x[1]), orderFriendlist))
	return nameOrderFriendlist
	
print("Usuarios ordenados pela quantidade de amigos:")
print(order_friends_quantity(), "\n")

# Listar amigos de amigos e somar repetição de sugestões, além de ordenar 

# Criar lista de relacionamentos por index

def list_of_index():
	
	listIdx = []
	for user in users:
		user = []
		listIdx.append(user)
	
	for i, j in friendship:
		listIdx[i].append(j)
		listIdx[j].append(i)
		
	return listIdx
	
lista = list_of_index()
		
# Verificar se existe um amigo em comum		
		
def not_already_friend(idx1,idx2, lista):
	
	for aux in lista[idx1]:
		if aux == idx2:
			return False
					
	return True;

def friends_of_friends(idx, lista):	
	
	fof = []
	for friend in lista[idx]:
		for ff in lista[friend]:
			if ((ff != idx) and (not_already_friend(ff,idx, lista))):
				fof.append(ff)
		

	fof = list(map(lambda x:(x,fof.count(x)),fof))
	fof = list(dict.fromkeys(fof))
	fof.sort(key=lambda a: a[1], reverse = True)
	fof = list(map(lambda x: (users[x[0]],x[1]), fof))
	return fof

print("Recomendacao de amigos para o usuario 3 em ordem crescente: ")
print(friends_of_friends(3, lista),"\n")

#################################################################
################# Adicionar lista de interesses #################
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
			 

from collections import defaultdict			 

# Criar keys para cada interesse que retorna uma lista de IDs

user_id_int = defaultdict(list)

for (id, interest) in interests:
	user_id_int[interest].append(id)

print("Lista de IDs por interesse: ")
print(user_id_int, "\n")

# Criar keys para cada ID que retorna uma lista de interesses

user_int_id = defaultdict(list)

for (id, interest) in interests:
	user_int_id[id].append(interest)

print("Lista de interesses por ID: ")
print(user_int_id, "\n")