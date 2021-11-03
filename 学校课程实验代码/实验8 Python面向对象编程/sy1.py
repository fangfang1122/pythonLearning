class Vector3:
    # 构造方法
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    # 向量相加
    def __add__(self, a):
        x = self.__x + a.__x
        y = self.__y + a.__y
        z = self.__z + a.__z
        return Vector3(x, y, z)

    # 向量相减
    def __sub__(self, a):
        x = self.__x - a.__x
        y = self.__y - a.__y
        z = self.__z - a.__z
        return Vector3(x, y, z)

    # 向量与一个数字相乘
    def __mul__(self, a):
        x, y, z = self.__x * a, self.__y * a, self.__z * a
        return Vector3(x, y, z)

    # 向量除以一个数字
    def __truediv__(self, a):
        x, y, z = self.__x / a, self.__y / a, self.__z / a
        return Vector3(x, y, z)

    # 查看向量长度，所有分量平方和的平方根
    def length(self):
        a = pow(pow(self.__x, 2) + pow(self.__y, 2) + pow(self.__z, 2), 0.5)
        return a

    def __str__(self):
        return f"Vector3({self.__x},{self.__y},{self.__z})"


print('请输入六个数a,b,c,d,e,f:')
a, b, c, d, e, f = map(int, input().split())
print('N1:', (a, b, c))
print('N2:', (d, e, f))
n1 = Vector3(a, b, c)
n2 = Vector3(d, e, f)
print(n1 + n2)
print(n1 - n2)
print(n1 * 3)
print(n1.length())
