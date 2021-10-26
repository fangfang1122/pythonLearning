# （一）编写加减乘除函数并测试使用
def add_(a, b):
    return a + b


def subtract_(a, b):
    return a - b


def multiply_(a, b):
    return a * b


def divide(a, b):
    return (a / b)


def demo1():
    print('加：', add_(1, 2))
    print('减：', subtract_(1, 2))
    print('乘：', multiply_(1, 2))
    print('除：', divide(1, 2))


# （二）编写lamda表达式加减乘除函数并使用
def demo2():
    add__ = lambda a, b: a + b
    sub__ = lambda a, b: a - b
    mul__ = lambda a, b: a * b
    div__ = lambda a, b: a / b
    print('加：', add__(1, 2))
    print('减：', sub__(1, 2))
    print('乘：', mul__(1, 2))
    print('除：', div__(1, 2))


# （三）参考教材5.3,练习不同的参数类型策略
# 默认值传参
def moRenZhiChuanCan(name='ff'):
    return 'hello ' + name


# 关键传参
def guanJianChuanCan(name='ff', year='18', learning='python'):
    return name + " " + year + " " + learning


# 可变长度参数
# *parameter接收多个实参并将其放在一个元组中
# **parameter接收类似于关键参数一样显示赋值形式的多个实参并将其放入字典中
def keBianChuanCan(a, b, c=4, *aa, **bb):
    print("可变长度参数(1, 2, 3, 4, 5, 6, 7, 8, 9, XX='1', YY='2', ZZ='3')：keBianChuanCan(a, b, c=4, *aa, **bb)")
    print(f"a={a},b={b},c={c}")
    print(f"aa={aa}")
    print(f"bb={bb}")


# 参数传递时的序列解包
def xuLieJieBao(a, b, c):
    return f'a={a},b={b},c={c}'


def demo3():
    print('默认值传参：', moRenZhiChuanCan())
    print('默认值传参-显式传参：', moRenZhiChuanCan('fangfang'))
    print()

    print('关键传参：', guanJianChuanCan('fangfang', '20', 'java'))
    print('关键传参-调整实参顺序：', guanJianChuanCan(learning='java', name='fangfang', year='20'))
    print()

    keBianChuanCan(1, 2, 3, 4, 5, 6, 7, 8, 9, XX='1', YY='2', ZZ='3')
    print()

    print('序列解包(列表):', xuLieJieBao(*[1, 2, 3]))
    print('序列解包(元组):', xuLieJieBao(*(1, 2, 3)))
    dic = {1: 'a', 2: 'b', 3: 'c'}
    print('序列解包(字典-键):', xuLieJieBao(*dic))
    print('序列解包(字典-值):', xuLieJieBao(*dic.values()))
    print('序列解包(集合):', xuLieJieBao(*{1, 2, 3}))


# （四）实验指导书-17:模拟汉诺塔问题
def hannuota(num, src, dst, temp=None):  # 递归算法
    if num < 1:
        return
    global times  # 声明全局变量-移动次数
    # 递归调用自身，先把除最后一个盘子外所有盘字移到临时柱上
    hannuota(num - 1, src, temp, dst)
    # 移动最后一个盘子
    print(f'the {times} Times move: {src} to {dst}')
    towers[dst].append(towers[src].pop())
    for tower in 'ABC':
        print(f"tower {tower} : {towers[tower]}")
    # 把除最后一个盘子之外的其它盘子从临时底座上移到目标底座上
    hannuota(num - 1, temp, dst, src)


times = 1  # 移动次数
n = 64  # 盘子数量
towers = {
    'A': list(range(n, 0, -1)),  # 初始状态，所有盘子在A上
    'B': [],
    'C': []
}

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # A表示最初放置盘子的底座,C是目标底座，B是临时底座
    hannuota(n, 'A', 'C', 'B')
