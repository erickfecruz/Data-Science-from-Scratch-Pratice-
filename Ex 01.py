# Inicializar base de dados de usuários

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

