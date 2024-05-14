import sqlite3

con = sqlite3.connect("medicine.db")
cursor = con.cursor()
cursor.execute('''create table if not exists medicine(id int, name text, deadline int, narxi text)''')
cursor.execute('''insert into medicine (id, name, deadline, narxi) values (00, "trimol" ,2025, "2000ming" )''')
cursor.execute('''insert into medicine (id, name, deadline, narxi) values (01, "pratstamol" ,2027, "2500ming" )''')
cursor.execute('''insert into medicine (id, name, deadline, narxi) values (02, "mezim" ,2027, "3500ming" )''')
name = input("dorini nomini kiriting: ")
