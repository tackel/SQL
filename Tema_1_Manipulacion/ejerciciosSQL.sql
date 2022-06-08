

CREATE TABLE IF NOT EXISTS curso (
    codigo INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL, 
    descripcion VARCHAR(200),
    turno VARCHAR(50)
    ) 

-- sqlite no admite alter por loq eu se hace desde el archivo .py
--ALTER TABLE curso ADD cupo INT;

--INSERT INTO curso VALUES (101, 'Algoritmos','Algoritmos y Estructuras de Datos','Mañana',35)
--INSERT INTO curso VALUES (102, "Matemática Discreta","","Tarde",30);

-- Error nombre nulo
--INSERT into curso VALUES (3, NULL, NULL,"Tarde",45);

-- Error clave primaria repetida
--INSERT into curso VALUES (102, "Quimica", "","Noche",20);


--UPDATE curso SET cupo = 25;


--DELETE FROM curso WHERE nombre = "Algoritmos"
