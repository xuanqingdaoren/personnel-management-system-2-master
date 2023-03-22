from tkinter.filedialog import askopenfilename
import MySQLdb
import ttkbootstrap as ttk
import xlrd
import MenuViews
import tkinter as tk
from tkinter import messagebox
import FunctionViews
class Main:
    def __init__(self, master: ttk.Window):
        self.root = master
        self.root.geometry('1500x1000')
        self.root.title('人事管理系统 v0.0.1')
        self.Menu_page()
        self.shouye_1()

    def Menu_page(self):
        self.shouye = MenuViews.Shouye_Frame(self.root)
        self.incert = FunctionViews.IncertFrame(self.root)
        self.count = FunctionViews.Count_frame(self.root)
        self.menu2 = ttk.Menu(self.root, tearoff=0)
        self.menu2.add_command(label="使用说明", command=self.way_messagebox)
        self.menu2.add_separator()
        self.menu2.add_command(label="关   于", command=self.display_messagebox)
        menubar = ttk.Menu(self.root)

        menubar.add_command(label='首   页', command=self.shouye_1)
        menubar.add_command(label='添加员工', command=self.show_add)
        menubar.add_command(label='信息统计', command=self.show_count)
        menubar.add_cascade(label='软件帮助', menu=self.menu2)
        menubar.add_command(label='导入数据', command=self.input)
        menubar.add_command(label='退出系统', command=self.root.quit)
        self.root['menu'] = menubar
        self.root.config(menu=menubar)

    def show_add(self):
        self.incert.pack()
        self.shouye.pack_forget()
        self.count.pack_forget()

    def shouye_1(self):
        self.shouye.pack()
        self.incert.pack_forget()
        self.count.pack_forget()

    def show_count(self):
        self.count.pack()
        self.shouye.pack_forget()
        self.incert.pack_forget()

    def display_messagebox(self):
        message = '人事管理系统 v0.0.1|2023.3.18' + '\r' + 'Powered by 王喆焓' + '\r' + 'Copyright © 2000–2023 Google'
        tk.messagebox.showinfo(title='关于', message=message)

    def way_messagebox(self):
        message = '注意事项' + '\r' + '1)、导入时后缀名应为.xls!' + '\r' + '2)、导出的文件后缀为.xlsx'
        tk.messagebox.showinfo(title='使用说明', message=message)

    def input(self):
        filename = tk.StringVar()
        filepath = askopenfilename()  # 选择打开什么文件，返回文件名
        filename.set(filepath)  # 设置变量filename的值
        data = xlrd.open_workbook(filename.get())
        table = data.sheets()[0]
        rows = table.nrows
        data = []
        for v in range(1, rows):
            values = table.row_values(v)
            data.append(
                (
                    {
                        "id": str(values[0]),
                        "name": str(values[1]),
                        "password": str(values[2]),
                        "department": str(values[3]),
                        "position": str(values[4]),
                        "degree": str(values[5]),
                        "phone number": str(values[6]),
                        "age": str(values[7]),
                        "salary": str(values[8]),
                        "performance": str(values[9]),
                        "gender": str(values[10]),
                        "time": str(values[11])
                    }
                )
            )
        for i in data:
            data1 = []
            data1.append(i['id'])
            data1.append(i['name'])
            data1.append(i['password'])
            data1.append(i['department'])
            data1.append(i['position'])
            data1.append(i['degree'])
            data1.append(i['phone number'])
            data1.append(i['age'])
            data1.append(i['salary'])
            data1.append(i['performance'])
            data1.append(i['gender'])
            data1.append(i['time'])
            con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', password='1201612425')
            c = con.cursor()
            c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", data1)
            con.commit()



if __name__ == '__main__':
    root = ttk.Window(themename='solar')
    Main(root)
    root.mainloop()
