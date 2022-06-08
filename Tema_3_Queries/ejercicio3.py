'''
Para cada caso, escriba la consulta correspondiente:

Nombre, apellido y fecha de nacimiento de todos los empleados, ordenado por fecha de nacimiento ascendente.
Todos los profesores cuyo salario sea mayor o igual a 65000.
Todos los profesores que nacieron en la década del 80.
5 registros
Todos los profesores cuyo apellido inicie con la letra “P”
Los profesores que nacieron en la década del 80 y tienen un salario mayor a 80000
'''

import sqlite3

conexion = sqlite3.connect("ejercicios2")
cursor = conexion.cursor()
with open('Tema_3_Queries\ejercicioSQL_3.sql', 'r',encoding='utf-8') as ejercicios3:
  data = ejercicios3.read()
  cursor.execute(data)
  datos = cursor.fetchall()
  print(datos)

  conexion.commit()



