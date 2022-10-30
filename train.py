







import random, time

from Binomial import Binomial as bnm

distr = bnm(n = 2, p = .2)


print(distr.get_mean())
print(distr.get_moment(c = distr.get_mean(), n = 3))
print(distr.get_var())
print(distr.get_entropy())
