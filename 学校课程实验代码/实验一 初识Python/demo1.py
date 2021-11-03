# import numpy as np
#
# str_ = '1 2 3;4 5 6;7 8 9'
# a = np.mat(str_)
# print("用字符串创建矩阵：", a)

"""
（二）定义一个Person父类和Student, Staff子类；父类定义shouru，display方法，
Student类的收入按照初始化奖学金计算，Staff的按照60%*工资+40%*奖金计算，调用display显示工资。编写测试代码
"""


class Person:
    def __init__(self, name):
        self.__name = name
        self.__money = 0
        self.__type = 'person'

    def shouru(self):
        pass

    def display(self):
        print(f"name:{self.__name}  type:{self.__type}   salary:{self.__money}")


class Student(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        self.__type = 'student'

    def shouru(self, award):
        self.__money = award * 1.0


class Staff(Person):

    def __init__(self, name):
        Person.__init__(self, name)
        self.__type = 'staff'

    def shouru(self, salary, award):
        self.__money = 0.6 * salary + 0.4 * award


if __name__ == "__main__":
    stu = Student("zhangsan")
    stu.shouru(2000)
    stu.display()

    staff = Staff("lisi")
    staff.shouru(8000, 4000)
    staff.display()
