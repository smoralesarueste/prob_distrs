

from Node import Node

class BinaryTree: 
	"""
	Class that generates a balanced binary tree for the states of a finete discrete distribution. 
	Useful for sampling a FineteDiscrete in O(log n)
	"""

	def __init__(self, values, weights): 
		"""
		Generates the binary tree. 

		Arguments
		------------
		values: list
			List of possible values in the support
		weights: list
			The relative weight of each element. Dont have to be normalized. 
		
		"""
		self.root = None




from collections import Counter

import time
import random
import numpy as np


n_samples = int(1e9)
n_states = int(100_000)


print("Using Node: \n")

start_time = time.perf_counter()
n = Node(value = 1, weight = 1)
for i in range(2, n_states + 1):
	n.add_value(value = i, weight = 1) #i**0)
end_time = time.perf_counter()
total_time = end_time - start_time
print(f"Building time: {total_time:.3f}")



start_time = time.perf_counter()
samples = n.get_samples(n = n_samples)
end_time = time.perf_counter()
total_time = end_time - start_time
print(f"Using binomial: {total_time:.3f}")

"""
print("\n"*4)


print("Using random choices: \n")

values = np.array([i for i in range(n_states)])
weights = np.array([i**3 for i in range(n_states)])
weights = weights / weights.sum()

start_time = time.perf_counter()
samples = random.choices(population = values, weights = weights, k = int(N))
end_time = time.perf_counter()
total_time = end_time - start_time
print(f"Using random: {total_time:.3f}")


"""














