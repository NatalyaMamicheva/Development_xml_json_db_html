import sqlite3
import pandas as pd

connection = sqlite3.connect('bd.sqlite')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS peoples
              (id INTEGER PRIMARY KEY, name TEXT, lastname TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS address
              (id INTEGER PRIMARY KEY, city TEXT, FOREIGN KEY (id) REFERENCES peoples (id))''')

# insert1 = "INSERT INTO peoples(name, lastname) VALUES('Ivan', 'Ivanov' );"
# insert2 = "INSERT INTO address(city) VALUES('Moscow' );"

# insert3 = "INSERT INTO peoples(name, lastname) VALUES('Natalia', 'Mamicheva' );"
# insert4 = "INSERT INTO address(city) VALUES('Samara' );"
#
# cursor.execute(insert1)
# cursor.execute(insert2)
# cursor.execute(insert3)
# cursor.execute(insert4)
connection.commit()

# print("Задание 3")
# # Задание 3
# answer = pd.read_sql("SELECT name, lastname, address.city FROM peoples JOIN address ON peoples.id=address.id",
#                      connection)
# print(answer)

print("Задание 4. Вывести людей из города Самара")
# Задание 4
choice = pd.read_sql("SELECT name, lastname, address.city FROM peoples JOIN address ON peoples.id=address.id "
                     "WHERE address.city = 'Samara'", connection)
print(choice)

connection.close()
