

class InfiniteSet: 
	"""
	Class that allows to deal with a set of potentially infinite numbers. 
	"""

	def __init__(self, base_set = "naturals", exceptions_set = None):
		"""
		Generates the set. 

		Arguments
		------------
		base_set: str
			Name of the set, if looking for a known set. 
			Can be: 
				- "naturals" or "N" for natural numbers
				- "negative naturals" or "NN" for the negative version of every natural number
				- "positive naturals" or "N+" for natural numbers without the 0
				- "strictly negative naturals" or "N-" for negative natural numbers without the 0
				- "integers" or "Z" for integers
				- "rationals" or "Q" for rational numbers
				- "irrationals" or "I" for irrational numbers
				- "reals" or "R" for real numbers
				- Default value: "naturals"

		exceptions_set: set or list
			Set of values to delete from the set. Can be a finite or infinite set. 
			If an element is not in the base set, it wont be considered. 
		
		"""

		assert isinstance(exceptions_set, InfiniteSet) or \
			isinstance(exceptions_set, set) or isinstance(exceptions_set, list) or \
			exceptions_set == None, "Exception sets must be an infinite set, set, list or None"

		# Natural numbers
		if base_set in ("naturals", "N"): 
			self.create_natural_numbers(exceptions_set)

		# Negative Naturals
		elif base_set in ("negative naturals", "NN"): 
			self.create_negative_naturals(exceptions_set)

		# Positive naturals
		elif  base_set in ("positive naturals", "N+"): 
			self.create_positive_naturals(exceptions_set)

		# Strictly negative numbers
		elif  base_set in ("strictly negative naturals", "N-"): 
			self.create_strictly_negative_naturals(exceptions_set)

		# Integers
		elif  base_set in ("integers", "Z"): 
			self.create_integers(exceptions_set)

		# Reals
		elif  base_set in ("reals", "R"): 
			self.create_reals(exceptions_set)

		# Invalid input
		else:
			err_txt = "Invalid base set selection. \n"
			err_txt += "Must choose one from the following: \n"
			err_txt += "\t* 'naturals' or 'N' for natural numbers \n"
			err_txt += "\t* 'negative naturals' or 'NN' for negative natural numbers \n"
			err_txt += "\t* 'positive naturals' or 'N+' for strictly positive natural numbers \n"
			err_txt += "\t* 'strictly negative naturals' or 'N-' for strictly negative natural numbers \n"
			err_txt += "\t* 'integers' or 'Z' for integer numbers \n"
			err_txt += "\t* 'reals' or 'R' for real numbers \n"
			raise AssertionError(err_txt)


	def __contains__(self, value): return self.validator(value)


	def create_natural_numbers(self, exceptions_set):
		"""
		Create the object to be the set of all natural numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value):
			if isinstance(value, int): return not (value in self.exceptions_set) and value >= 0
			if isinstance(value, float) and (value - int(value)) == 0.0: return not (value in self.exceptions_set) and value >= 0
			return False

		self.validator = validator


	def create_negative_naturals(self, exceptions_set):
		"""
		Create the object to be the set of all negative natural numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value):
			if isinstance(value, int): return not (value in self.exceptions_set) and value <= 0
			if isinstance(value, float) and (value - int(value)) == 0.0: return not (value in self.exceptions_set) and value <= 0
			return False

		self.validator = validator


	def create_positive_naturals(self, exceptions_set):
		"""
		Create the object to be the set of all strictly positive natural numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value):
			if isinstance(value, int): return not (value in self.exceptions_set) and value > 0
			if isinstance(value, float) and (value - int(value)) == 0.0: return not (value in self.exceptions_set) and value > 0
			return False

		self.validator = validator


	def create_strictly_negative_naturals(self, exceptions_set):
		"""
		Create the object to be the set of all strictly negative natural numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value, exceptions_set):
			if isinstance(value, int): return not (value in self.exceptions_set) and value < 0
			if isinstance(value, float) and (value - int(value)) == 0.0: return not (value in self.exceptions_set) and value < 0
			return False

		self.validator = validator


	def create_integers(self, exceptions_set):
		"""
		Create the object to be the set of all integer numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value):
			if isinstance(value, int): return not (value in self.exceptions_set)
			if isinstance(value, float) and (value - int(value)) == 0.0: return not (value in self.exceptions_set)
			return False

		self.validator = validator


	def create_reals(self, exceptions_set):
		"""
		Create the object to be the set of all real numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value):
			if isinstance(value, int): return not (value in self.exceptions_set)
			if isinstance(value, float): return not (value in self.exceptions_set)
			return False

		self.validator = validator


	def create_reals(self, exceptions_set):
		"""
		Create the object to be the set of all real numbers
		"""

		# Assigning the set of exceptions
		if exceptions_set == None: 
			self.exceptions_set = set()
		else:
			self.exceptions_set = exceptions_set

		# Creating and assigning the function to validate whether a value is within the set or not
		def validator(value):
			if isinstance(value, int): return not (value in self.exceptions_set)
			if isinstance(value, float): return not (value in self.exceptions_set)
			return False

		self.validator = validator









