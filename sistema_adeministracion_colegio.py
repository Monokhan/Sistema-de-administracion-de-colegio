import os
import sqlite3

# Ruta de la base de datos: siempre junto a este archivo, sin importar desde donde se ejecute
tablaDB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tablaDB.db")


#funcion para matricular un alumno, retorna el codigo de la matricula
def matricular_alumno(tablaDB, dni, id_curso):
    con = sqlite3.connect(tablaDB)
    cur = con.execute("insert into matriculas(dni, curso_id) values (?, ?)", (dni, id_curso))
    con.commit()
    var = cur.lastrowid   # id de la matricula recien creada
    con.close()
    return var


#seleccionar informacion respecto a alumnos o tabla
def buscar_one(tablaDB, tabla, *campos):
    con = sqlite3.connect(tablaDB)
    text = ",".join(campos)   # concatena todos los argumentos que estan en campos y los separa con una coma
    cur = con.execute(f"select {text} from {tabla}")  #consulta dinamica, en text estan almacenados todos los argumentos de campos
    var = cur.fetchone()
    con.close()
    return var


#buscar muchos elementos
def buscar_muchos(tablaDB, tabla, *campos):
    con = sqlite3.connect(tablaDB)
    text = ",".join(campos)
    cur = con.execute(f"select {text} from {tabla}")
    var = cur.fetchall()
    con.close()
    return var


#verificar si un alumno existe y esta activo
def alumno_activo(tablaDB, dni):
    con = sqlite3.connect(tablaDB)
    cur = con.execute("select estado from alumnos where dni = ?", (dni,))
    fila = cur.fetchone()
    con.close()
    return fila is not None and bool(fila[0])


#verificar si un curso existe
def curso_existe(tablaDB, id_curso):
    con = sqlite3.connect(tablaDB)
    cur = con.execute("select 1 from cursos where id = ?", (id_curso,))
    fila = cur.fetchone()
    con.close()
    return fila is not None


#funcion para retirar alumnos
def retirar_alumno(tablaDB, dni):
    con = sqlite3.connect(tablaDB)
    cur = con.execute("update alumnos set estado = false where dni = ?", (dni,))  #actualizar campo de estado del alumno
    con.commit()   # sin commit el cambio no queda guardado
    filas = cur.rowcount
    con.close()
    if filas:
        print("ejecucion correcta, retirar alumno")
    else:
        print("no existe un alumno con ese dni")


#funcion para insertar alumnos en la DB
def insertar_alumno(tablaDB, dni, nombre, apellido):
    con = sqlite3.connect(tablaDB)
    try:
        con.execute("insert into alumnos(dni, nombre, apellido) values (?, ?, ?)", (dni, nombre, apellido))
        con.commit()
        print("ejecucion correcta insertar alumno")
    except sqlite3.IntegrityError:
        print("ya existe un alumno con ese dni")
    finally:
        con.close()


#funcion para listar cursos con sus alumnos matriculados
def listar_cursos_y_alumnos(tablaDB):
    con = sqlite3.connect(tablaDB)
    cursos = con.execute("select id, nombre from cursos order by id").fetchall()
    for id_curso, nombre_curso in cursos:
        alumnos = con.execute(
            "select a.dni, a.nombre, a.apellido, a.estado from matriculas m "
            "join alumnos a on a.dni = m.dni where m.curso_id = ? order by a.apellido",
            (id_curso,)).fetchall()
        print(f"\n[{id_curso}] {nombre_curso} - {len(alumnos)} alumno(s)")
        for dni, nombre, apellido, estado in alumnos:
            print(f"    {dni}  {nombre} {apellido}{'' if estado else '  (retirado)'}")
    sin_curso = con.execute(
        "select dni, nombre, apellido, estado from alumnos where dni not in (select dni from matriculas)").fetchall()
    if sin_curso:
        print("\nAlumnos sin matricula:")
        for dni, nombre, apellido, estado in sin_curso:
            print(f"    {dni}  {nombre} {apellido}{'' if estado else '  (retirado)'}")
    con.close()


#pedir un numero entero, repite la pregunta si el valor no es valido
def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("ingrese un numero valido")


#funcion menu registro
def menu():
    print("=======================================================================")
    print("1- inserte un nuevo alumno.")
    print("2- retirar un alumno.")
    print("3- matricular un alumno al curso...")
    print("4- cursos y alumnos en nuestra base de dato.")
    print("5- salir de la app.")
    print("=======================================================================")
    return pedir_entero("elija una opcion:")


#bucle condicional del menu
if __name__ == "__main__":
    if not os.path.exists(tablaDB):
        print("No se encontro tablaDB.db. Ejecute primero 'creacion de la DB.py'.")
        raise SystemExit(1)

    while True:
        opcion = menu()
        if opcion == 1:
            dni = pedir_entero("inserte el dni del alumno: ")
            nombre = input("inserte el nombre del alumno: ").strip()
            apellido = input("inserte el apellido del alumno: ").strip()
            if nombre and apellido:
                insertar_alumno(tablaDB, dni, nombre, apellido)
            else:
                print("nombre y apellido son obligatorios")

        elif opcion == 2:
            dni = pedir_entero("inserte el dni del alumno: ")
            retirar_alumno(tablaDB, dni)

        elif opcion == 3:
            dni = pedir_entero("inserte el dni del alumno: ")
            if not alumno_activo(tablaDB, dni):
                print("el alumno no existe o esta retirado")
                continue
            for id_curso, nombre_curso in buscar_muchos(tablaDB, "cursos", "id", "nombre"):
                print(f"  {id_curso} - {nombre_curso}")
            id_curso = pedir_entero("inserte el codigo del curso: ")
            if curso_existe(tablaDB, id_curso):
                cod_matricula = matricular_alumno(tablaDB, dni, id_curso)
                print("su codigo de matricula es", cod_matricula)
            else:
                print("el curso no existe")

        elif opcion == 4:
            listar_cursos_y_alumnos(tablaDB)

        elif opcion == 5:
            break

        else:
            print("opcion no valida")
