# Justificación del diseño de la base de datos universitaria

## 1. Entidades y atributos (incluye multivaluados)
La imagen del DER representa todas las entidades requeridas por el documento: Estudiante, Materia, Carrera, Profesor, Comision, Cursada, Docente_Comision, Bloque_Horario y Aula. Los atributos multivaluados (teléfonos) se modelan correctamente como entidad aparte, y los atributos compuestos (dirección) están desglosados, lo que mejora la normalización y flexibilidad. El modelo contempla todos los atributos relevantes para la gestión académica y administrativa.

## 2. Claves visibles y técnicas
Todas las entidades incluyen identificadores técnicos (PK) y claves visibles donde corresponde (legajo para Estudiante, código para Materia). Esto cumple con los requerimientos de trazabilidad, identificación y gestión eficiente.

## 3. Comisiones
La entidad Comision está correctamente asociada a Materia, con nombre no global y el atributo "cupo" que permite gestionar la capacidad de cada comisión, aportando valor administrativo y operativo.

## 4. Cursadas de estudiantes
La entidad Cursada incluye todos los datos requeridos: estado_cursada, fecha_inscripcion, calificacion_final y fecha_aprobacion, permitiendo el seguimiento académico y la obtención de analíticos parciales por estudiante.

## 5. Carga horaria de materias
Materia incluye carga_horaria_semanal y carga_horaria_total, cumpliendo con la gestión horaria solicitada y permitiendo un control preciso de la carga académica.

## 6. Docentes y comisiones
La relación Docente_Comision permite asignar docentes a comisiones con rol académico y ahora incluye los atributos de vigencia (fecha_desde, fecha_hasta), cumpliendo completamente el requerimiento de registrar la temporalidad de las asignaciones docentes.

## 7. Teléfonos del estudiante
El atributo teléfono se modela como multivaluado, permitiendo registrar múltiples contactos por estudiante y facilitando la comunicación institucional.

## 8. Días, horarios y aulas
Bloque_Horario modela correctamente los bloques semanales, incluyendo día, hora de inicio y fin, turno y aula (con número y edificio/sede), permitiendo la gestión detallada y flexible de la cursada y el uso de espacios físicos.

## Conclusión
La imagen del DER cumple de manera completa y precisa con los 8 puntos del documento de requerimientos. El modelo es normalizado, flexible y permite la gestión académica y administrativa requerida, incluyendo detalles operativos como cupo y vigencia docente. Todas las decisiones se justifican en base al análisis del documento y la verificación visual del DER, asegurando que la base de datos resultante será robusta y funcional para el dominio universitario.
