import os
from tkinter.filedialog import asksaveasfilename, askopenfilename
import MySQLdb
import ttkbootstrap as ttk
import tkinter as tk
import FunctionViews
import db
import xlwt
import xlrd
import CountViews

class Shouye_Frame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.Function_bar()

    def Function_bar(self):
        ttk.Button(self, text='员工资料', command=self.Yuangong).pack(pady=100)
        ttk.Button(self, text='统计管理', command=self.Show_count_diagram).pack(pady=100)
        ttk.Button(self, text='实用工具', command=self.cmd_frame).pack(pady=100)

    def Yuangong(self):
        self.top = tk.Toplevel()
        self.top.title('员工资料')
        self.top.geometry('1500x1000')
        self.Yuangong_frame()
        self.show_incert()

    def Yuangong_frame(self):
        menubar = tk.Menu(self.top)
        self.incert = FunctionViews.IncertFrame(self.top)
        self.find = FunctionViews.Find_frame(self.top)
        self.delete = FunctionViews.Delete_frame(self.top)
        self.change = FunctionViews.Change_frame(self.top)
        self.count = FunctionViews.Count_frame(self.top)
        menubar.add_command(label='录入', command=self.show_incert)
        menubar.add_command(label='查询', command=self.show_find)
        menubar.add_command(label='删除', command=self.show_delete)
        menubar.add_command(label='修改', command=self.show_change)
        menubar.add_command(label='统计', command=self.show_count)
        menubar.add_command(label='导入', command=self.input)
        menubar.add_command(label='导出', command=self.output)
        menubar.add_command(label='退出', command=self.top.destroy)
        self.top['menu'] = menubar

    def show_incert(self):
        self.incert.pack()
        self.find.pack_forget()
        self.delete.pack_forget()
        self.change.pack_forget()
        self.count.pack_forget()

    def show_find(self):
        self.find.pack()
        self.incert.pack_forget()
        self.delete.pack_forget()
        self.change.pack_forget()
        self.count.pack_forget()

    def show_delete(self):
        self.delete.pack()
        self.find.pack_forget()
        self.incert.pack_forget()
        self.change.pack_forget()
        self.count.pack_forget()

    def show_change(self):
        self.change.pack()
        self.delete.pack_forget()
        self.find.pack_forget()
        self.incert.pack_forget()
        self.count.pack_forget()

    def show_count(self):
        self.count.pack()
        self.change.pack_forget()
        self.delete.pack_forget()
        self.find.pack_forget()
        self.incert.pack_forget()

    def output(self):
        dball = db.db_1()
        self.wb = xlwt.Workbook(encoding='utf-8')
        ws1 = self.wb.add_sheet('first')
        # 添加一个新表命名为‘first’
        ws1.write(0, 0, '工号')
        ws1.write(0, 1, '姓名')
        ws1.write(0, 2, '密码')
        ws1.write(0, 3, '部门')
        ws1.write(0, 4, '职位')
        ws1.write(0, 5, '学历')
        ws1.write(0, 6, '电话号码')
        ws1.write(0, 7, '年龄')
        ws1.write(0, 8, '工资')
        ws1.write(0, 9, '绩效')
        ws1.write(0, 10, '性别')
        ws1.write(0, 11, '入职时间')
        row = 1
        # 写入起始行
        for i in dball:
            ws1.write(row, 0, str(i['id']))
            ws1.write(row, 1, str(i['name']))
            ws1.write(row, 2, str(i['password']))
            ws1.write(row, 3, str(i['department']))
            ws1.write(row, 4, str(i['position']))
            ws1.write(row, 5, str(i['degree']))
            ws1.write(row, 6, str(i['phone number']))
            ws1.write(row, 7, str(i['age']))
            ws1.write(row, 8, str(i['salary']))
            ws1.write(row, 9, str(i['performance']))
            ws1.write(row, 10, str(i['gender']))
            ws1.write(row, 11, str(i['time']))
            row += 1
        filenewname = tk.StringVar()
        filenewpath = asksaveasfilename(defaultextension='.xls')
        filenewname.set(filenewpath)
        self.wb.save(str(filenewname.get()))

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


    def Show_count_diagram(self):
        self.top1 = tk.Toplevel()
        self.top1.title('统计图表')
        self.top1.geometry('500x200')
        self.Frame()

    def Frame(self):
        ttk.Button(self.top1, text='年龄统计图', command=CountViews.Show_age).pack()
        ttk.Button(self.top1, text='学历统计图', command=CountViews.Show_degree).pack()
        ttk.Button(self.top1, text='性别统计图', command=CountViews.Show_gender).pack()
        ttk.Button(self.top1, text='部门统计图', command=CountViews.Show_department).pack()

    def cmd_frame(self):
        self.top3 = tk.Toplevel()
        self.top3.title('实用工具')
        self.top3.geometry('500x200')
        self.show()

    def show(self):
        ttk.Button(self.top3, text='清理系统缓存', command=self.delete).pack()
        ttk.Button(self.top3, text='五子棋小游戏', command=self.game).pack()
        ttk.Button(self.top3, text='系统朗读', command=self.read).pack()
        ttk.Button(self.top3, text='hyper_v虚拟机环境配置', command=self.hyper_v).pack()

    def delete(self):
        os.system('start D:\pythonProject1\shanchu.bat')

    def game(self):
        os.system('start D:\pythonProject1\wuziqi.bat')

    def read(self):
        os.system('start D:\pythonProject1\Read.vbs')

    def hyper_v(self):
        os.system('start D:\pythonProject1\hyper_v.cmd')





