import sqlite3
#crear las tablas de datos
con = sqlite3.connect(r"C:\Users\mizai\Desktop\PYTHON APLICADO A LA MINERIA ISE ACADEMY\ejercicios\base de datos\tablaDB.db")
con.execute("create table if not exists alumnos(dni int primary key, nombre text not null, apellido text not null, estado boolean default true)") 
con.execute("create table if not exists cursos(id integer primary key autoincrement, nombre text not null, apellido text)") 
con.execute("create table if not exists matriculas(id integer primary key autoincrement, dni int not null, curso_id int not null)") 



nombre_curso = "algebra", "trigonometria", "programacion", "aritmetica"    #tupla

for i in nombre_curso:
    con.execute(f"insert into cursos (nombre) values ('{i}') ")
con.commit()

con.close()

print("tablaDB creada con exito")


