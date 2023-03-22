import tkinter as tk
from tkinter import ttk
import db
import MySQLdb

class IncertFrame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.password = tk.StringVar()
        self.department = tk.StringVar()
        self.position = tk.StringVar()
        self.degree = tk.StringVar()
        self.phone_number = tk.StringVar()
        self.age = tk.StringVar()
        self.salary = tk.StringVar()
        self.performance = tk.StringVar()
        self.gender = tk.StringVar()
        self.time = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)
        ttk.Label(self, text='工   号:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=1, column=2, pady=10)
        ttk.Label(self, text='姓   名:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        ttk.Label(self, text='密   码:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.password).grid(row=3, column=2, pady=10)
        ttk.Label(self, text='部   门:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.department).grid(row=4, column=2, pady=10)
        ttk.Label(self, text='职   位:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.position).grid(row=5, column=2, pady=10)
        ttk.Label(self, text='学   历:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.degree).grid(row=6, column=2, pady=10)
        ttk.Label(self, text='电话号码:').grid(row=7, column=1, pady=10)
        tk.Entry(self, textvariable=self.phone_number).grid(row=7, column=2, pady=10)
        ttk.Label(self, text='年   龄:').grid(row=8, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=8, column=2, pady=10)
        ttk.Label(self, text='工   资:').grid(row=9, column=1, pady=10)
        tk.Entry(self, textvariable=self.salary).grid(row=9, column=2, pady=10)
        ttk.Label(self, text='绩   效:').grid(row=10, column=1, pady=10)
        tk.Entry(self, textvariable=self.performance).grid(row=10, column=2, pady=10)
        ttk.Label(self, text='性   别:').grid(row=11, column=1, pady=10)
        tk.Entry(self, textvariable=self.gender).grid(row=11, column=2, pady=10)
        ttk.Label(self, text='入职时间:').grid(row=12, column=1, pady=10)
        e = tk.Entry(self,  textvariable=self.time)
        e.grid(row=12, column=2, pady=10)
        e.delete(0, "end")
        e.insert(0, "如：2002-01-01")
        ttk.Button(self, text='录入', command=self.recode_info).grid(row=13, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=14, column=2, pady=10)

    def recode_info(self):
        data = []
        data.append(self.id.get())
        data.append(self.name.get())
        data.append(self.password.get())
        data.append(self.department.get())
        data.append(self.position.get())
        data.append(self.degree.get())
        data.append(self.phone_number.get())
        data.append(self.age.get())
        data.append(self.salary.get())
        data.append(self.performance.get())
        data.append(self.gender.get())
        data.append(self.time.get())
        # print(data)
        con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', password='1201612425')
        cursor = con.cursor()
        cursor.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", data)
        # 提交
        con.commit()
        self.status.set('录入数据成功')

class Find_frame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.status = tk.StringVar()
        self.find_view()
        self.creat_page()

    def find_view(self):
        tk.Label(self).pack(pady=10)
        ttk.Label(self, text='工   号:').pack(pady=10)
        tk.Entry(self, textvariable=self.id).pack(pady=10)
        ttk.Label(self, text='姓   名:').pack(pady=10)
        tk.Entry(self, textvariable=self.name).pack(pady=10)
        ttk.Button(self, text='查询', command=self.find_info).pack(pady=10)
        tk.Label(self, textvariable=self.status).pack(pady=10)
        tk.Label(self, text='请在工号与姓名中二选一进行查询！').pack(pady=10)

    def creat_page(self):
        columns = ('department', 'name', 'id', 'password', 'gender', 'age', 'performance', 'phone number', 'position', 'degree', 'salary', 'time')
        columns_values = ('部门', '姓名', '工号', '密码', '性别', '年龄', '绩效', '电话号码', '职位', '学历', '工资', '入职时间')
        ybar = tk.Scrollbar(self, orient='vertical')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns, yscrollcommand=ybar.set)
        ybar['command'] = self.tree_view.yview
        self.tree_view.column('department', width=80, anchor='center')
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('id', width=100, anchor='center')
        self.tree_view.column('gender', width=50, anchor='center')
        self.tree_view.column('password', width=110, anchor='center')
        self.tree_view.column('age', width=50, anchor='center')
        self.tree_view.column('performance', width=80, anchor='center')
        self.tree_view.column('phone number', width=130, anchor='center')
        self.tree_view.column('position', width=110, anchor='center')
        self.tree_view.column('degree', width=90, anchor='center')
        self.tree_view.column('salary', width=110, anchor='center')
        self.tree_view.column('time', width=110, anchor='center')
        self.tree_view.heading('department', text='部门')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('id', text='工号')
        self.tree_view.heading('gender', text='性别')
        self.tree_view.heading('password', text='密码')
        self.tree_view.heading('age', text='年龄')
        self.tree_view.heading('performance', text='绩效')
        self.tree_view.heading('phone number', text='电话号码')
        self.tree_view.heading('position', text='职位')
        self.tree_view.heading('degree', text='学历')
        self.tree_view.heading('salary', text='工资')
        self.tree_view.heading('time', text='入职时间')
        self.tree_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ybar.pack(anchor=tk.E, side=tk.RIGHT, fill=tk.Y)
        ybar.config(command=self.tree_view.yview)
        self.show_data_frame()
        ttk.Button(self, text='刷新数据', command=self.show_data_frame).pack()

    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        people = db.db_1()
        index = 0
        for stu in people:
            self.tree_view.insert('', index + 1, values=(
                stu['department'], stu['name'], stu['id'], stu['password'], stu['gender'], stu['age'], stu['performance'], stu['phone number'], stu['position'], stu['degree'], stu['salary'], stu['time']
            ))

    def find_info(self):
        people = db.db_1()
        for i in people:
            if i['id'] == self.id.get():
                self.status.set('查询成功,有工号为{}的人'.format(self.id.get()))
            elif i['name'] == self.name.get():
                self.status.set('查询成功,有姓名为{}的人'.format(self.name.get()))
            else:
                self.status.set('查询失败,无此人')

class Delete_frame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.id = tk.StringVar()
        self.status = tk.StringVar()
        self.delete_view()

    def delete_view(self):
        tk.Label(self).grid(row=0, pady=50)
        ttk.Label(self, text='请输入需要删除人的工号:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=1, column=2, pady=10)
        ttk.Button(self, text='删除', command=self.delete_info).grid(row=2, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=3, column=2, pady=10)

    def delete_info(self):
        people = db.db_1()
        for i in people:
            if i['id'] == self.id.get():
                con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root',
                                      password='1201612425')
                cursor = con.cursor()
                na = (self.id.get(),)
                sql = "DELETE FROM Suppliers WHERE Supplier_id=%s;"
                cursor.execute(sql, na)
                # 提交
                con.commit()
                self.status.set('删除成功！')
            else:
                self.status.set('删除失败，没有该工号，请重试!')

class Change_frame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.password = tk.StringVar()
        self.department = tk.StringVar()
        self.position = tk.StringVar()
        self.degree = tk.StringVar()
        self.phone_number = tk.StringVar()
        self.age = tk.StringVar()
        self.salary = tk.StringVar()
        self.performance = tk.StringVar()
        self.gender = tk.StringVar()
        self.time = tk.StringVar()
        self.status = tk.StringVar()
        self.change_page()

    def change_page(self):
        tk.Label(self, text='工号要存在！且所有空均需要填写！').grid(row=0, column=1, pady=10)
        ttk.Label(self, text='工   号:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=1, column=2, pady=10)
        ttk.Label(self, text='姓   名:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        ttk.Label(self, text='密   码:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.password).grid(row=3, column=2, pady=10)
        ttk.Label(self, text='部   门:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.department).grid(row=4, column=2, pady=10)
        ttk.Label(self, text='职   位:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.position).grid(row=5, column=2, pady=10)
        ttk.Label(self, text='学   历:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.degree).grid(row=6, column=2, pady=10)
        ttk.Label(self, text='电话号码:').grid(row=7, column=1, pady=10)
        tk.Entry(self, textvariable=self.phone_number).grid(row=7, column=2, pady=10)
        ttk.Label(self, text='年   龄:').grid(row=8, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=8, column=2, pady=10)
        ttk.Label(self, text='工   资:').grid(row=9, column=1, pady=10)
        tk.Entry(self, textvariable=self.salary).grid(row=9, column=2, pady=10)
        ttk.Label(self, text='绩   效:').grid(row=10, column=1, pady=10)
        tk.Entry(self, textvariable=self.performance).grid(row=10, column=2, pady=10)
        ttk.Label(self, text='性   别:').grid(row=11, column=1, pady=10)
        tk.Entry(self, textvariable=self.gender).grid(row=11, column=2, pady=10)
        ttk.Label(self, text='入职时间:').grid(row=12, column=1, pady=10)
        e = tk.Entry(self, textvariable=self.time)
        e.grid(row=12, column=2, pady=10)
        e.delete(0, "end")
        e.insert(0, "如：2002-01-01")
        ttk.Button(self, text='修改', command=self.change_info).grid(row=13, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=14, column=2, pady=10)

    def change_info(self):
        data = []
        data.append(self.name.get())
        data.append(self.password.get())
        data.append(self.department.get())
        data.append(self.position.get())
        data.append(self.degree.get())
        data.append(self.phone_number.get())
        data.append(self.age.get())
        data.append(self.salary.get())
        data.append(self.performance.get())
        data.append(self.gender.get())
        data.append(self.time.get())
        data.append(self.id.get())
        # print(data)
        con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', password='1201612425')
        cursor = con.cursor()
        cursor.execute("""UPDATE Suppliers SET Supplier_name=%s,Supplier_password=%s,Supplier_department=%s,\
        Supplier_post=%s,Supplier_edu=%s,Supplier_telephone=%s,Supplier_age=%s,Supplier_salary=%s,\
        Supplier_performance=%s,Supplier_gender=%s,Supplier_time=%s WHERE Supplier_id=%s;""", data)
        # 提交
        con.commit()
        self.status.set('修改数据成功')

class Count_frame(tk.Frame):
    def __init__(self, top):
        super().__init__(top)
        self.age = tk.StringVar()
        self.performance = tk.StringVar()
        self.department = tk.StringVar()
        self.edu = tk.StringVar()
        self.status = tk.StringVar()
        self.status2 = tk.StringVar()
        self.status3 = tk.StringVar()
        self.status1 = tk.StringVar()
        self.count_page()

    def count_page(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='年龄查询:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=1, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_age).grid(row=1, column=3, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=1, column=4, pady=10)

        tk.Label(self, text='绩效查询:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.performance).grid(row=2, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_performance).grid(row=2, column=3, pady=10)
        tk.Label(self, textvariable=self.status1).grid(row=2, column=4, pady=10)

        tk.Label(self, text='部门查询:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.department).grid(row=3, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_department).grid(row=3, column=3, pady=10)
        tk.Label(self, textvariable=self.status2).grid(row=3, column=4, pady=10)

        tk.Label(self, text='学历查询:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.edu).grid(row=4, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_edu).grid(row=4, column=3, pady=10)
        tk.Label(self, textvariable=self.status3).grid(row=4, column=4, pady=10)

    def count_age(self):
        people = db.db_1()
        a = 0
        for i in people:
            if self.age.get() == str(i['age']):
                a += 1
        if a != 0:
            self.status.set('%s共有%s项数据' % (self.age.get(), a))
        else:
            self.status.set('未查询到数据!')

    def count_performance(self):
        people = db.db_1()
        a = 0
        for i in people:
            if self.performance.get() == str(i['performance']):
                a += 1
        if a != 0:
            self.status1.set('%s共有%s项数据' % (self.performance.get(), a))
        else:
            self.status1.set('未查询到数据!')

    def count_department(self):
        people = db.db_1()
        a = 0
        for i in people:
            if self.department.get() == str(i['department']):
                a += 1
        if a != 0:
            self.status2.set('%s共有%s项数据' % (self.department.get(), a))
        else:
            self.status2.set('未查询到数据!')

    def count_edu(self):
        people = db.db_1()
        a = 0
        for i in people:
            if str(self.edu.get()) == str(i['degree']):
                a += 1
        if a != 0:
            self.status3.set('%s共有%s项数据' % (self.edu.get(), a))
        else:
            self.status3.set('未查询到数据!')
