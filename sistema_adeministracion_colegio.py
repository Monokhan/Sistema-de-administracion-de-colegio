import sqlite3

#funcion para matricular un alumno
def matricular_alumno(tablaDB,dni,id_curso):
    con = sqlite3.connect(tablaDB)
    con.execute("insert into matriculas(dni, curso_id) values (?, ?)", (dni, id_curso))
    con.commit()
    cur = con.execute("select id from matriculas where dni=? and curso_id =?",(dni, id_curso) )   #posible error
    var = cur.fetchone
    con.close()
    return var


#seleccionar informacion respecto a alumnos o tabla 
def buscar_one (tablaDB, tabla, *campos):  
    con = sqlite3.connect(tablaDB)
    if len(campos) > 1:
        text = ",".join(campos)   # concadena todos los argumentos que estan en campos y los separa con una coma
    else:
        text = campos [0]
    cur = con.execute(f"select {text} from {tabla}") #consulta dinamica, en text estan almacenados todos los argum,entos de campos, separados por ','
    var = cur.fetchone()
    con.close()
    return var

#buscar muchos elementos
def buscar_muchos (tablaDB, tabla, *campos):  
    con = sqlite3.connect(tablaDB)
    if len(campos) > 1:
        text = ",".join(campos)   # concadena todos los argumentos que estan en campos y los separa con una coma
    else:
        text = campos [0]
    cur = con.execute(f"select {text} from {tabla}") #consulta dinamica, en text estan almacenados todos los argum,entos de campos, separados por ','
    var = cur.fetchall()
    con.close()
    return var    
    
#funcion para retirar alumnos
def retirar_alumno(tablaDB, dni): 
    con = sqlite3.connect(tablaDB)
    con.execute(f"update alumnos set estado = false where dni =?", (dni, )) #actualizar campo de estado del alumno
    con.close()
    print("ejecucion correcta, retirar alumno")
#funcion para insertar alumnos en la DB
def insertar_alumno(tablaDB, dni,nombre , apellido):
    con = sqlite3.connect(tablaDB)
    con.execute("insert into alumnos(dni, nombre, apellido) values (?, ?, ?)", (dni, nombre, apellido))
    con.commit()
    con.close()
    print("ejecucion correcta insertar alumno")


#funcion menu registro
def menu():
    print("=======================================================================")
    print("1- inserte un nuevo alumno.")
    print("2- retirar un alumno.")
    print("3- matricular un alumno al curso...")
    print("4- cursos y alumnos en nuestra base de dato.")
    print("5- salir de la app.")
    print("=======================================================================")
    opcion = int(input("elija una opcion:"))
    return opcion
#bucle condicional del menu
while True:
    opcion = menu()
    if  opcion ==1:
        dni = int(input("inserte el dni del alumno: "))
        nombre = input("inserte el nombre del alumno: ")
        apellido = input("inserte el apellido del alumno: ")
        insertar_alumno("tablaDB.db", dni, nombre, apellido)    #hacer validacion de datos

    elif  opcion  == 2:
        dni = int(input("inserte el dni del alumno: "))   
        retirar_alumno('tablaDB.db', dni)

    elif  opcion  == 3:
        variable_control = False   
        buscar_DNI = buscar_muchos(tablaDB.db, "alumnos", "dni", "nombre")
        dni = int(input("inserte el dni del alumno: "))  

        for i in buscar_DNI:
         if dni == i[0]:
                variable_control = True

        print(buscar_muchos(tablaDB, "cursos","id", "nombre"))
        curso = int(input("inserte el codigo del curso: "))

        if variable_control:
         cod_matricula = matricular_alumno(tablaDB, dni, id_curso)
         print("su codigo de matricula es", cod_matricula)
        else:
         print("el alumno no existe")   


    elif opcion == 4:
        pass
    elif opcion == 5:
        break



