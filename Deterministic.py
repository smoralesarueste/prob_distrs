



class Deterministic: 
	"""
	Class to deal with deterministic distributions. 
	"""

	def __init__(self, value): 

		self.value = value

	@property
	def support(self):
		return {self.value}
	

	def get_mean(self):
		"""
		Computes the unconditional mean of the distr. 

		Returns
		------------
		float
		
		"""
		return self.value

	def get_std(self):
		"""
		Computes the standard deviation of the distr. 

		Returns
		------------
		float
		
		"""
		return 0

	def get_var(self):
		"""
		Computes the variance of the distr. 

		Returns
		------------
		float
		
		"""
		return 0

	def get_median(self):
		"""
		Computes the median of the distr. 

		Returns
		------------
		float
		
		"""
		return self.value

	def get_mode(self):
		"""
		Computes the mode of the distr. 

		Returns
		------------
		float
		
		"""
		return self.value

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
		return (self.value - c)**n

	def get_entropy(self):
		"""
		Computes the entropy of the distr. 

		Returns
		------------
		float
		
		"""
		return 0

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
		return [self.value for _ in range(k)]



d = Deterministic(1)


print(d.get_samples(10))







