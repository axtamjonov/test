import sqlite3

con = sqlite3.connect("medicine.db")
cursor = con.cursor()
cursor.execute('''create table if not exists medicine(id int, name text, deadline int, narxi text)''')
cursor.execute('''insert into medicine (id, name, deadline, narxi) values (00, "trimol" ,2025, "2000ming" )''')
cursor.execute('''insert into medicine (id, name, deadline, narxi) values (01, "pratstamol" ,2027, "2500ming" )''')
cursor.execute('''insert into medicine (id, name, deadline, narxi) values (02, "mezim" ,2027, "3500ming" )''')
name = input("dorini nomini kiriting: ")
cursor.execute('''select * from medicine where name==[name]''')
result1 = cursor.fetchall()
for el in result1:
    if name in el:
        print("Mana malumotlar")
        print(f"saqlash muddati {el[2]}")
        print(f"narxi {el[3]}")
con.commit()
def hello():
    pass
def hasan():
    ...
def husan():
    ...
