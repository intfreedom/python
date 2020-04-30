import tkinter
import tushare as ts
import tkinter as tk
from tkinter.constants import *
import datetime


# window = tk.Tk()
# window.title('my window')
# window.geometry('300x100')
# datetime.datetime.now()
# window.after(100,window.__str__())
# L = tk.Label(window, text=str, bg='green', font=('Arial', 12), width=15, height=2)
#
# L.pack()    # 固定窗口位置
#
# window.mainloop()


class Questions(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        self.wm_title('CSSE1001 Queue')
        self.configure(background='white')
        self.wm_minsize(10, 10)  # 设置窗口最小化大小
        self.wm_maxsize(600, 500)  # 设置窗口最大化大小
        self.resizable(width=True, height=True)  # 设置窗口宽度不可变，高度可变

        # tk = tkinter.Tk()
        # frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
        # frame.pack(fill=BOTH, expand=1)
        # label = tkinter.Label(frame, text="Hello, World")
        # label.pack(fill=X, expand=1)
        # button = tkinter.Button(frame, text="Exit", command=tk.destroy)
        # button.pack(side=BOTTOM)
        # tk.mainloop()

        self.run()
        self.refresh_data()
        self.mainloop()

    def refresh_data(self):
        ticket = '603993'
        this = ts.get_realtime_quotes(ticket)['price'][0]
        valueYClose = ts.get_hist_data('603993')['close'][0]
        p = float(this) / float(valueYClose)
        if p >= 1.03:
            self.configure(background='red')
        elif p >= 1.02:
            self.configure(background='gold')
        elif p > 0.98:
            self.configure(background='white')
        elif p > 0.97:
            self.configure(background='blue')
        elif p >= 0.88:
            self.configure(background='green')
        self.wm_title(string=this)
        self.after(100, self.refresh_data)  # 这里的10000单位为毫秒

    def run(self):
        pass


if __name__ == '__main__':
    question = Questions()





















