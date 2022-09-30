from auxs import BinaryTree as bt


vals = [i for i in range(100_000)]
weigs = [i**2 for i in range(100_000)]



from collections import Counter


tree = bt(vals, weigs)

sams = tree.get_samples(100_000_000)

print(Counter(sams))