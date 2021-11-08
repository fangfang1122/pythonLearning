from os.path import isdir, join, splitext, getsize
from os import remove, listdir
import sys
# （三）实验指导书-27:磁盘垃圾文件清理器


# 指定要删除的文件类型
filetypes = ['.tmp', '.log', '.obj', 'txt']


def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)
        elif splitext(temp)[1] in filetypes or getsize(temp) == 0:
            remove(temp)
            print(temp, ' deleted...')


# directory = sys.argv[1]
directory = input('请输入要删除的文件夹名称：')
delCertainFiles(directory)
