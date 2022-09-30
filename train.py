

import random, time
from FiniteDiscrete import FiniteDiscrete as fd



N = 1_000_000


vals = [i for i in range(N)]
weigs = [(10 * random.random())**2 for i in range(N)]

dist = fd({vals[i]: weigs[i] for i in range(N)})


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

get_samples(n = n_samples)
get_samples_original(n = n_samples)

# dist.get_samples(n_samples)


