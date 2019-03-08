#################################################################
########### Inicializar base de salario e experiencia ###########
#################################################################

# Base de dados inicial

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5),
						(76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]
						
print("Base de dados inicial:")
print(salaries_and_tenures, "\n")

from collections import defaultdict

# Média salarial por ano de experiencia (utilizando intervalos de tempo)

def tenure_bucket(tenure):
	if tenure < 2:
		return "Nivel Trainee"
	elif tenure < 5:
		return "Nivel Junior"
	else :
		return "Nivel Pleno"

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure_bucket(tenure)].append(salary)

average_salary_by_tenure = {
	tenure : sum(salaries) / len(salaries)
	for tenure, salaries in salary_by_tenure.items()
}

print("Media salarial por nivel de experiencia")
print(average_salary_by_tenure, "\n")