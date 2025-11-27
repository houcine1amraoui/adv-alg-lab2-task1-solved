from utils import sum_array
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

sizes = [100, 1000, 10000]
times1 = []
times2 = []

for size in sizes:
    # complete the loop
    pass

plt.plot(sizes, times1, label="my sum")
plt.plot(sizes, times2, label="python sum")
plt.legend()
plt.show()