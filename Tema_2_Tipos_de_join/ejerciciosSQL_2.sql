
CREATE TABLE IF NOT EXISTS profesor (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL, 
    apellido VARCHAR(50),
    fecha_nacimiento VARCHAR(100),
    salario INTEGER
    ) 
/*
CREATE TABLE IF NOT EXISTS curso (
    codigo INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL, 
    descripcion VARCHAR(200),
    cupo INTEGER,
    turno VARCHAR(50),
    profesor_id INTEGER NOT NULL,
    FOREIGN KEY (profesor_id) REFERENCES profesor (id)
    ) 