import sqlite3
import pandas as pd
connection = sqlite3.connect('bd2.sqlite')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS peoples
              (id INTEGER PRIMARY KEY, peoples_id TEXT, name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders
              (id INTEGER PRIMARY KEY, orders_id TEXT, customer_id TEXT, price TEXT, FOREIGN KEY (orders_id) REFERENCES peoples (peoples_id) 
              ON UPDATE CASCADE ON DELETE CASCADE)''')

# insert1 = "INSERT INTO peoples(peoples_id, name) VALUES('111', 'Ivanov' );"
# insert2 = "INSERT INTO orders(orders_id, customer_id, price) VALUES(555, 111, 2400);"
#
# insert3 = "INSERT INTO peoples(peoples_id, name) VALUES('122', 'Mamicheva' );"
# insert4 = "INSERT INTO orders(orders_id, customer_id, price) VALUES(888, 122, 3000);"
# insert5 = "INSERT INTO peoples(peoples_id, name) VALUES('122', 'Mamicheva' );"
# insert6 = "INSERT INTO orders(orders_id, customer_id, price) VALUES(777, 122, 1800);"
#
# cursor.execute(insert1)
# cursor.execute(insert2)
# cursor.execute(insert3)
# cursor.execute(insert4)
# cursor.execute(insert5)
# cursor.execute(insert6)
connection.commit()

# print("Задание 3")
# #Задание 3
# answer = pd.read_sql("SELECT name, peoples_id, orders.orders_id, orders.customer_id, orders.price "
#                      "FROM peoples JOIN orders ON orders.id=peoples.id", connection)
# print(answer)

print("Задание 4. Вывести клиентов с номером заказа 122")
#Задание 4
choice = pd.read_sql("SELECT orders.customer_id, name, orders.orders_id, orders.price "
                     "FROM peoples JOIN orders ON orders.id=peoples.id WHERE orders.customer_id = 122", connection)
print(choice)
connection.close()
