-- Escriba una consulta para saber cuántos estudiantes son de la carrera Mecánica.

--SELECT COUNT(nombre) FROM profesor WHERE nombre = 'Fernando'

--Escriba una consulta para saber, de la tabla PROFESOR, el salario mínimo de los profesores nacidos en la década del 80.
--SELECT MIN(salario) FROM profesor WHERE fecha_nacimiento BETWEEN '1980-01-01' AND '1999-12-31'

--Escriba las siguientes consultas:

--Cantidad de pasajeros por país
SELECT pasajero.idpasajero, count(*) as ‘Cantidad de Pasajeros’
from PASAJERO p inner join PAIS P on pasajero.idpasajero = pais.idpais
inner join PAIS P on P.idpais =
p.idpasajero
group by p.idpasajero;


--Suma de todos los pagos realizados
--Suma de todos los pagos que realizó un pasajero. El monto debe aparecer con dos decimales.
--Promedio de los pagos que realizó un pasajero.

