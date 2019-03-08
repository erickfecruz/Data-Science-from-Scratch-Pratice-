#################################################################
############### Inicializar Base de Contas Pagas ################
#################################################################

# Base de dados inicial

experience_paid = [(0.7, "paid"), (1.9, "unpaid"), (2.5, "paid"), (4.2, "unpaid"), (6, "unpaid"),
				   (6.5, "unpaid"), (7.5, "unpaid"), (8.1, "unpaid"), (8.7, "paid"), (10, "paid")]
						
print("Base de dados inicial:")
print(experience_paid, "\n")

# Neste momento ainda não foi abordado uma forma mais adequada de realizar
# um corte para definir um valor mais adequado para dividir duas classes da 
# base de dados, desta forma foi feita uma função para classificar as amostras
# a partir de uma breve análise visual.

def predict_paid(experience):
	if experience < 3:
		return "paid"
	elif experience < 8.5:
		return "unpaid"
	else :
		return "paid"

# Vamos calcular a taxa de acerto dos cortes sugeridos

count = 0
for experience, paid in experience_paid:
	if predict_paid(experience) == paid:
		count = count + 1
		
successes = count / len(experience_paid)

print("Taxa de acertos:")
print(successes*100, "%\n")