'''
Ejercicio 1
Objetivo: en este ejercicio crearemos una tabla, especificando los
campos; luego agregaremos un campo a la tabla creada
anteriormente. Para finalizar, utilizaremos sentencias de
manipulación de datos
Ingresa al sitio web: https://sqliteonline.com/
Selecciona el editor de SQLite, en el centro podrás ver un editor de
SQL.
1) Crea una tabla llamada CURSO con los atributos:
a. Código de curso (clave primaria, entero no nulo);
b. Nombre (varchar no nulo);
c. Descripción (varchar);
d. Turno (varchar no nulo).
1) Agrega un campo “cupo” de tipo numérico.
2) Inserta datos en la tabla:
a. (101, “Algoritmos”,”Algoritmos y Estructuras de
Datos”,”Mañana”,35)
b. (102, “Matemática Discreta”,””,”Tarde”,30)
3) Crea un registro con el nombre nulo y verifica que no
funciona.
4) Crea un registro con la clave primaria repetida y verifica que
no funciona.
5) Actualiza, para todos los cursos, el cupo en 25.
6) Elimina el curso “Algoritmos”.
'''


import sqlite3

conexion = sqlite3.connect("ejercicios1")
cursor = conexion.cursor()
with open('Tema_1_Manipulacion\ejerciciosSQL.sql', 'r',encoding='utf-8') as ejercicios:
  data = ejercicios.read()
  cursor.execute(data)



# cursor.execute("ALTER TABLE curso ADD column cupo INTEGER")

# cursor.execute("INSERT INTO curso VALUES(101, 'Algoritmos','Algoritmos y Estructuras de Datos','Mañana',35)")
# cursor.execute("INSERT INTO curso VALUES (102, 'Matemática Discreta','','Tarde',30)") 
# cursor.execute("INSERT INTO curso VALUES(101, 'null','Algoritmos y Estructuras de Datos','Mañana',35)")
# cursor.execute("INSERT INTO curso VALUES(101, 'Algoritmos','Algoritmos y Estructuras de Datos','Mañana',35)")
cursor.execute("UPDATE curso SET cupo = 25")
cursor.execute("DELETE FROM curso WHERE nombre = 'Algoritmos'")

conexion.commit()
conexion.close()
