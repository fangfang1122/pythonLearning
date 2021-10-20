# （一）使用循环，判断一个正整数是否为素数
def demo1():
    n = int(input("输入一个正整数n（n>=2）："))
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} 不是素数")
            break
    else:
        print(f"{n} 是素数")


# （二）使用选择和循环，输出由1、2、3、4这四个数组成的每位数都不相同的所有三位数
def demo2():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    print(f"{i}{j}{k}", end='  ')


def demo3():
    while True:
        try:
            n = int(input('请输入评委人数：'))
            assert n > 2
            break
        except:
            print('必须输入大于2的整数')

    scores = []
    for i in range(n):
        while True:
            try:
                score = float(input(f"请输入第 {i + 1} 个评委的分数："))
                assert 0 <= score <= 100
                scores.append((score))
                break
            except:
                print('必须输入0~100的分数')

    highest = max(scores)
    scores.remove(highest)
    lowest = min(scores)
    scores.remove(lowest)

    # 计算平均分，保留2个小数
    finalScore = round(sum(scores) / len(scores), 2)

    print(f'去掉一个最高分 {highest}\n去掉一个最低分 {lowest}\n最后得分 {finalScore}')


def demo4():
    while True:
        try:
            n = int(input('请输入评委人数：'))
            assert n > 2
            break
        except:
            print('必须输入大于2的整数')

    maxScore, minScore = 0, 100
    total = 0

    for i in range(n):
        while True:
            try:
                score = float(input(f"请输入第 {i + 1} 个评委的分数："))
                assert 0 <= score <= 100
                break
            except:
                print('必须输入0~100的分数')
        total += score
        if score > maxScore:
            maxScore = score
        if score < minScore:
            minScore = score

    # 计算平均分，保留2个小数
    finalScore = round((total - maxScore - minScore) / (n - 2), 2)

    print(f'去掉一个最高分 {maxScore}\n去掉一个最低分 {minScore}\n 最后得分 {finalScore}')


# （四）编写程序,计算100以内所有奇数的和
def demo5():
    list_ = []
    for i in range(0, 101):
        if i % 2 != 0:
            list_.append(i)
    print('100以内的所有奇数为:', list_)
    print('奇数和为:', sum(list_))


# 举例python几种常用的条件表达式。
def demo6():
    # 正常用法
    x = 2
    if x == 1:
        s = 'p'
    elif x == 2:
        s = 'y'
    elif x == 3:
        s = 't'
    else:
        s = 'h'
    print(s)

    # 三元表达式
    age = 17
    s = 'minor' if age < 18 else 'adult'
    print(s)

    s = ('p' if x == 1 else
         'y' if x == 2 else
         't' if x == 3 else
         'h'
         )
    print(s)


if __name__ == '__main__':
    demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
