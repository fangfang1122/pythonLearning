import pickle

# （四）Pickle模块的使用:参考教材7.3.1,编写pickle文件的写入和读取
def write():
    f = open('sample_pickle.dat', 'wb')
    n = 7
    i = 1300000
    a = 99.222
    s = 'hello world'
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    tu = (1, 2, 3)
    coll = {1, 2, 3}
    dic = {'a': 'aaple', 'b': 'bbna', 'c': 'ccat'}
    try:
        pickle.dump(n, f)
        pickle.dump(i, f)
        pickle.dump(a, f)
        pickle.dump(s, f)
        pickle.dump(lst, f)
        pickle.dump(tu, f)
        pickle.dump(coll, f)
        pickle.dump(dic, f)
    except:
        print('写入异常')
    finally:
        f.close()


def read():
    f = open('sample_pickle.dat', 'rb')
    n = pickle.load(f)
    i = 0
    while i < n:
        x = pickle.load(f)
        print(x)
        i += 1
    f.close()


if __name__ == '__main__':
    write()
    read()
