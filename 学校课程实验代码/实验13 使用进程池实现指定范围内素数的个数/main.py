from time import time
from multiprocessing import Pool
"""
创建进程池使用进程池的map（）方法，把该函数映射到指定范围内的数字，
使用内置函数sum（）统计有多少素数。 同时，使用内置函数map（）和sum（）完成相同的任务，比较单进程和多进程的速度。
"""

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    start = time()
    print("1-100000内素数：", sum(map(isPrime, range(100000))))
    print("单进程时间：", time() - start)

    start = time()
    with Pool(15) as p:
        print("1-100000内素数：", sum(p.map(isPrime, range(100000))))
    print("多进程时间：", time() - start)
