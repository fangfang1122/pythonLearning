import numpy as np


# 1.利用np.random.rand函数创建一个数组。并随机的在这个数组中添加缺失值。
# 2.
def demo1():
    array = np.array(np.random.rand(10))
    num = np.random.randint(0, 10, 3)
    for i in num:
        array[i] = None
    print(array)

    sum = 0
    for j in range(0, 10):
        if np.isnan(array[j]):
            sum += 1
            print(f"位置：{j}")
    print(f"总数：{sum}")


def demo2():
    array = np.array(np.random.rand(5, 5))
    num = np.random.randint(0, 5, 2)
    array[num[0]][num[1]] = None
    print(f"删除之前：{array}")
    for i in range(5):
        for j in range(5):
            if np.isnan(array[i][j]):
                after = np.delete(array, i, axis=0)
    print(f"删除之后：{after}")


if __name__ == '__main__':
    # demo1()
    demo2()
