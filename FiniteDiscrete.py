
import numpy as np

from math import log

from Deterministic import Deterministic
from auxs import BinaryTree

class FiniteDiscrete: 
	"""
	Class to deal with finite discrete distributions of arbitrary densities. 
	"""

	def __init__(self, values): 
		"""
		Generates the basic object. 

		Arguments
		------------
		values: list or dict
			If list, the elements are the support, and the distributions is assumed to be uniform. 
			If dict, the keys are the values in the support, each one pointing to its (proportional) weight
		
		"""

		# Check if values is either list or dict
		if isinstance(values, list):
			vals = np.array(values, dtype = float)
			weigs = np.repeat(1., len(values))

		elif isinstance(values, dict):
			vals = np.fromiter(values.keys(), dtype = float)
			weigs = np.fromiter(values.values(), dtype = float)

		else:
			raise TypeError("FiniteDiscrete values argument should be a list or a dict")

		# Check the support is not an empty set
		assert len(vals) > 0, "Support can not be empty"

		# Check weights are non negative, and that the sum > 0
		assert (weigs >= 0).all(), "Weights must be non-negative"
		assert weigs.sum() > 0, "Weights can not be all 0"

		# Omit values with weight == 0, they are not part of the support
		vals, weigs = vals[weigs>0], weigs[weigs>0]

		# Creates support set and probability dictionary
		self.support, self.probs = self.get_support_probs(vals, weigs)

		# Creates balances binary tree for sampling
		self.tree_repr = self.get_tree_repr(vals, weigs)

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










