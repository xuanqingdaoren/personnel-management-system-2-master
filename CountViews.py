import matplotlib.pyplot as plt
import db
def Show_age():
    data = db.db_1()
    age_db = []
    for i in data:
        age_db.append(i['age'])
    age_db_1 = []
    for i in data:
        if i['age'] not in age_db_1:
            age_db_1.append(i['age'])
    a = {}
    for i in age_db:
        if age_db.count(i) > 1:
            a[i] = age_db.count(i)
        elif age_db.count(i) == 1:
            a[i] = 1
    q = []
    for i in range(len(a)):
        q.append(0.01)
    # print(q)
    value = []
    for i in a.values():
        value.append(i)
    # print(value)
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 设置中文显示
    plt.figure(figsize=(6, 6))
    # 将画布设定为正方形，则绘制的饼图是正圆
    label = age_db_1
    # 定义饼图的标签，标签是列表
    explode = q
    values = value
    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')
    # 绘制饼图
    plt.title('年龄组成饼图')
    plt.show()

def Show_degree():
    data = db.db_1()
    age_db = []
    for i in data:
        age_db.append(i['degree'])
    age_db_1 = []
    for i in data:
        if i['degree'] not in age_db_1:
            age_db_1.append(i['degree'])
    a = {}
    for i in age_db:
        if age_db.count(i) > 1:
            a[i] = age_db.count(i)
        elif age_db.count(i) == 1:
            a[i] = 1
    q = []
    for i in range(len(a)):
        q.append(0.01)
    # print(q)
    value = []
    for i in a.values():
        value.append(i)
    # print(value)
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 设置中文显示
    plt.figure(figsize=(6, 6))
    # 将画布设定为正方形，则绘制的饼图是正圆
    label = age_db_1
    # 定义饼图的标签，标签是列表
    explode = q
    values = value
    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')
    # 绘制饼图
    plt.title('学历组成饼图')
    plt.show()

def Show_gender():
    data = db.db_1()
    age_db = []
    for i in data:
        age_db.append(i['gender'])
    age_db_1 = []
    for i in data:
        if i['gender'] not in age_db_1:
            age_db_1.append(i['gender'])
    a = {}
    for i in age_db:
        if age_db.count(i) > 1:
            a[i] = age_db.count(i)
        elif age_db.count(i) == 1:
            a[i] = 1
    q = []
    for i in range(len(a)):
        q.append(0.01)
    # print(q)
    value = []
    for i in a.values():
        value.append(i)
    # print(value)
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 设置中文显示
    plt.figure(figsize=(6, 6))
    # 将画布设定为正方形，则绘制的饼图是正圆
    label = age_db_1
    # 定义饼图的标签，标签是列表
    explode = q
    values = value
    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')
    # 绘制饼图
    plt.title('性别组成饼图')
    plt.show()

def Show_department():
    data = db.db_1()
    age_db = []
    for i in data:
        age_db.append(i['department'])
    age_db_1 = []
    for i in data:
        if i['department'] not in age_db_1:
            age_db_1.append(i['department'])
    a = {}
    for i in age_db:
        if age_db.count(i) > 1:
            a[i] = age_db.count(i)
        elif age_db.count(i) == 1:
            a[i] = 1
    q = []
    for i in range(len(a)):
        q.append(0.01)
    # print(q)
    value = []
    for i in a.values():
        value.append(i)
    # print(value)
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 设置中文显示
    plt.figure(figsize=(6, 6))
    # 将画布设定为正方形，则绘制的饼图是正圆
    label = age_db_1
    # 定义饼图的标签，标签是列表
    explode = q
    values = value
    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')
    # 绘制饼图
    plt.title('部门组成饼图')
    plt.show()
