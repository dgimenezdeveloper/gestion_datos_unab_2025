-- Esquema lógico de la base de datos Universidad

CREATE TABLE Departamento (
    id_departamento SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Carrera (
    id_carrera SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    duracion INTEGER NOT NULL
);

CREATE TABLE Profesor (
    id_profesor SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE,
    direccion VARCHAR(200),
    email VARCHAR(100),
    telefono VARCHAR(20),
    id_departamento INTEGER REFERENCES Departamento(id_departamento)
);

CREATE TABLE Estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE,
    direccion VARCHAR(200),
    email VARCHAR(100),
    telefono VARCHAR(20),
    id_carrera INTEGER REFERENCES Carrera(id_carrera)
);

CREATE TABLE Materia (
    id_materia SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    carga_horaria INTEGER NOT NULL,
    id_carrera INTEGER REFERENCES Carrera(id_carrera)
);

CREATE TABLE Inscripcion (
    id_inscripcion SERIAL PRIMARY KEY,
    id_estudiante INTEGER REFERENCES Estudiante(id_estudiante),
    id_materia INTEGER REFERENCES Materia(id_materia),
    fecha_inscripcion DATE NOT NULL,
    estado VARCHAR(20)
);

CREATE TABLE Calificacion (
    id_calificacion SERIAL PRIMARY KEY,
    id_estudiante INTEGER REFERENCES Estudiante(id_estudiante),
    id_materia INTEGER REFERENCES Materia(id_materia),
    nota NUMERIC(4,2),
    fecha DATE
);
