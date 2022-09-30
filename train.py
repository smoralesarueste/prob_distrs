







import random, time
from FiniteDiscrete import FiniteDiscrete as fd

from collections import Counter
from pprint import pprint

N = 1_000


# vals = [i for i in range(N)]
vals = [1,2,3,4]
# weigs = [(10 * random.random())**3 for i in range(N)]
weigs = [10, 50, 25, 15]

dist = fd({vals[i]: weigs[i] for i in range(4)})# N)})


n_samples = 100_000_000


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


@timer_func
def get_samples(n):
	return dist.get_samples(n)

@timer_func
def get_samples_original(n):
	return random.choices(population = vals, weights = weigs, k = n)

pprint(Counter(get_samples(n = n_samples)))
# get_samples_original(n = n_samples)

# dist.get_samples(n_samples)





