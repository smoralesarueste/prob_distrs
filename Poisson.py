
import numpy as np

from math import log, exp, factorial, ceil

from auxs import InfiniteSet

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
		if not (isinstance(_lambda, int) or isinstance(_lambda, float)): 
			raise TypeError("Lambda parameter has to be float or int")

		# Check lambda is greater than 0
		assert _lambda > 0, "Lambda parameter can not be negative for a Poisson distribution"

		# Assign lambda param
		self._lambda = _lambda

		# Creates support set as the set of all natural numbers
		self.support = InfiniteSet(base_set = "N")

		# Creates the prob function 
		self.probs = self.get_prob_function()


	def get_prob_function(self):
		"""
		Creates self.probs function to evaluate the probability of a value. 
		Use memoization and the recurrence formula P(k+1) = P(k) * lambda / (k+1)

		Returns
		------------
		function:value->float
			The self.probs value for the PDF of a Poisson distribution
		
		"""

		def memoized_PDF(): 

			# Cache for known values
			cache = dict()

			# Base step: P(0) is easy to compute
			cache[0] = exp(-self._lambda)


			def PDF(value):
				# If value not in support, prob is 0
				if value not in self.support: return 0.0

				# If prob has been memoized, no need for calculation
				# Otherwise, we advance using the recursion formula, memoizing the steps
				if value > len(cache)-1: 
					i = len(cache)-1
					while i < value: 
						cache[i+1] = cache[i] * self._lambda / (i+1)
						i += 1
				return cache[value]

			return PDF

		return memoized_PDF()

	def get_mean(self):
		"""
		Computes the unconditional mean of the distr. 

		Returns
		------------
		float
		
		"""
		return self._lambda

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

		return self._lambda

	def get_median(self):
		"""
		Computes the median of the distr. 

		Returns
		------------
		float
		
		"""

		return ceil(self._lambda - log(2))

	def get_mode(self):
		"""
		Computes the mode of the distr. 

		Returns
		------------
		float
		
		"""
		return ceil(self._lambda) - 1

	def get_moment(self, n, c = 0): 
		"""
		Computes the n-th moment of the distr, centered on c. 
		For lack of mathematical knowledge, only n = 0,1,2 are allowed

		Arguments
		------------
		n: int
			The moment to calculate. Has to be a positive integer. 
			Only n = 0,1,2 are allowed for now
		c: float
			The center of the calculation. Default value of 0. 

		Returns
		------------
		float
		
		"""

		# Check if n = 0,1,2
		assert n in (0,1,2), f"Error computing the {n}-th moment: Parameter n has to be 0, 1 or 2. "

		# Returning based on per case resolution
		if n == 0: 
			return 1
		elif n == 1: 
			return self.get_mean() - c
		else:
			(self.get_mean - c)**2 + self.get_var()
		return

	def get_entropy(self):
		"""
		Computes the entropy of the distr. 
		Returns None, as no closed form is known. 

		Returns
		------------
		float
		
		"""
		return None

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
		return None









