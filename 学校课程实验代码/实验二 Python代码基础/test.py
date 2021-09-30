import numpy as np
from my_pkg import my_module


# （一）熟悉常用内置函数，如转换类函数：int(), str(), ord(), chr(), float()等;max(), mean(), sum(), sorted()等；
def demo1():
    print('int(3.14)操作：', int(3.14), type(int(3.14)))
    print('str(3.14)操作：', str(3.14), type(str(3.14)))
    print("ord('a')操作：", ord('a'), type(ord('a')))
    print('chr(97)操作：', chr(97), type(chr(97)))
    print('float(3)操作：', float(3), type(float(3)))
    print('max(1, 5, 8)操作：', max(1, 5, 8))
    print('np.mean([1, 2])操作：', np.mean([1, 2]))
    print('sum((1, 10, 3))操作：', sum((1, 10, 3)))
    print('sorted((1, 10, 3))操作：', sorted((1, 10, 3)))


# （二）练习input(), print()函数的使用
def demo2():
    name = input('请输入你的姓名：')
    print(f'你好,{name}')


# （三）编写自己的模块my_module.py, 编写自己的包,文件夹my_pkg/__init__.py. 在模块和包里面写入一些代码，并在test.py进行导入使用。
def demo3():
    my_module.hello("ff")


if __name__ == '__main__':
    demo1()
    demo2()
    demo3()
