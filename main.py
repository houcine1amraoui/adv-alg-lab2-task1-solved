from utils import sum_array
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt
sizes = [100, 1000, 10000]
times1 = []
times2 = []
for size in sizes:
    arr = [randint(0, 10) for i in range(size)]
    time1 = timeit(lambda: sum_array(arr), number=10)/10
    time2 = timeit(lambda: sum(arr), number=10)/10
    times1.append(time1)
    times2.append(time2)

plt.plot(sizes, times1, label="my sum")
plt.plot(sizes, times2, label="python sum")
plt.legend()
plt.show()