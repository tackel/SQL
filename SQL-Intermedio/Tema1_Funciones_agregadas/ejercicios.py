import sqlite3

conexion = sqlite3.connect("ejercicios2")
cursor = conexion.cursor()
with open('SQL-Intermedio\Tema1_Funciones_agregadas\ejercicios.SQL.sql', 'r',encoding='utf-8') as ejercicios3:
  data = ejercicios3.read()
  cursor.execute(data)
  datos = cursor.fetchall()
  print(datos)

  conexion.commit()