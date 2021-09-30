# （一）熟悉列表创建、元素增加、删除等。
def demo1():
    a_list_0 = []  # 创建空列表
    a_list = list(range(1, 10, 2))  # 创建列表
    print('创建空列表：', a_list_0)
    print('创建列表：', a_list)

    a_list_0.append(0)  # append添加元素至尾部
    a_list_0.extend(a_list)  # extend讲另一个迭代对象所有元素添加至尾部
    a_list_0.insert(1, 1001)  # insert添加元素至指定位置
    print('元素增加:', a_list_0)

    del a_list_0[0]  # del删除指定位置的元素，或整个列表
    a_list_0.pop()  # pop删除指定位置元素并返回该元素，默认删除最后一个元素
    a_list_0.remove(3)  # 删除首次出现的指定元素
    print('删除后:', a_list_0)


# （二）练习列表的访问、切片、计数、成员判断、排序操作
def demo2():
    a_list = list(range(1, 10, 1))  # 创建列表
    print('列表：', a_list)

    print('列表访问')
    print('直接指定下标访问元素:', a_list[0])
    print('index()获取指定元素出现的下标：', a_list.index(1))  # index(value,[start,[stop]]),stop默认为列表长度
    print('count()统计指定元素出现次数', a_list.count(1))

    print('切片操作')
    print('切片访问元素：', a_list[0:8:2])  # 切片：切片开始位置，切片截止位置（默认列表长度）,切片步长
    a_list[len(a_list):] = [11]  # 切片增加元素
    print('切片增加元素：', a_list)
    a_list[:3] = [16, -11, -21]
    print('切片修改元素：', a_list)

    print('成员判断')
    print('1是否在列表内：', 1 in a_list)
    print('0是否在列表内：', 0 in a_list)

    print('排序操作')
    import random
    random.shuffle(a_list)  # 打乱顺序
    print('当前列表：', a_list)
    a_list.sort()  # 返回空
    print('sort()默认升序列表:', a_list)
    a_list.sort(reverse=True)
    print('sort(reverse=True)降序:', a_list)


# （三）编写代码，练习map,list,any,all,zip内置函数使用。
def demo3():
    def square(x):
        return x ** 2

    # list()方法用于将元组转换为列表。
    print("map()和list()操作：", list(map(square, [1, 2, 3, 4, 5])))  # map() 会根据提供的函数对指定序列做映射。
    # 元素除了是 0、空、None、False 外都算 True
    # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，是则返回 False，如果有一个为 True，则返回 True。
    print("any(['','',False])操作：", any(['', '', False]))
    print("any(['a','12',False])操作：", any(['a', '12', False]))
    # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
    print("all(['a','',123])操作：", all(['a', '', 123]))
    print("all(['a','12',123])操作：", all(['a', '12', 123]))
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    a_list = [1, 2, 3]
    b_list = [4, 5, 6]
    c_list = ['a', 'b', 'c']
    print('zip操作:', list(zip(a_list, b_list, c_list)))


# （四）编写代码，练习列表推导式的使用。
def demo4():
    list_a = [b for b in range(5)]
    print(list_a)
    list_b = [i for i in range(10) if i % 2 == 0]  # 生成一个包含10以内的偶数的list
    print(list_b)


if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    demo4()
