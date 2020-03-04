from tkinter import *

def login():
    print("to do")

def send():
    print("to do")

def logger():
    print("to do")

if __name__ == '__main__':
    root = Tk()
    root.title("发送直播弹幕")#窗口标题
    root.geometry('300x100+600+300')#窗口大小位置 用x链接 +后面是位置
    label = Label(root, text="developped by shutongX & ztono", font=('微软雅黑'))
    label.grid(row=0, columnspan=3)  # 网格式布局
    button_tq = Button(root,text="登录",font=('微软雅黑',8),command=login())#点击按钮
    button_tq.grid(row=1,column=1)
    entry1 = Entry(root,text="账号", font=('微软雅黑'))#创建输入框
    entry2 = Entry(root, text="密码", font=('微软雅黑'))  # 创建输入框
    entry1.grid(row=1,column=0)#定位第1行3列
    entry2.grid(row=2,column=0)
    root.mainloop()
