
import numpy as np

from math import log

from auxs import BinaryTree

class Poisson: 
	"""
	Class to deal with Poisson distributions. 
	"""

	def __init__(self, _lambda): 
		"""
		Generates the basic object. 

		Arguments
		------------
		_lambda: float
			Parameter of the distribution. 
		
		"""

		# Check if lambda is a float
		if not isinstance(_lambda, float): 
			raise TypeError("FiniteDiscrete values argument should be a list or a dict")

		# Check lambda is greater than 0
		assert _lambda > 0, "Lambda parameter can not be negative for a Poisson distribution"

		# Creates support set and probability dictionary
		self.support, self.probs = self.get_support_probs(vals, weigs)

	def get_support_probs(self, values, weights):
		"""
		Creates self.support, and the self.probs dictionary. 

		Arguments
		------------
		values: list
			List of possible values in the support
		weights: list
			The relative weight of each element. Dont have to be normalized. 

		Returns
		------------
		tuple(set, dict)
			The self.support and self.probs attributes
		
		"""
		supp = set(values)

		total_weight = weights.sum()
		probs = {v: w / total_weight for (v,w) in zip(values, weights)}

		return supp, probs

	def get_tree_repr(self, values, weights): 
		"""
		Creates the balanced binary tree used to get faster samples from the distribution. 

		Arguments
		------------
		None

		Returns
		------------
		Node:
			The root of the tree. 
		
		"""
		return BinaryTree(list(values), list(weights))

	def get_mean(self):
		"""
		Computes the unconditional mean of the distr. 

		Returns
		------------
		float
		
		"""
		return sum([self.probs[val] * val for val in [*self.probs]]) / sum([self.probs[val] for val in [*self.probs]])

	def get_std(self):
		"""
		Computes the standard deviation of the distr. 

		Returns
		------------
		float
		
		"""
		return self.get_var()**0.5

	def get_var(self):
		"""
		Computes the variance of the distr. 

		Returns
		------------
		float
		
		"""

		mean = self.get_mean()
		return sum([self.probs[val] * (val - mean)**2 for val in [*self.probs]]) / sum([self.probs[val] for val in [*self.probs]])

	def get_median(self):
		"""
		Computes the median of the distr. 

		Returns
		------------
		float
		
		"""

		vals = [*self.probs]
		vals.sort()
		cum_prob = 0.0

		for val in vals:
			if cum_prob >= .5: break
			cum_prob += self.probs[val]

		return val

	def get_mode(self):
		"""
		Computes the mode of the distr. 

		Returns
		------------
		float
		
		"""
		return max(self.probs, key = self.probs.get)

	def get_moment(self, n, c = 0): 
		"""
		Computes the n-th moment of the distr, centered on c. 

		Arguments
		------------
		n: int
			The moment to calculate. Has to be a positive integer. 
		c: float
			The center of the calculation. Default value of 0. 

		Returns
		------------
		float
		
		"""

		return sum([self.probs[val] * (val - c)**n for val in [*self.probs]]) / sum([self.probs[val] for val in [*self.probs]])

	def get_entropy(self):
		"""
		Computes the entropy of the distr. 

		Returns
		------------
		float
		
		"""
		return - sum([self.probs[val] * log(self.probs[val]) for val in [*self.probs]]) / sum([self.probs[val] for val in [*self.probs]])

	def get_samples(self, k = 1):
		"""
		Generates k samples of the distr. 

		Arguments
		------------
		k: int >= 0
			The number of samples to generate. 

		Returns
		------------
		list[floats]
		
		"""
		return self.get_samples(k)










