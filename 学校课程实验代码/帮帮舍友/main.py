def demo1():
    num = []  # 初始化列表
    while (1):
        n = input("请输入一个数字：")  # 输入数字
        if n == 'Q':  # 判断输入是否为Q退出
            break
        else:
            if n.isdigit():  # 判断输入内容是否为数字
                n = float(n)  # 转换为浮点类型
                num.append(n)  # 加入列表尾部
            else:  # 如果输入既不为数字也不为Q,则提醒输入数字！
                print("请输入数字！")
                continue

    print(f"您输入的列表长度：{len(num)}")  # 打印输出列表的长度
    num.sort()  # 调用sort内置函数排序
    print(f"排序后的列表：{num}")  # 打印输出排序后的列表


def demo2():
    dict1 = {'name': '丁一', 'age': 19, 'gender': '男', 'major': '汽车服务工程', 'score': 85}  # 创建字典
    dict2 = {'name': '贾二', 'age': 18, 'gender': '女', 'major': '汽车服务工程', 'score': 92}  # 创建字典
    dict3 = {'name': '张三', 'age': 20, 'gender': '男', 'major': '车辆工程', 'score': 95}  # 创建字典
    dict4 = {'name': '李四', 'age': 19, 'gender': '男', 'major': '车辆工程', 'score': 80}  # 创建字典
    list_dict = [dict1, dict2, dict3, dict4]  # 定义字典列表，以便于遍历所有字典
    A = []  # 定义名字列表，存储创建大于等于90分的学生名字
    major_carService = []  # 定义汽车服务工程专业列表
    major_carProject = []  # 定义车辆工程专业列表
    total_score = 0  # 定义所有学生成绩总和，以便于最后求平均分数
    for dict in list_dict:  # 遍历所有字典
        for key, value in dict.items():  # 遍历该字典的键和值
            # print(f"{key}:{value}") #打印键和值
            if key == 'score':  # 如果该键为分数
                total_score += value  # 则求和所有学生分数
                if value >= 90:  # 如果分数大于90
                    A.append(dict.get('name'))  # 讲该学生名字加入A列表
                    print(f"{dict.get('name')} 同学成绩大于等于90分，分数为{value}分")

        if dict.get('major') == '汽车服务工程':
            major_carService.append(dict)
        else:
            major_carProject.append(dict)

    average_score = total_score / 4
    print(f"所有同学平均分为：{average_score}")
    for dict in list_dict:
        dict['difference'] = dict.get('score') - average_score


import xlsxwriter

ROW = 1  # 表格的row，用于每次添加记录后+1，相当于游标


def demo3():
    o = xlsxwriter.Workbook('sale.xlsx')  # 创建表格
    e = o.add_worksheet('Sheet1')  # 创建工作表
    e.write(0, 0, '姓名')  # 定义表格第一行标签名字
    e.write(0, 1, '数量')  # 定义表格第一行标签数量
    e.write(0, 2, '总价')  # 定义表格第一行标签总价

    # 奶茶店，客户姓名，数量，配料
    def naichadian(name, amount, peiLiao):
        print(f'客户名：{name}，购买数量：{amount} 杯，配料：{peiLiao}')
        total = amount * count_money(peiLiao)  # 计算本次购买总价
        global ROW
        e.write(ROW, 0, name)  # 写入工作表中
        e.write(ROW, 1, amount)
        e.write(ROW, 2, total)
        ROW += 1  # 全局行数加1

    # 价格计算
    def count_money(pl):
        total = 0
        dict = {
            '乌龙茶': 12,
            '茉莉花茶': 9,
            '绿茶': 10,
            '鲜奶': 3,
            '珍珠': 2,
            '蜂蜜': 5
        }
        for item in pl:
            total += dict[item]
        print(f'总价：{total} 元')
        return total

    _pl = ['乌龙茶', '茉莉花茶', '绿茶', '鲜奶', '珍珠', '蜂蜜']
    naichadian('吴纪峰', 1000, _pl)
    naichadian('吴纪峰', 2000, _pl)

    o.close()  # 表格关闭


if __name__ == '__main__':
    # demo1()
    # demo2()
    demo3()
