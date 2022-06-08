import sqlite3

conexion = sqlite3.connect("ejercicios2")
cursor = conexion.cursor()
with open('Tema_2_Tipos_de_join\ejerciciosSQL_2.sql', 'r',encoding='utf-8') as ejercicios2:
  data = ejercicios2.read()
  cursor.execute(data)
'''
cursor.execute("INSERT INTO profesor VALUES(null,'Fernando','Gomez','2000-02-30',35000)")
cursor.execute("INSERT INTO profesor VALUES(null,'marta','peralata','1980-03-30',35000)")

cursor.execute("INSERT INTO curso VALUES(101, 'Algoritmos','Algoritmos y Estructuras de Datos','Mañana',35,1)")
cursor.execute("INSERT INTO curso VALUES(102, 'Matematica','Null',20,'Mañana',1)")
'''
cursor.execute("SELECT profesor.apellido , curso.nombre, curso.turno FROM profesor LEFT JOIN curso ON profesor.id = curso.profesor_id")
conexion.commit()
