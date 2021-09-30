# （一）练习元组、字典、集合的创建和使用等
def demo1():
    a_tuple = (1, 2, 3, 4)
    a_tuple2 = (tuple('asdf'))
    print("元组创建：", a_tuple, a_tuple2)
    a_dict = {'name': 'ff', 'age': '19'}
    print('字典创建：', a_dict)
    a_dict['school_id'] = '201904010427'
    a_dict['age'] = 18
    print('字典添加及修改：', a_dict)
    a_set = set(range(1, 10))
    b_set = set(range(1, 10, 2))
    print('集合创建及使用交集：', a_set, b_set, a_set & b_set)


# （二）练习列表、元组、字典等序列的解包操作
def demo2():
    a_list = (2, 3, 4, 5)
    a, b, c, d = a_list
    print('列表序列解包：', a, b, c, d)
    a_tuple = (1, 2, 3, 4)
    a, b, c, d = a_tuple
    print('元组序列解包：', a, b, c, d)
    print('用 * 序号解包：', *range(3))
    a_dict = {'name': 'ff', 'age': '19'}
    a, b = a_dict.items()  # 默认对 键 操作，items()对 键值对，values()对 值
    print('字典序列解包：', a, b)
    print('序列解包之同时遍历多个序列：', end=' ')
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    for key, value in zip(keys, values):
        print(key, value, end=' ,')


# （三）编写代码，练习生成器、字典、集合推导式使用。
def demo3():
    gen = (i + 2 for i in range(10) if i % 2 == 0)  # 生成器表达式
    list1 = list(gen)
    print("生成器表达式:", list1)
    list1 = ["天空", "白云", "大地", "小草", "大树"]
    dict1 = dict(enumerate(list1))
    print("字典推导式(枚举):", dict1)
    dict2 = {'name': 'ff', 'age': '11'}
    dict2_get = {v: k for k, v in dict2.items()}
    print("字典推导式(快速更换key、value):", dict2_get)
    set1 = {i for i in list(range(10))}
    print("集合推导式:", set1)  # 注意集合的去重性


def demo4():
    num = input('请输入一个自然数：')
    print(sum(map(int, num)))

    setA = eval(input('请输入一个集合：'))
    setB = eval(input('再输入一个集合：'))
    print('交集：', setA & setB)
    print('并集：', setA | setB)
    print('setA-setB:', setA - setB)

    num = int(input('请输入一个自然数：'))
    print('二进制：', bin(num))
    print('八进制；', oct(num))
    print('十六进制：', hex(num))

    lst = eval(input('请输入一个包含若干整数的列表：'))
    print(list(filter(lambda x: x % 2 == 0, lst)))

    lstA = eval(input('请输入一个包含若干整数的列表A：'))
    lstB = eval(input('请输入一个包含若干整数的列表B：'))
    result = dict(zip(lstA, lstB))
    print(result)

    lst = eval(input('请输入一个包含若干整数的列表：'))
    print(sorted(lst, reverse=True))

    from functools import reduce
    lst = eval(input('请输入一个包含若干整数的列表：'))
    print(reduce(lambda x, y: x * y, lst))

    lstA = eval(input('请输入一个包含若干整数的列表A：'))
    lstB = eval(input('请输入一个包含若干整数的列表B：'))
    print(sum(map(lambda i, j: abs(i - j), lstA, lstB)))

    lstSets = eval(input('请输入一个包含若干集合的列表：'))
    print(reduce(lambda x, y: x | y, lstSets))

    a1 = int(input('请输入等比数列首项：'))
    q = int(input('请输入等比数列公比(不等于1且小于36的正整数):'))
    n = int(input('请输入一个自然数：'))
    result = a1 * int('1' * n, q)  # 这个方法屌爆了我感觉
    print(result)

    data = input('请输入一个字符串：')
    d = dict()
    for ch in data:
        d[ch] = d.get(ch, 0) + 1
    mostCommon = max(d.items(), key=lambda item: item[1])
    print(mostCommon)


if __name__ == '__main__':
# demo1()
# demo2()
# demo3()
# demo4()
