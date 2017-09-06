import random as r

GENERATIONS = 100
POP_SIZE = 25
GENOME_SIZE = 8

""" The function that will be maximized. """
def fit_func( x ):
	return -1*(x - 10)*(x - 100)+200

def main():
	pop = build_random_pop(POP_SIZE)
	print("initial population:")
	print_pop(pop)

	for g in range(GENERATIONS):
		# Evaluate
		for i in pop:
			i.fitness = evaluate( i.genome, fit_func )

		# Select/Operate
		new_pop = []
		for i in range(0, POP_SIZE/2):
			# Approximation of roulette wheel selection 
			sorted_pop = sorted(pop, key=lambda ind : max(1, ind.fitness)*r.random() )
			new_pop += crossover( sorted_pop[-1].genome, sorted_pop[-2].genome )

		pop = new_pop
	print("final:")
	print_pop(pop)

def build_random_pop( size ):
	ret = []
	for i in range(0, size):
		ret.append(random_individual())
	return ret

def random_individual():
	# binary representation of a random in, trimmed the 0b, and zero padded. 
	return Individual(bin(r.randint(0,2**GENOME_SIZE-1))[2:].zfill(GENOME_SIZE))

def evaluate( g, func ):
	return func( int(g, 2) )

def crossover(p1, p2):
	crossover_point = r.randint(0, GENOME_SIZE-1)
	c1_genome = p1[:crossover_point]+p2[crossover_point:]
	c2_genome = p2[:crossover_point]+p1[crossover_point:]
	return [Individual(c1_genome), Individual(c2_genome)]

def print_pop(pop):
	for p in pop:
		p.fitness = evaluate(p.genome, fit_func)
		print( p )

class Individual:
	def __init__(self, g):
		self.genome = g
		self.fitness = 0

	def __str__(self):
		return "{}, {}, {}".format(self.genome, int(self.genome, 2), self.fitness)

if __name__ == "__main__":
	main()