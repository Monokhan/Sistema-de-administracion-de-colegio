import sqlite3

con = sqlite3.connect("uno.db") # establecer coneccion con la base de dato. se le puede dar cualquier  nombre
con.execute("create table if not exists alumnos(dni int primary key, nombre text not null, apellido text not null)") # aca es donde se executa la instruccion
#execute va a crear una tabla  *create table, con 3 columnas, la primera dni que solo recibe enteros, la segunda nombre que solo recibe texto, y la tercera apalledido que solo recibe texto
# la restriccion not null. es para que los campos no sean nulos si no ingresan nada *creo

con.execute("insert into alumnos(dni, nombre, apellido) values (?,?,?)", (5,"marcelo","reinoso"))  #insertar datos en la tabla
#  hay distintas formas de insertar informacion, una puede ser el metodo "f  de concadenar" u el usado esta vez de (?,?,?) que solo lo soporta o permite el 
nombre= "JUANCARLOSBODOQUE"
con.execute(f"update alumnos set nombre ='{nombre}'  where  dni = {5}") #ejemplo de actualizar y borrar un registro en especifico
con.commit()  

cur = con.execute("select * from alumnos")   #cur= es la variable
print(cur.fetchall()) #fetchall  retorna una lista con toda las filas de la tabla



con.close()   # cerrar la coneccion con la DB