import MySQLdb
import csv
from datetime import datetime
input_file = './db.csv'
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', password='1201612425')
c = con.cursor()
file_reader = csv.reader(open(input_file, 'r', newline='', encoding='utf-8'))
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 11:
            data.append(str(row[column_index]))
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%Y'))
            a_date = a_date.strftime('%Y-%d-%m')
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", data)
con.commit()
print("")
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)

