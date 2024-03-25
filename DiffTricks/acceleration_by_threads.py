from multiprocessing.dummy import Pool as ThreadPool
from time import *


start = time()


def my_func(x):
    sleep(1)
    print(x)


my_list = [x for x in range(1, 10)]

pool = ThreadPool(12)
results = pool.map(my_func, my_list)

print('Время выполнения:')
print(time() - start)
