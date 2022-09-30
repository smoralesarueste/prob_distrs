

import copy
import numpy as np


class Node: 
	"""
	Class that generates the nodes of the binary tree. 
	Useful for sampling a FineteDiscrete in O(log n)
	"""

	def __init__(self, value, weight): 
		self.value = value
		self.weight = weight
		self.left = None
		self.right = None

	def redefined_as(self, new_node):
		"""
		Redirect self to the new_node object, copying all of its atributtes. 

		Arguments
		------------
		new_node: Node
			The node that replaces the self pointer

		"""
		self.value, self.weight, self.left, self.right = new_node.value, new_node.weight, new_node.left, new_node.right

	def get_copy(self):
		"""
		Gets a copy object of self. Useful for add_value method. 

		Returns
		------------
		Node
			A copy of self

		"""
		return copy.deepcopy(self)

	def describe(self, depth = 0):
		"""
		Prints every element of the self object, and all of the nodes below, in order. 

		Arguments
		------------
		depth: int >= 0
			Keeps track of how many levels down this node is with respect to the root

		"""
		print("val:", self.value)
		print("wei", self.weight, "\n")

		if self.left == None: 
			print("left: None")
		else:
			print(f"left ({depth}): ")
			self.left.describe(depth = depth + 1)

		if self.right == None: 
			print("right: None")
		else:
			print(f"right ({depth}): ")
			self.right.describe(depth = depth + 1)

	def add_value(self, value, weight): 
		"""
		A new value is being added to the node. 
		Note there is the convention that the left node has always >= value than the right one. 

		Arguments
		------------
		value: float
			The value of the node

		weight: float >= 0
			The weight that the new value has to compare the probabilities of each node. Non negative. 

		"""

		# Node is a leaf 
		if self.value != None: 
			new_node = Node(value = None, weight = weight + self.weight)
			if self.weight > weight: 
				new_node.left = self.get_copy()
				new_node.right = Node(value = value, weight = weight)
			else:
				new_node.left = Node(value = value, weight = weight)
				new_node.right = self.get_copy()
			self.redefined_as(new_node)

		# Node is intermediate
		else:

			# The new node is greater than the examined node
			if weight > self.weight: 
				new_node = Node(value = None, weight = weight + self.weight)
				new_node.left = Node(value = value, weight = weight)
				new_node.right = self.get_copy()
				self.redefined_as(new_node)

			# The new node is greater than the left child, but not the examined node
			elif weight > self.left.weight: 
				new_node = Node(value = None, weight = weight + self.weight)
				new_node.left = self.get_copy()
				new_node.right = Node(value = value, weight = weight)
				self.redefined_as(new_node)

			# The new node plus the right child is greater than the left child
			elif weight + self.right.weight > self.left.weight: 
				new_node = Node(value = None, weight = weight + self.weight)
				new_node.left = self.right
				new_node.right = self.left
				new_node.left.add_value(value, weight)
				self.redefined_as(new_node)
			else: 
				self.weight += weight
				self.right.add_value(value, weight)
			

	def get_samples(self, n = 1): 
		"""
		Get n samples the node using the relative weights as probabilities

		Arguments
		------------
		n: int >= 1
			Number of samples to get
		
		Returns
		------------
		list
			Containing the n values sampled

		"""

		if self.value != None: 
			return np.repeat(self.value, n)

		n_samples_left = np.random.binomial(n = n, p = self.left.weight / self.weight)
		n_samples_right = n - n_samples_left

		return np.append(self.left.get_samples(n_samples_left), self.right.get_samples(n_samples_right))












