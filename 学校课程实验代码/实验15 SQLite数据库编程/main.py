import os
import time
from os import listdir

import xlwt
import random


# 生成10个EXCEL文件，每个文件包含5列数据，其中每个单元格的数据内容都是随机生成的，且每个文件的数据行数都是不同的。
def demo1():
    row_total = 2
    for i in range(10):
        work_book = xlwt.Workbook(encoding='utf-8')
        rows = random.randrange(0, 10, 1)
        sheet = work_book.add_sheet('sheet表名')
        for row in range(rows):
            for col in range(5):
                sheet.write(row, col, random.randint(1, 1000))
        work_book.save(f'Excel表{i + 1}.xls')
        row_total += 1

# （二）创建SQLite数据库，其结构和EXCEL文件相符合，然后把生成的10个EXCEL数据导入到这个数据库中。
# （）输出程序的导入速度，即平均每秒插入多少条记录（QPS）。
def demo2():
    import sqlite3
    import xlrd
    xlsxs = ('xls\\' + fn for fn in listdir('xls'))
    with sqlite3.connect('test.db') as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS xls")
        cur.execute("CREATE TABLE xls(one TEXT,two TEXT, three TEXT, four TEXT, five TEXT)")
        for xlsx in xlsxs:
            # 打开文件excel
            workBook = xlrd.open_workbook(xlsx)
            # 打开表格
            table = workBook.sheets()[0]
            # 计算文档有多少行
            all_row = table.nrows
            total_records = 0
            start_time = time.time()
            for i in range(0, all_row):
                data = table.row_values(i)
                cur.execute('''insert into xls values('%s','%s','%s','%s','%s')''' % (
                    data[0], data[1], data[2], data[3], data[4]))
                total_records += 1
            delta = time.time() - start_time
            print(f"QPS:{total_records / delta}")
            conn.commit()


if __name__ == "__main__":
    # demo1()
    demo2()
