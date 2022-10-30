
import numpy as np

from math import floor, log

from FiniteDiscrete import FiniteDiscrete

class Binomial: 
	"""
	Class to deal with Binomial distributions. 
	"""

	def __init__(self, n, p): 
		"""
		Generates the basic object. 

		Arguments
		------------
		n: int
			Parameter with the size of the distribution
		p: float
			Probability of success for each realization
		
		"""

		# Check if n is an int
		if not isinstance(n, int): 
			raise TypeError("N parameter has to be int")

		# Check if p is a float
		if not (isinstance(p, float) or isinstance(p, int)): 
			raise TypeError("p parameter has to be float or int")

		# Check p is greater >= 0 and <= 1
		assert p >= 0 and p <= 1, "p parameter has to be between 0 and 1"

		# Assign n and ´
		self.n = n
		self.p = p

		# Creates support set as the set of all natural numbers
		self.support = np.array([*range(n+1)])

		# Creates the prob function 
		self.probs = self.get_prob_function()

		# Creates the PDF as a FiniteDiscrete one
		self.finite_discrete = self.get_finite_discrete()


	def get_prob_function(self):
		"""
		Creates self.probs function to evaluate the probability of a value. 

		Returns
		------------
		function: value -> float
			The self.probs value for the PDF of a Poisson distribution
		
		"""

		def PDF(k): 
			# If function is not in the support, its probability is 0
			if k not in self.support: return 0.0

			# Computing the binnomial coeffiicent trying yo avoid the factorial terms
			bin_coef = 1.0
			if k <= self.n / 2:
				for i in range(k): 
					bin_coef *= (self.n - i) / (i + 1)
			else:
				for i in range(self.n - k): 
					bin_coef *= (self.n - i) / (i + 1)

			return bin_coef * (self.p ** k) * (1 - self.p) ** (self.n - k)


		return PDF

	def get_finite_discrete(self): 
		"""
		Creates self.finite_discrete PDF object that represents the entire distribution. 

		Returns
		------------
		FiniteDiscrete
			The self.finite_discrete object representing the distribution. 
		
		"""
		return FiniteDiscrete({val: self.probs(val) for val in [*self.support]})

	def get_mean(self):
		"""
		Computes the unconditional mean of the distr. 

		Returns
		------------
		float
		
		"""
		return self.n * self.p

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

		return self.get_mean() * (1 - self.p)

	def get_median(self):
		"""
		Computes the median of the distr. 

		Returns
		------------
		float
		
		"""

		return floor(self.get_mean())

	def get_mode(self):
		"""
		Computes the mode of the distr. 

		Returns
		------------
		float
		
		"""
		return floor(self.get_mean() + self.p)

	def get_moment(self, n, c = 0): 
		"""
		Computes the n-th moment of the distr, centered on c. 

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

		return sum([self.probs(val) * (val - c) ** n for val in [*self.support]])

	def get_entropy(self):
		"""
		Computes the entropy of the distr. 
		Returns None, as no closed form is known. 

		Returns
		------------
		float
		
		"""
		return - sum([self.probs(val) * log(self.probs(val)) for val in [*self.support]])

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
		if not isinstance(k, int): 
			raise TypeError("k parameter has to be int")

		assert k >= 0, "k parameter can not be negative"

		return self.finite_discrete.get_samples(k)









