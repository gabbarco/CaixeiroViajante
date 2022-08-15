from random import randint

INT_MAX = 2147483647
# Número de cidades
V = 6

# Nomes dos nódulos
GENES = "ABCDEF"

# Nódulo inicial
START=0

POP_SIZE = 10

# Estrutura do genoma
# Define o caminho percorrido
# pelo caixeiro enquanto o melhor valor
# do caminho é armazenado


class individual:
	def __init__(self) -> None:
		self.gnome = ""
		self.fitness = 0

	def __lt__(self, other):
		return self.fitness < other.fitness

	def __gt__(self, other):
		return self.fitness > other.fitness


# Função para retornar número aleatório
def rand_num(start, end):
	return randint(start, end-1)


# Função para verificar cidades repetidas
def repeat(s, ch):
	for i in range(len(s)):
		if s[i] == ch:
			return True

	return False


# Função para retornar um genoma mutado
# Genoma mutado é uma string
# Com mudanças aleatórias entre dois genes para aumentar a
# variação de resultados 
def mutatedGene(gnome):
	gnome = list(gnome)
	while True:
		r = rand_num(1, V)
		r1 = rand_num(1, V)
		if r1 != r:
			temp = gnome[r]
			gnome[r] = gnome[r1]
			gnome[r1] = temp
			break
	return ''.join(gnome)


# Função para retornar um genoma valido
def create_gnome():
	gnome = "0"
	while True:
		if len(gnome) == V:
			gnome += gnome[0]
			break

		temp = rand_num(1, V)
		if not repeat(gnome, chr(temp + 48)):
			gnome += chr(temp + 48)

	return gnome


# Função para retornar o melhor valor para o genoma
# O melhor valor é o caminho menor do genoma representado
def cal_fitness(gnome):
	mp = [
		[0, 60, INT_MAX, 120, 50, 60],
		[60, 0, 50, INT_MAX, 100, 25],
		[INT_MAX, 50, 0, 70, 100, 25],
		[120, INT_MAX, 70, 0, 80, 75],
		[50, 100, 100, 80, 0, 75],
    [60, 25, 25, 75, 75, 0],
	]
	f = 0
	for i in range(len(gnome) - 1):
		if mp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48] == INT_MAX:
			return INT_MAX
		f += mp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48]

	return f


# Função para retornar o valor atualizado
def cooldown(temp):
	return (90 * temp) / 100



# Função para o TSP(traveling salesman problem)
def TSPUtil(mp):
	# Número de geração
	gen = 1
	# Número de árvores interações entre os genes
	gen_thres = 5

	population = []
	temp = individual()

	for i in range(POP_SIZE):
		temp.gnome = create_gnome()
		temp.fitness = cal_fitness(temp.gnome)
		population.append(temp)

	print("\nGENOMA	 VALOR\n")
	for i in range(POP_SIZE):
		print(population[i].gnome, population[i].fitness)
	print()

	temperature = 10000

	# Iteração para melhorar a mutação dos genes
	while temperature > 1000 and gen <= gen_thres:
		population.sort()
		print("\nCurrent temp: ", temperature)
		new_population = []

		for i in range(POP_SIZE):
			p1 = population[i]

			while True:
				new_g = mutatedGene(p1.gnome)
				new_gnome = individual()
				new_gnome.gnome = new_g
				new_gnome.fitness = cal_fitness(new_gnome.gnome)

				if new_gnome.fitness <= population[i].fitness:
					new_population.append(new_gnome)
					break

				else:

					# Aceitando combinações rejeitadas para mutar e criar
          # novas possíveis combinações
					prob = pow(
						2.7,
						-1
						* (
							(float)(new_gnome.fitness - population[i].fitness)
							/ temperature
						),
					)
					if prob > 0.5:
						new_population.append(new_gnome)
						break

		temperature = cooldown(temperature)
		population = new_population
		print("Geração", gen)
		print("GENOMA	 VALOR")

		for i in range(POP_SIZE):
			print(population[i].gnome, population[i].fitness)
		gen += 1


if __name__ == "__main__":
  #ordem do mp [grafo 0, grafo 1, grafo 2, grafo 3, grafo 4]
  #int_max significa que não se ligam
	mp = [
		[0, 60, INT_MAX, 120, 50, 60],
		[60, 0, 50, INT_MAX, 100, 25],
		[INT_MAX, 50, 0, 70, 100, 25],
		[120, INT_MAX, 70, 0, 80, 75],
		[50, 100, 100, 80, 0, 75],
    [60, 25, 25, 75, 75, 0],
	]
	TSPUtil(mp)

  #Diferente do modo de força bruta esse calcula a volta ao 
  #vértice inicial