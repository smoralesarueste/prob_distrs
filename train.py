







import random, time


from auxs import InfiniteSet as inf_set


excs = inf_set(base_set = "Z")
target = inf_set(base_set = "R", exceptions_set = excs)


print(dir(target.exceptions_set))


for i in range(26): 
	print(f"{i**0.5:.2f}" + ": " + str(i**0.5 in target))