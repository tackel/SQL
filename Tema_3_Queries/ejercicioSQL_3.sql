

--SELECT nombre, apellido, fecha_nacimiento
--FROM profesor ORDER BY fecha_nacimiento DESC

--SELECT * FROM profesor WHERE salario >= 65000

--SELECT * FROM profesor WHERE fecha_nacimiento BETWEEN '1980-01-01' AND '1989-12-31'

--SELECT * FROM profesor LIMIT 5

--SELECT * FROM profesor WHERE apellido LIKE 'P%'

SELECT * FROM profesor WHERE fecha_nacimiento BETWEEN 
'1980-01-01' AND '1989-12-31' AND salario > 35000

