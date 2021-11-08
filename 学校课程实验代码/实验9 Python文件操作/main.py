import json


# （二）新建一个json文件内容如下, 编写程序将每个键值对输出
def demo2():
    with open('./demo.json', 'r', encoding='utf-8') as f:
        ret_dic = json.load(f)
        print(type(ret_dic))  # 结果 <class 'dict'>
        print(ret_dic)  # 结果 pengjunlee


if __name__ == "__main__":
    demo2()
