import MySQLdb

def db_1():
    con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', password='1201612425')
    c = con.cursor()
    c.execute("""SELECT * FROM Suppliers WHERE Supplier_performance > 0.0;""")
    rows = c.fetchall()
    db = []
    db_1 = []
    for i in rows:
        f = {}
        f['id'] = i[0]
        f['name'] = i[1]
        f['password'] = i[2]
        f['department'] = i[3]
        f['position'] = i[4]
        f['degree'] = i[5]
        f['phone number'] = i[6]
        f['age'] = i[7]
        f['salary'] = i[8]
        f['performance'] = i[9]
        f['gender'] = i[10]
        f['time'] = i[11]
        db.append(f)
    for i in db:
        if i not in db_1:
            db_1.append(i)
    return db_1



class Mysqldb:
    def __init__(self):
        self.people = db_1()
    def check_login(self, username, password):
        for user in self.people:
            if username == user['id']:
                if password == str(user['password']):
                    return True, '登陆成功'
                else:
                    return False, '密码不存在'
        return False, '登陆失败,用户不存在'

db = Mysqldb()
