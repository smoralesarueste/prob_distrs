

from .Node import Node

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
			The relative weight of each element. Dont have to be normalized. Should be in the same order as values. 
		
		"""

		if len(values) == 0: return None

		# Initializing the tree
		val, wei = values.pop(), weights.pop()
		self.root = Node(value = val, weight = wei)

		# Iterating to populate it
		while len(values) > 0:
			val, wei = values.pop(), weights.pop()
			self.root.add_value(value = val, weight = wei)

	def describe(self):
		"""
		Prints all the nodes that are part of the tree, in order of apparience. 

		Arguments
		------------
		depth: int >= 0
			Keeps track of how many levels down this node is with respect to the root

		"""
		self.root.describe(depth = 0)

	def get_samples(self, n = 1): 
		"""
		Get n samples from the tree using the relative weights as probabilities. 

		Arguments
		------------
		n: int >= 1
			Number of samples to get. Default value of 0. 
		
		Returns
		------------
		list
			Containing the n values sampled

		"""
		return self.root.get_samples(n)

		
