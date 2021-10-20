import jieba
import re


# （一）编写代码，练习% format f三种字符串格式化方法
def demo1():
    name = 'ff'
    age = '18'
    print('第一种：%% ---  Hello, my name is %s, and I am %s years old' % (name, age))
    print('第二种：format ---  Hello, my name is {0}, and I am {1} years old'.format(name, age))
    print(f'第三种：f-strings ---  Hello, my name is {name}, and I am {age} years old')


# （二）编写代码，参考教材4.1.2, 练习字符串常用方法
def demo2():
    s = "apple,peach,banana,peach,pear"
    print("方法：find(),rfind(),index(),rindex(),count()")
    print(s.find('peach'), end=', ')  # 返回第一次出现的位置，找不到返回-1
    print(s.find("peach", 7), end=', ')  # 指定位置开始查找
    print(s.find("prach", 7, 20), end=', ')  # 指定范围查找
    print(s.rfind('p'), end=', ')  # 从后往前找
    print(s.index('p'), end=', ')  # 返回第一次出现的位置，找不到抛出异常
    print(s.rindex('p'), end=',')  # 返回第一次出现的位置，找不到抛出异常
    print(s.count('p'))  # 统计出现次数

    s = "apple,peach,ban\nana,pear"
    print("方法：split(),rsplit(),partition(),rpartition()")
    print(s.split(','))  # 使用逗号分隔,若不指定，则以任何空白符号为分隔符
    print(s.split(None))  # 若不指定分隔符，则以任何空白符号为分隔符。
    print(s.split(',', 2))  # 允许指定最大分隔次数
    print(s.rsplit(','))  # 从后往前使用逗号分隔
    print(s.partition(','))  # 以逗号分隔出三部分
    print(s.rpartition(','))  # 从后往前以逗号分隔出三部分
    s = '2019-2-2'
    print(list(map(int, s.split('-'))))

    print('方法：join()')
    li = ['apple', 'peach', 'banana']
    sep = ','
    print(sep.join(li))  # 将列表中多个字符串相连，并在相邻之间加入指定字符

    s = "WhAt is Your Name?"
    print('方法：lower(),upper(),capitalize(),title(),swapcase()')
    print(s.lower())  # 全部小写
    print(s.upper())  # 全部大写
    print(s.capitalize())  # 第一个字符大写，其它小写
    print(s.title())  # 首字母大写
    print(s.swapcase())  # 大小写互换

    print('方法：replace()')
    s = "CHINA,SS"
    print(s.replace('S', 'AA'))  # 替换字符

    print('方法：maketrans()，translate()')
    table = ''.maketrans('123456', 'abcdef')  # 生成映射表
    s = '112233445566'
    print(s.translate(table))  # 转换字符

    print('方法：strip()，lstrip(),rsplit()')
    s = '   ssabc   '
    print(s.strip())  # 两端删除字符，默认空白字符
    print(s.strip('s'))
    print(s.lstrip())  # 左端开始
    s = '   ssabc   '
    print(s.rsplit())  # 右端开始

    print('方法：eval()')
    print(eval("3+4"))  # 转换表达式并求值

    print('方法：in()')
    print("a" in "abcde")  # 关键字in

    s = "beautiful"
    print(s.startswith('b'))  # 判断以字符开始
    print(s.endswith('u'))

    print('123'.isalnum())  # 判断字符串类型

    print('hell'.center(10))  # 返回指定宽度
    print('hell'.ljust(10, '-'))
    print('hel'.rjust(10, '='))


# （三）使用jieba对段落进行分词,并显示。
# 精确模式，试图将句子最精确地切开，适合文本分析；
# 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
# 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
def demo3():
    char_x2 = "人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器，该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。"

    test1 = jieba.cut(char_x2, cut_all=True)
    print("全模式: " + " | ".join(test1))

    test2 = jieba.cut(char_x2, cut_all=False)
    print("精确模式: " + " | ".join(test2))

    test3 = jieba.cut_for_search(char_x2)
    print("搜索引擎模式:" + " | ".join(test3))


# （四）使用正则表达,找出AABC和ABAC类型的成员
def demo4():
    s = '生财有道、极乐世界、情不自禁、愚公移山、魑魅魍魉、龙生九子、精卫填海、海市蜃楼、高山流水、卧薪尝胆、壮志凌云、金枝玉叶、四海一家、穿针引线、无忧无虑、无地自容、三位一体、落叶归根、相见恨晚、惊天动地、滔滔不绝、相濡以沫、长生不死、原来如此、女娲补天、三皇五帝、万箭穿心、水木清华、窈窕淑女'
    # 从左往右数每一个括号代表了一个正则表达式的子模式，\3代表的是此处匹配的项与子模式3相同，即ABAC
    pattern = r'(((.).\3.\W)|((.)\5(.).\W))'
    for i in re.findall(pattern, s):
        print(i[0][0:4])


# Python可以用哪几种方式连接多个字符串?
def demo5():
    s = 'aa' + 'bb'
    print('加号 方法:', s)
    s = 'aa''bb'
    print('直接相连 方法：', s)
    s = '%s %s' % ('Python', 'Tab')
    print('格式化 方法:', s)
    str_list = ['Python', 'Tab']
    print('join 方法：', ' '.join(str_list))
    s = ('select *'
         'from atable'
         'where id=888')
    print('多行字符串拼接（）方法：', s)


if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    demo5()
