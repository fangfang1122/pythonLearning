import tkinter
import tkinter.messagebox
import re

root = tkinter.Tk()
root.geometry('320x370+400+100')
root.title('计算器')

contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(root, textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10, y=10, width=300, height=80)


def buttonClick(btn):
    content = contentVar.get()
    if content.startswith('.'):
        content = '0' + content

    if btn in '0123456789':
        content += btn
    elif btn == '.':
        print("content: ", content)
        print("sss  ", re.split(r'\+|-|\*|/', content))
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        print("lastPart: ", lastPart)
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误', '小数点太多了')
            return
        else:
            content += btn
    elif btn == 'C':
        content = ''
    elif btn == '=':
        try:
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == 'Sqrt':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', "表达式错误")
            return
    contentVar.set(content)


btnClear = tkinter.Button(root, text='Clear', command=lambda: buttonClick('C'))
btnClear.place(x=10, y=100, width=220, height=50)

btnOperator = tkinter.Button(root, text='/', command=lambda x='/': buttonClick('/'))
btnOperator.place(x=229, y=100, width=81, height=50)

digits = list('789456123') + ['/']
index = 0
for row in range(3):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigits = tkinter.Button(root, text=d, command=lambda x=d: buttonClick(x))
        btnDigits.place(x=10 + col * 70, y=146 + row * 50, width=80, height=60)

# 0
btnDigits = tkinter.Button(root, text=0, command=lambda x='0': buttonClick('0'))
btnDigits.place(x=10 + 0 * 70, y=146 + 3 * 50, width=160, height=60)

# .
btnDigits = tkinter.Button(root, text='.', command=lambda x='.': buttonClick('.'))
btnDigits.place(x=10 + 2 * 70, y=146 + 3 * 50, width=80, height=60)

operators = ('*', '-', '+', '=', '/')
for index, operator in enumerate(('*', '-', '+', '=')):
    btnOperator = tkinter.Button(root, text=operator, command=lambda x=operator: buttonClick(x))
    btnOperator.place(x=229, y=146 + index * 50, width=81, height=60)

root.mainloop()
