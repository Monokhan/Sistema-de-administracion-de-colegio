import os
import sqlite3

#crear las tablas de datos junto a este archivo
ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tablaDB.db")
con = sqlite3.connect(ruta)
con.execute("create table if not exists alumnos(dni int primary key, nombre text not null, apellido text not null, estado boolean default true)")
con.execute("create table if not exists cursos(id integer primary key autoincrement, nombre text not null, apellido text)")
con.execute("create table if not exists matriculas(id integer primary key autoincrement, dni int not null, curso_id int not null)")


nombre_curso = "algebra", "trigonometria", "programacion", "aritmetica"    #tupla

# insertar los cursos solo si no existen, para no duplicarlos al ejecutar de nuevo
for i in nombre_curso:
    existe = con.execute("select 1 from cursos where nombre = ?", (i,)).fetchone()
    if not existe:
        con.execute("insert into cursos (nombre) values (?)", (i,))
con.commit()

con.close()

print("tablaDB creada con exito")
