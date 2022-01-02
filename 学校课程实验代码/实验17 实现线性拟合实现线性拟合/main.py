"""
数据拟合点如下：
x0 = [75, 70, 65, 60, 55,50,45,40,35,30]
y0 = [22.44, 22.17, 21.74, 21.37, 20.92,20.67,20.32,20.05,19.84,19.59]
"""
# 根据图中数据，利用plt.scatter画出散点图（红点）。
import numpy as np
import pylab as pl
from matplotlib import font_manager as fm
from scipy import optimize


def demo1():
    x0 = [75, 70, 65, 60, 55, 50, 45, 40, 35, 30]
    y0 = [22.44, 22.17, 21.74, 21.37, 20.92, 20.67, 20.32, 20.05, 19.84, 19.59]
    pl.scatter(x0, y0, 25, "red")
    pl.show()


# 直线方程函数
def f_1(x, A, B):
    return A * x + B


def demo2():
    x0 = [75, 70, 65, 60, 55, 50, 45, 40, 35, 30]
    y0 = [22.44, 22.17, 21.74, 21.37, 20.92, 20.67, 20.32, 20.05, 19.84, 19.59]
    A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
    x1 = np.arange(30, 78, 1)
    y1 = A1 * x1 + B1
    pl.plot(x1, y1, "blue")
    pl.scatter(x0, y0, 5, "red")
    pl.show()


if __name__ == "__main__":
    # demo1()
    demo2()
