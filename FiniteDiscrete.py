
import numpy as np
from Deterministic import Deterministic


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
		Creates self.support, and the self.probs dict. 

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
		return None







