# Modelo Entidad-Relación (ER) Preliminar - Universidad

## Entidades

- **Estudiante**
  - id_estudiante (PK)
  - legajo (clave visible)
  - nombre
  - apellido
  - dni
  - fecha_nacimiento
  - direccion
  - email
  - id_carrera (FK)

- **Telefono_Estudiante** (multivaluado)
  - id_telefono (PK)
  - id_estudiante (FK)
  - telefono

- **Materia**
  - id_materia (PK)
  - codigo (clave visible)
  - nombre
  - carga_horaria_semanal
  - carga_horaria_total
  - id_carrera (FK)

- **Carrera**
  - id_carrera (PK)
  - nombre
  - duracion

- **Comision**
  - id_comision (PK)
  - nombre_comision
  - id_materia (FK)

- **Cursada** (participación de estudiante en comisión)
  - id_cursada (PK)
  - id_estudiante (FK)
  - id_comision (FK)
  - estado_cursada (Regular/Aprobada)
  - fecha_inscripcion
  - calificacion_final (nullable)
  - fecha_aprobacion (nullable)

- **Profesor**
  - id_profesor (PK)
  - nombre
  - apellido
  - dni
  - fecha_nacimiento
  - direccion
  - email

- **Docente_Comision** (asignación de docente a comisión)
  - id_docente_comision (PK)
  - id_profesor (FK)
  - id_comision (FK)
  - rol_academico (Titular/Adjunto/JTP/Ayudante)
  - fecha_desde (nullable)
  - fecha_hasta (nullable)

- **Bloque_Horario**
  - id_bloque (PK)
  - id_comision (FK)
  - dia_semana
  - hora_inicio
  - hora_fin
  - turno (etiqueta)
  - id_aula (FK)

- **Aula**
  - id_aula (PK)
  - numero
  - edificio

## Relaciones

- Un **estudiante** puede tener varios **teléfonos**
- Un **estudiante** cursa varias **comisiones** (Cursada)
- Una **materia** puede tener varias **comisiones**
- Una **comisión** puede tener varios **bloques horarios** y varios **docentes**
- Un **docente** puede estar asignado a varias **comisiones** con distintos roles y vigencias
- Un **bloque horario** se realiza en un **aula**

## Diagrama ER (texto simplificado)

[Estudiante]---<Telefono_Estudiante>
         |
         |---<Cursada>---[Comision]---<Bloque_Horario>---[Aula]
         |                        |
         |                        |---<Docente_Comision>---[Profesor]
         |                        |
         |                        |---[Materia]---[Carrera]

> Modelo ajustado para contemplar los 8 puntos del alcance del inciso 1.
