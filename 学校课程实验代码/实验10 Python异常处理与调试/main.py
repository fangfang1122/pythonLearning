# （一）参考教材8.2(P183),编写自定义异常类并测试
class ShortInputException(Exception):
    "自定义异常类"

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

    def showMessage(self):
        print(f"ShortInputException:输入的长度是{self.length},长度至少应是{self.atleast}")


def demo1():
    try:
        s = input("请输入：")
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except EOFError:
        print('你输入了一个结束标记EOF')
    except ShortInputException as x:
        x.showMessage()
    else:
        print("没有异常发生")


# （二）使用读方式打开一个不存在的txt文件, 编写相应的异常处理,使得出现异常时候就新建一个该文件,并退出
def demo2():
    try:
        with open('一个不存在的文件.txt') as f:
            print(f.read())
    except OSError as reason:
        print('出错啦！reason: ' + str(reason))
        f = open('一个不存在的文件.txt', 'a+')
        print("已自动新建该文件 - 一个不存在的文件.txt")
        f.close()


def demo3():
    import pdb
    n = 7
    pdb.set_trace()
    for i in range(2, n):
        if n % i == 0:
            print('No')
            break
        else:
            print('Yes')


def demo4():
    for i in range(-2, 10):
        try:
            assert i > 0, " i 不能小于 0 "
            print(i)
        except AssertionError as reason:
            print(f"{reason.__class__.__name__}:{reason}")


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    demo4()
