# -*- coding  = utf-8 -*-
# @Time : 2021/7/17 20:45
# @Author : fangfang
# @File : demo9-timetable.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import xlwt  # 进行excel操作


def main():
    datalist = getData()
    savepath = "年级课程表.xls"
    saveData(datalist, savepath)


def askUrl(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/91.0.4472.124 Safari/537.36"
    }  # 用户代理，模拟机器类型
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 班级名称
className = re.compile(r'<nobr>(.*)</nobr>')  # 创建正则表达式对象，表示规则（字符串的模式）  --- r 是忽视后面的特殊字符
# 课程代码段
codeArea = re.compile(r'<td align="center" height="28" valign="top">(.*?)</td>', re.S)
# 课程信息
course = re.compile(r'<div class="kbcontent1" id="">(.*)</div>', re.S)


# 数据处理
def getData():
    dataList = []  # 全年级信息
    f = open('tbody.txt', "r", encoding='UTF-8') # 打开代码记事本
    html = f.read()
    f.close()
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('tr'):  # 每个班级的代码段遍历
        data = []  # 单个班级的课表信息，第一个元素为班级名称，其后为课程信息

        item = str(item)
        # print(item)

        class_name = re.findall(className, item)[0]  # 班级名称
        data.append(class_name)
        # print(class_name)

        for td in re.findall(codeArea, item):  # 所有节次遍历
            course_information = re.findall(course, td)
            if course_information:
                course_information = re.sub('<br/>', '\n', course_information[0])
            else:
                course_information = "该时间段无课程"
            # print(course_information)
            data.append(course_information)

        dataList.append(data)  # 将处理好的班级放入list

    # print(dataList)
    return dataList


# 生成表格
def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象

    alignment = xlwt.Alignment()  # Create Alignment  设置单元格对齐方式
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    alignment.wrap = 1  # 设置自动换行

    font = xlwt.Font()  # 为样式创建字体
    font.name = '宋体'

    style = xlwt.XFStyle()  # Create Style
    style.alignment = alignment  # Add Alignment to Style
    style.font = font

    for item in datalist:
        # print(item)
        sheet = workbook.add_sheet(item[0])  # 创建工作表

        row = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
        col = (' ', '0102', '0304', '0506', '0708', '0910', '1112')
        for i in range(0, 7):
            sheet.col(i + 1).width = 4400
            sheet.write(0, i + 1, row[i], style)  # 行 列 内容
            sheet.write(i, 0, col[i], style)

        now = 1
        for i in range(1, 8):  # 列
            for j in range(1, 7):  # 行
                # item[now] = re.sub('\n', '\r', item[now])
                sheet.write(j, i, item[now], style)
                now += 1

    workbook.save(savepath)


if __name__ == "__main__":  # 当程序执行时
    main()
    print("课程表生成完成")
