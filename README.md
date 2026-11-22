<div align="center">

<img src="assets/banner.svg" width="100%" alt="Sistema de administración de colegio — Python y SQLite"/>

<br/>

<img src="https://img.shields.io/badge/Python-0b1220?style=for-the-badge&logo=python&logoColor=22d3ee" alt="Python"/>
<img src="https://img.shields.io/badge/SQLite-0b1220?style=for-the-badge&logo=sqlite&logoColor=a78bfa" alt="SQLite"/>

</div>

Aplicación de consola en Python para **administrar alumnos, cursos y matrículas** de un colegio sobre una base de datos **SQLite**. Ejercicio de práctica de Python con bases de datos.

## 🗄️ Modelo de datos

| Tabla | Campos |
|---|---|
| `alumnos` | `dni` (clave), `nombre`, `apellido`, `estado` (activo/retirado) |
| `cursos` | `id`, `nombre` — viene cargada con álgebra, trigonometría, programación y aritmética |
| `matriculas` | `id`, `dni`, `curso_id` |

## 🖥️ Menú

```
1- inserte un nuevo alumno.
2- retirar un alumno.
3- matricular un alumno al curso...
4- cursos y alumnos en nuestra base de dato.
5- salir de la app.
```

## 🚀 Cómo usarlo

```bash
python "creacion de la DB.py"           # crea tablaDB.db con las tablas y los cursos (ajusta la ruta)
python sistema_adeministracion_colegio.py
```

## 🧭 Estado

| Opción | Estado |
|---|---|
| Insertar alumno | ✅ Funciona |
| Retirar alumno | ⚠️ Falta `con.commit()`, por lo que el cambio no se guarda |
| Matricular alumno | ⚠️ Usa variables con nombres distintos (`tablaDB.db`, `id_curso`) y falla al ejecutarse |
| Listar cursos y alumnos | 🚧 Pendiente |

```
├── sistema_adeministracion_colegio.py   ← aplicación y menú
├── DB.py                                ← práctica de consultas SQLite (crear, insertar, actualizar)
├── creacion de la DB.py                 ← crea las tablas
├── Ambiente_pruebas.py                  ← pruebas de str.join
├── tablaDB.db                           ← base SQLite
└── assets/                              ← banner de este README
```

---

<div align="center">

Hecho por **[Marcelo Reinoso](https://github.com/Monokhan)** · datos aplicados a minería e infraestructura

</div>
