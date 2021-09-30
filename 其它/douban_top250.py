# -*- coding  = utf-8 -*-
# @Time : 2021/9/3 21:07
# @Author : fangfang
# @File : demo.py
# @Software : PyCharm


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL,获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    # 2.解析数据
    # 3.保存数据
    savepath = "豆瓣电影250爬取.xls"
    saveData(datalist, savepath)


# 影片详情链接的规则
finkLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）  --- r 是忽视后面的特殊字符
# 影片图片链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S忽略换行符
# 影片片名
findTile = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    dataList = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)  # 修改每个请求页面的start值
        html = askUrl(url)  # 保存网页源代码

        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查看符合要求的区域
            # print(item)
            data = []  # 保存每部电影的所有信息
            item = str(item)

            # 影片详情的链接
            link = re.findall(finkLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            title = re.findall(findTile, item)
            if (len(title) == 2):  # 可能有外语名
                data.append(title[0])
                otitle = title[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())

            dataList.append(data)  # 将处理好的一部电影信息放入list

    return dataList


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


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影top250')  # 创建工作表
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外国名', '评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print(f'第{i}条')
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)


if __name__ == "__main__":  # 当程序执行时
    main()
