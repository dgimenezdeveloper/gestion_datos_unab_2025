# Banco de 300 preguntas para simulador de parcial de Gestión de Datos
# Cada pregunta tiene justificación detallada para feedback formativo
# Formato: ver ejemplo en el script principal

question_bank = [
    # --- A. MER y Requisitos ---
    {
        "topic": "A. MER y Requisitos",
        "universe": "Biblioteca",
        "question": "Un libro puede ser escrito por varios autores y un autor puede escribir varios libros. ¿Qué tipo de relación es?",
        "options": ["1:1", "1:N", "N:M", "Unaria"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. 1:1 implicaría que cada libro tiene un solo autor y viceversa.",
            "1": "Incorrecto. 1:N implicaría que un libro tiene un solo autor, pero un autor puede escribir varios libros.",
            "2": "Correcto. N:M significa que varios autores pueden escribir varios libros.",
            "3": "Incorrecto. Unaria sería una relación de una entidad consigo misma."
        }
    },
    {
        "topic": "A. MER y Requisitos",
        "universe": "Red Social",
        "question": "Un usuario publica posts y otros usuarios pueden comentar esos posts. ¿Cuáles son las entidades principales?",
        "options": ["USUARIO, POST, COMENTARIO", "USUARIO, POST", "POST, COMENTARIO", "USUARIO, COMENTARIO"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Las tres entidades son necesarias para modelar la situación.",
            "1": "Incorrecto. Falta la entidad COMENTARIO.",
            "2": "Incorrecto. Falta la entidad USUARIO.",
            "3": "Incorrecto. Falta la entidad POST."
        }
    },
    {
        "topic": "A. MER y Requisitos",
        "universe": "Aerolínea",
        "question": "Un pasajero reserva un asiento en un vuelo. ¿Qué representa 'reserva' en el MER?",
        "options": ["Entidad fuerte", "Atributo", "Relación con atributos propios", "Entidad débil"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. 'Reserva' no es una entidad fuerte, sino una relación entre pasajero, asiento y vuelo.",
            "1": "Incorrecto. 'Reserva' no es un atributo, es una acción.",
            "2": "Correcto. Es una relación que puede tener atributos propios como fecha o código.",
            "3": "Incorrecto. No es una entidad débil, ya que no depende de una sola entidad para su existencia."
        }
    },
    # --- B. Cardinalidades y Tipos de Relación ---
    {
        "topic": "B. Cardinalidades y Tipos de Relación",
        "universe": "Universidad",
        "question": "Un estudiante puede inscribirse en varias materias y una materia puede tener varios estudiantes. ¿Qué tipo de relación es?",
        "options": ["1:1", "1:N", "N:M", "Unaria"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. 1:1 implicaría que cada estudiante solo puede inscribirse en una materia y viceversa.",
            "1": "Incorrecto. 1:N implicaría que un estudiante puede inscribirse en varias materias, pero cada materia solo tiene un estudiante.",
            "2": "Correcto. N:M significa que varios estudiantes pueden inscribirse en varias materias.",
            "3": "Incorrecto. Unaria sería una relación de una entidad consigo misma."
        }
    },
    {
        "topic": "B. Cardinalidades y Tipos de Relación",
        "universe": "Empresa",
        "question": "Cada empleado pertenece a un único departamento, pero un departamento tiene muchos empleados. ¿Qué cardinalidad describe esta relación?",
        "options": ["1:1", "1:N (Departamento a Empleado)", "N:M", "1:N (Empleado a Departamento)"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. 1:1 implicaría que cada empleado y cada departamento se corresponden uno a uno.",
            "1": "Correcto. Un departamento tiene muchos empleados, pero cada empleado solo pertenece a un departamento.",
            "2": "Incorrecto. N:M implicaría que un empleado puede estar en varios departamentos.",
            "3": "Incorrecto. El sentido correcto es de departamento a empleado."
        }
    },
    {
        "topic": "B. Cardinalidades y Tipos de Relación",
        "universe": "Hospital",
        "question": "Un médico puede atender a muchos pacientes, pero cada paciente es atendido por un solo médico. ¿Qué tipo de relación es?",
        "options": ["1:1", "1:N (Médico a Paciente)", "N:M", "Unaria"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. 1:1 implicaría que cada médico atiende a un solo paciente y viceversa.",
            "1": "Correcto. Un médico puede atender a muchos pacientes, pero cada paciente solo tiene un médico asignado.",
            "2": "Incorrecto. N:M implicaría que un paciente puede tener varios médicos.",
            "3": "Incorrecto. Unaria sería una relación de una entidad consigo misma."
        }
    },
    # --- C. Atributos ---
    {
        "topic": "C. Atributos",
        "universe": "Hospital",
        "question": "Si solo guardamos la fecha de nacimiento de un paciente, su 'edad' es un atributo de tipo:",
        "options": ["Compuesto", "Multivaluado", "Derivado", "Simple"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. Un atributo compuesto es aquel que puede descomponerse en partes más pequeñas, como dirección (calle, número, ciudad).",
            "1": "Incorrecto. Un atributo multivaluado es aquel que puede tener varios valores para una misma entidad, como teléfonos.",
            "2": "Correcto. Un atributo derivado es aquel cuyo valor se puede calcular a partir de otro, como la edad desde la fecha de nacimiento.",
            "3": "Incorrecto. Un atributo simple es indivisible, pero la edad aquí se deriva de la fecha de nacimiento."
        }
    },
    {
        "topic": "C. Atributos",
        "universe": "Inmobiliaria",
        "question": "La dirección de una propiedad (calle, número, ciudad) es un ejemplo de atributo:",
        "options": ["Simple", "Compuesto", "Multivaluado", "Clave"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. Un atributo simple es indivisible, pero dirección puede descomponerse.",
            "1": "Correcto. Un atributo compuesto se puede descomponer en partes más pequeñas con significado propio.",
            "2": "Incorrecto. Un atributo multivaluado es aquel que puede tener varios valores para una misma entidad.",
            "3": "Incorrecto. Clave no es un tipo de atributo, sino una función en el modelo lógico."
        }
    },
    {
        "topic": "C. Atributos",
        "universe": "Red Social",
        "question": "Un usuario puede tener múltiples 'hobbies'. En el MER, 'hobbies' se modelaría inicialmente como un atributo:",
        "options": ["Simple", "Compuesto", "Multivaluado", "Derivado"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. Un atributo simple solo puede tener un valor por entidad.",
            "1": "Incorrecto. Un atributo compuesto se descompone en partes, pero no necesariamente es multivaluado.",
            "2": "Correcto. Un atributo multivaluado puede contener múltiples valores para una misma instancia de una entidad.",
            "3": "Incorrecto. Un atributo derivado se calcula a partir de otros."
        }
    },
    # --- D. Entidades Débiles ---
    {
        "topic": "D. Entidades Débiles",
        "universe": "Gestión de Proyectos",
        "question": "En una tabla 'TAREAS', la PK es (id_proyecto, nro_tarea). Esto es una señal de que 'TAREA' podría ser una:",
        "options": ["Entidad Fuerte con clave compuesta", "Entidad Débil de 'PROYECTO'", "Relación Unaria", "Clave Alternativa"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. Una entidad fuerte con clave compuesta no depende de otra entidad para su existencia.",
            "1": "Correcto. La PK de una entidad débil se forma con la PK de su entidad fuerte y un discriminante propio.",
            "2": "Incorrecto. Relación unaria es una relación de una entidad consigo misma.",
            "3": "Incorrecto. Clave alternativa es una candidata no elegida como PK."
        }
    },
    {
        "topic": "D. Entidades Débiles",
        "universe": "Aerolínea",
        "question": "Un 'ASIENTO' no puede existir si no pertenece a un 'AVION', y su número se repite. 'ASIENTO' es un ejemplo de:",
        "options": ["Entidad Fuerte", "Relación N:M", "Entidad Débil", "Atributo Compuesto"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. Una entidad fuerte tiene existencia independiente.",
            "1": "Incorrecto. No es una relación N:M, sino una entidad dependiente.",
            "2": "Correcto. Su existencia depende de AVION y su identificador solo es único en ese contexto, definiendo una entidad débil.",
            "3": "Incorrecto. No es un atributo compuesto, sino una entidad."
        }
    },
    {
        "topic": "E. Claves",
        "universe": "E-commerce",
        "question": "¿Cuáles de los siguientes serían buenas claves candidatas naturales para un PRODUCTO?",
        "options": ["ID Autonumérico", "SKU (si es único)", "Código de Barras (EAN)", "Nombre del Producto"],
        "type": "multiple",
        "correct_answers": [1, 2],
        "justification": {
            "0": "Incorrecto. El ID autonumérico es una clave surrogada, no natural.",
            "1": "Correcto. El SKU es un identificador único de negocio.",
            "2": "Correcto. El código de barras es un identificador único de negocio.",
            "3": "Incorrecto. El nombre puede repetirse y no es único."
        }
    },
    {
        "topic": "F. DDL y Restricciones Físicas",
        "universe": "Sistema de Pedidos",
        "question": "La regla 'El precio de un producto no puede ser negativo' se implementa con la restricción:",
        "options": ["TRIGGER", "CHECK", "VIEW", "APPLICATION LOGIC"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. Un trigger puede validar, pero la forma declarativa y segura es un CHECK.",
            "1": "Correcto. CHECK (precio >= 0) es la forma estándar en SQL.",
            "2": "Incorrecto. Una vista no impone restricciones.",
            "3": "Incorrecto. La lógica de aplicación puede validar, pero no es suficiente para la integridad de datos."
        }
    },
    {
        "topic": "G. Capas de Control",
        "universe": "General",
        "question": "¿En qué capa se controla principalmente la restricción 'No se puede eliminar un cliente con pedidos'?",
        "options": ["Conceptual (MER)", "Lógico (Relacional)", "Físico (DDL/Constraints)", "Aplicación"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. El MER define la regla, pero el control efectivo es físico.",
            "1": "Incorrecto. El modelo lógico define la FK, pero la restricción se implementa en el físico.",
            "2": "Correcto. Se controla con ON DELETE RESTRICT/NO ACTION en la base de datos.",
            "3": "Incorrecto. La aplicación puede validar, pero la integridad debe estar en la base."
        }
    },
    {
        "topic": "H. UoD Comparados",
        "universe": "Veterinaria",
        "question": "Una mascota puede recibir varias vacunas en distintas fechas y una vacuna puede aplicarse a muchas mascotas. ¿Cómo se modela esto en el lógico?",
        "options": ["1:N Mascota–Vacuna", "N:M con tabla puente (fecha, dosis)", "Atributo multivaluado en Mascota", "Columna 'vacunas' VARCHAR"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. 1:N no permite registrar varias vacunas por mascota y varias mascotas por vacuna.",
            "1": "Correcto. Se requiere una tabla puente con atributos propios (fecha, dosis).",
            "2": "Incorrecto. Un atributo multivaluado no permite registrar metadatos como fecha y dosis.",
            "3": "Incorrecto. Una columna VARCHAR no es relacional ni escalable."
        }
    },
    {
        "topic": "I. Integridad Referencial",
        "universe": "Universidad",
        "question": "¿Qué sucede si intentamos eliminar una materia que tiene inscripciones activas, con una FK ON DELETE RESTRICT?",
        "options": ["Se elimina la materia y las inscripciones", "Se elimina solo la materia", "No se permite la eliminación", "Se eliminan solo las inscripciones"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. ON DELETE RESTRICT impide eliminar si hay registros relacionados.",
            "1": "Incorrecto. No se elimina la materia si hay inscripciones.",
            "2": "Correcto. La base de datos rechaza la operación para mantener la integridad.",
            "3": "Incorrecto. No se eliminan automáticamente las inscripciones."
        }
    },
    {
        "topic": "J. Normalización",
        "universe": "Restaurante",
        "question": "Si una tabla de pedidos almacena el nombre y teléfono del cliente en cada fila, ¿qué problema de normalización existe?",
        "options": ["Redundancia y actualización inconsistente", "Falta de clave primaria", "Atributo multivaluado", "Ninguno"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Se repite información y puede haber inconsistencias si el cliente cambia su teléfono.",
            "1": "Incorrecto. Puede haber clave primaria, pero el problema es la redundancia.",
            "2": "Incorrecto. No es un atributo multivaluado, sino repetido.",
            "3": "Incorrecto. Sí existe un problema de normalización."
        }
    },
    {
        "topic": "K. Casos Integradores",
        "universe": "Biblioteca",
        "question": "¿Cuál sería la clave primaria más adecuada para una tabla de préstamos de libros?",
        "options": ["ID autonumérico", "(id_libro, id_usuario, fecha_prestamo)", "id_libro solo", "id_usuario solo"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. Un ID autonumérico puede ser útil, pero la clave natural compuesta es más representativa.",
            "1": "Correcto. La combinación identifica unívocamente cada préstamo.",
            "2": "Incorrecto. id_libro solo no distingue entre préstamos a distintos usuarios.",
            "3": "Incorrecto. id_usuario solo no distingue entre distintos libros."
        }
    },
    {
        "topic": "L. Situaciones Prácticas",
        "universe": "E-commerce",
        "question": "¿Qué ventaja tiene usar una clave surrogada (ID autonumérico) en vez de una clave natural compleja?",
        "options": ["Facilita la gestión y relaciones", "Evita la redundancia", "Permite más atributos", "No tiene ventajas"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Simplifica las relaciones y la gestión de claves foráneas.",
            "1": "Incorrecto. No evita la redundancia por sí sola.",
            "2": "Incorrecto. No afecta la cantidad de atributos.",
            "3": "Incorrecto. Sí tiene ventajas en la práctica."
        }
    },
    {
        "topic": "M. Modelado Integrador",
        "universe": "Universidad",
        "question": "Un alumno puede inscribirse a materias, cada materia tiene un profesor, y los exámenes se asocian a inscripciones. ¿Cuántas tablas mínimas requiere el modelo lógico?",
        "options": ["3", "4", "5", "6"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. Faltan entidades o relaciones.",
            "1": "Incorrecto. Faltan entidades o relaciones.",
            "2": "Correcto. Alumnos, Materias, Profesores, Inscripciones, Exámenes.",
            "3": "Incorrecto. Se puede resolver con 5 tablas."
        }
    },
    {
        "topic": "N. Dependencias Funcionales",
        "universe": "Supermercado",
        "question": "Si el código de producto determina el nombre y el precio, ¿qué tipo de dependencia existe?",
        "options": ["Parcial", "Total", "Transitiva", "Multivaluada"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. Parcial sería si solo una parte de la clave determina el atributo.",
            "1": "Correcto. El código determina completamente nombre y precio.",
            "2": "Incorrecto. Transitiva sería si hay una cadena de dependencias.",
            "3": "Incorrecto. No es una dependencia multivaluada."
        }
    },
    {
        "topic": "O. Paso de ER a Relacional",
        "universe": "Hospital",
        "question": "¿Cómo se representa una relación N:M entre PACIENTE y TRATAMIENTO en el modelo relacional?",
        "options": ["Tabla puente con FKs", "Atributo multivaluado", "Columna booleana", "No se representa"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Se crea una tabla intermedia con FKs a ambas entidades.",
            "1": "Incorrecto. Un atributo multivaluado no es relacional.",
            "2": "Incorrecto. Una columna booleana no representa la relación N:M.",
            "3": "Incorrecto. Sí debe representarse."
        }
    },
    {
        "topic": "P. Restricciones de Unicidad",
        "universe": "Red Social",
        "question": "¿Cómo se asegura que el email de usuario sea único en la base de datos?",
        "options": ["PRIMARY KEY", "UNIQUE", "CHECK", "FOREIGN KEY"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. PRIMARY KEY solo puede haber una por tabla y suele ser un ID.",
            "1": "Correcto. UNIQUE garantiza que no se repita el valor en la columna.",
            "2": "Incorrecto. CHECK valida condiciones pero no unicidad.",
            "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no unicidad."
        }
    },
    {
        "topic": "Q. Casos Prácticos",
        "universe": "Inmobiliaria",
        "question": "¿Qué entidad sería débil en el caso de departamentos dentro de un edificio?",
        "options": ["EDIFICIO", "DEPARTAMENTO", "PROPIETARIO", "CIUDAD"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. El edificio existe independientemente.",
            "1": "Correcto. El departamento depende del edificio para su identificación.",
            "2": "Incorrecto. El propietario es una entidad fuerte.",
            "3": "Incorrecto. La ciudad es una entidad fuerte."
        }
    },
    {
        "topic": "R. Modelado Avanzado",
        "universe": "Empresa",
        "question": "Un empleado puede supervisar a otros empleados. ¿Cómo se modela esto en el MER?",
        "options": ["Relación unaria", "Entidad débil", "Atributo multivaluado", "Relación N:M"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Es una relación de la entidad EMPLEADO consigo misma.",
            "1": "Incorrecto. No es una entidad débil.",
            "2": "Incorrecto. No es un atributo multivaluado.",
            "3": "Incorrecto. No necesariamente es N:M, puede ser 1:N."
        }
    },
    {
        "topic": "S. Claves Alternativas",
        "universe": "Universidad",
        "question": "En la tabla ALUMNO, además del DNI, ¿qué otro atributo podría ser clave alternativa?",
        "options": ["Nombre", "Correo electrónico institucional", "Fecha de nacimiento", "Carrera"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. El nombre no es único.",
            "1": "Correcto. El correo institucional suele ser único y puede ser clave alternativa.",
            "2": "Incorrecto. La fecha de nacimiento no es única.",
            "3": "Incorrecto. La carrera no es única por alumno."
        }
    },
    {
        "topic": "T. Integridad de Dominio",
        "universe": "Hospital",
        "question": "¿Cómo se asegura que la fecha de alta de un paciente no sea anterior a la de ingreso?",
        "options": ["CHECK", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. CHECK permite validar condiciones entre columnas.",
            "1": "Incorrecto. UNIQUE solo asegura unicidad.",
            "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones.",
            "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
        }
    },
    {
        "topic": "U. Diseño Físico",
        "universe": "E-commerce",
        "question": "¿Qué aspecto es propio del diseño físico de una base de datos?",
        "options": ["Índices", "Entidades", "Relaciones", "Atributos"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Los índices son parte del diseño físico para optimizar consultas.",
            "1": "Incorrecto. Las entidades son del modelo conceptual.",
            "2": "Incorrecto. Las relaciones son del modelo conceptual/lógico.",
            "3": "Incorrecto. Los atributos son del modelo lógico."
        }
    },
    {
        "topic": "V. Optimización",
        "universe": "General",
        "question": "¿Cuál es el principal objetivo de la normalización en bases de datos?",
        "options": ["Eliminar redundancias", "Aumentar la velocidad de consulta", "Reducir el tamaño físico", "Facilitar la programación"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. La normalización busca eliminar redundancias y anomalías.",
            "1": "Incorrecto. Puede afectar la velocidad, pero no es el objetivo principal.",
            "2": "Incorrecto. El tamaño físico puede aumentar por la descomposición.",
            "3": "Incorrecto. No es el objetivo principal."
        }
    },
    {
        "topic": "W. Casos Integradores",
        "universe": "Hospital",
        "question": "Un paciente puede tener varias internaciones, cada una en una habitación distinta. ¿Cómo se modela esto en el lógico?",
        "options": ["FK en PACIENTE a HABITACION", "Tabla INTERNA con FKs a PACIENTE y HABITACION", "Atributo multivaluado en PACIENTE", "No se puede modelar"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. Un paciente puede tener varias internaciones, no una sola.",
            "1": "Correcto. Se requiere una tabla INTERNA con FKs a ambas entidades.",
            "2": "Incorrecto. Un atributo multivaluado no permite registrar metadatos de la internación.",
            "3": "Incorrecto. Sí se puede modelar correctamente."
        }
    },
    {
        "topic": "X. Vistas",
        "universe": "Universidad",
        "question": "¿Para qué se utiliza una vista en una base de datos relacional?",
        "options": ["Restringir acceso a datos", "Aumentar la velocidad de escritura", "Eliminar redundancia física", "Definir claves primarias"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Una vista puede mostrar solo ciertos datos a determinados usuarios.",
            "1": "Incorrecto. Las vistas no mejoran la velocidad de escritura.",
            "2": "Incorrecto. No eliminan redundancia física, solo presentan datos.",
            "3": "Incorrecto. Las claves primarias se definen en tablas, no en vistas."
        }
    },
    {
        "topic": "Y. Triggers",
        "universe": "E-commerce",
        "question": "¿Cuál es una función típica de un trigger en una base de datos?",
        "options": ["Actualizar automáticamente un stock", "Definir una clave foránea", "Crear una tabla", "Definir un índice"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Un trigger puede actualizar el stock tras una venta.",
            "1": "Incorrecto. Las claves foráneas se definen en el DDL, no con triggers.",
            "2": "Incorrecto. Crear tablas es DDL, no trigger.",
            "3": "Incorrecto. Los índices se definen aparte."
        }
    },
    {
        "topic": "Z. Transacciones",
        "universe": "Banco",
        "question": "¿Qué propiedad asegura que una transacción se ejecute completamente o no se ejecute nada?",
        "options": ["Atomicidad", "Consistencia", "Aislamiento", "Durabilidad"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Atomicidad implica todo o nada.",
            "1": "Incorrecto. Consistencia asegura que los datos sigan reglas de integridad.",
            "2": "Incorrecto. Aislamiento evita interferencias entre transacciones.",
            "3": "Incorrecto. Durabilidad asegura persistencia tras commit."
        }
    },
    {
        "topic": "AA. Casos de Modelado",
        "universe": "Veterinaria",
        "question": "Un animal puede tener varios dueños a lo largo de su vida, pero solo uno a la vez. ¿Cómo se modela esto?",
        "options": ["N:M con historial", "1:N con historial de fechas", "Atributo multivaluado", "No se puede modelar"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. No es N:M simultáneo, sino secuencial.",
            "1": "Correcto. Se modela con 1:N y un historial de fechas de propiedad.",
            "2": "Incorrecto. Un atributo multivaluado no permite registrar fechas.",
            "3": "Incorrecto. Sí se puede modelar correctamente."
        }
    },
    {
        "topic": "AB. Control de Acceso",
        "universe": "General",
        "question": "¿Qué mecanismo permite limitar qué usuarios pueden consultar o modificar ciertas tablas?",
        "options": ["Permisos/GRANT", "Índices", "Triggers", "Vistas materializadas"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Los permisos (GRANT/REVOKE) controlan el acceso a los objetos.",
            "1": "Incorrecto. Los índices optimizan búsquedas, no controlan acceso.",
            "2": "Incorrecto. Los triggers ejecutan acciones automáticas, no controlan acceso.",
            "3": "Incorrecto. Las vistas materializadas almacenan resultados, no controlan acceso."
        }
    },
    {
        "topic": "AC. Backup y Recuperación",
        "universe": "General",
        "question": "¿Cuál es el objetivo principal de un backup periódico de la base de datos?",
        "options": ["Recuperar datos ante fallos", "Aumentar la velocidad de consulta", "Reducir el tamaño de la base", "Evitar la normalización"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. El backup permite restaurar datos ante pérdidas o fallos.",
            "1": "Incorrecto. El backup no afecta la velocidad de consulta.",
            "2": "Incorrecto. No reduce el tamaño de la base.",
            "3": "Incorrecto. No tiene relación con la normalización."
        }
    },
    {
        "topic": "AD. Recuperación ante Fallos",
        "universe": "Banco",
        "question": "¿Qué mecanismo permite restaurar la base de datos a un estado consistente tras un corte de energía?",
        "options": ["Transacciones y logs", "Índices", "Triggers", "Vistas"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Los logs de transacciones permiten recuperar el estado consistente.",
            "1": "Incorrecto. Los índices solo optimizan búsquedas.",
            "2": "Incorrecto. Los triggers no restauran estados.",
            "3": "Incorrecto. Las vistas no almacenan datos."
        }
    },
    {
        "topic": "AE. Concurrencia",
        "universe": "E-commerce",
        "question": "¿Qué problema puede surgir si dos usuarios intentan modificar el mismo registro al mismo tiempo?",
        "options": ["Condición de carrera", "Redundancia", "Normalización", "Integridad referencial"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Puede haber inconsistencias si no se controla la concurrencia.",
            "1": "Incorrecto. La redundancia es otro tipo de problema.",
            "2": "Incorrecto. La normalización no es un problema de concurrencia.",
            "3": "Incorrecto. La integridad referencial es otro aspecto."
        }
    },
    {
        "topic": "AF. Auditoría",
        "universe": "Hospital",
        "question": "¿Qué mecanismo permite registrar quién y cuándo modificó un registro?",
        "options": ["Triggers de auditoría", "Índices", "Permisos", "Vistas"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Los triggers pueden registrar cambios en tablas de auditoría.",
            "1": "Incorrecto. Los índices no registran cambios.",
            "2": "Incorrecto. Los permisos controlan acceso, no registran cambios.",
            "3": "Incorrecto. Las vistas no registran cambios."
        }
    },
    {
        "topic": "AG. Modelado Avanzado",
        "universe": "Universidad",
        "question": "Un curso puede tener varios profesores a lo largo de los años, pero solo uno por ciclo lectivo. ¿Cómo se modela esto?",
        "options": ["N:M con historial de ciclos", "1:N con ciclo lectivo", "Atributo multivaluado", "No se puede modelar"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. No es N:M simultáneo, sino secuencial.",
            "1": "Correcto. Se modela con 1:N y ciclo lectivo como parte de la clave.",
            "2": "Incorrecto. Un atributo multivaluado no permite registrar ciclos.",
            "3": "Incorrecto. Sí se puede modelar correctamente."
        }
    },
    {
        "topic": "AH. Caso ElectroHogar",
        "universe": "ElectroHogar",
        "question": "¿Cuál es la mejor PK para la tabla PEDIDO_ITEM en ElectroHogar?",
        "options": ["ID autonumérico", "(pedido_id, producto_id)", "producto_id solo", "pedido_id solo"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. El ID autonumérico no evita duplicados de producto en un mismo pedido.",
            "1": "Correcto. La PK compuesta evita ítems duplicados en el mismo pedido.",
            "2": "Incorrecto. No distingue entre pedidos distintos.",
            "3": "Incorrecto. No distingue entre productos distintos."
        }
    },
    {
        "topic": "AI. Caso Universidad",
        "universe": "Universidad",
        "question": "¿Qué atributo sería multivaluado en una entidad ALUMNO?",
        "options": ["DNI", "Nombre", "Teléfonos", "Carrera"],
        "type": "single",
        "correct_answers": [2],
        "justification": {
            "0": "Incorrecto. El DNI es monovaluado y único.",
            "1": "Incorrecto. El nombre es monovaluado.",
            "2": "Correcto. Un alumno puede tener varios teléfonos.",
            "3": "Incorrecto. Normalmente un alumno tiene una carrera principal."
        }
    },
    {
        "topic": "AJ. Caso Veterinaria",
        "universe": "Veterinaria",
        "question": "¿Cómo se modela la aplicación de vacunas a mascotas con fecha y dosis?",
        "options": ["Atributo multivaluado en MASCOTA", "Tabla puente con atributos propios", "Columna 'vacunas' VARCHAR", "No se puede modelar"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. No permite registrar fecha y dosis.",
            "1": "Correcto. Se requiere una tabla puente con FKs y atributos propios.",
            "2": "Incorrecto. No es relacional ni escalable.",
            "3": "Incorrecto. Sí se puede modelar correctamente."
        }
    },
    {
        "topic": "AK. Caso Marketplace",
        "universe": "Marketplace",
        "question": "¿Qué relación requiere una tabla de intersección con atributos propios?",
        "options": ["Vendedor–Producto (con precio y stock)", "Producto–Categoría", "Cliente–Pedido", "Producto–Marca"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. La relación Vendedor–Producto requiere atributos como precio y stock.",
            "1": "Incorrecto. Producto–Categoría suele ser 1:N.",
            "2": "Incorrecto. Cliente–Pedido es 1:N.",
            "3": "Incorrecto. Producto–Marca suele ser 1:N."
        }
    },
    {
        "topic": "AL. Interpretación de DDL",
        "universe": "General",
        "question": "¿Qué significa CHECK (cantidad > 0) en una tabla PEDIDO_ITEM?",
        "options": ["No se permiten cantidades negativas ni cero", "La cantidad puede ser cero", "Solo se permite un ítem por pedido", "No tiene efecto"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. La restricción impide valores menores o iguales a cero.",
            "1": "Incorrecto. No se permite cantidad cero.",
            "2": "Incorrecto. No limita la cantidad de ítems, solo el valor de cada uno.",
            "3": "Incorrecto. Sí tiene efecto en la validación."
        }
    },
    {
        "topic": "AM. Errores Frecuentes",
        "universe": "General",
        "question": "¿Cuál es un error común al modelar relaciones N:M?",
        "options": ["No crear tabla puente", "Usar PK compuesta", "Definir FKs en ambos lados", "Agregar atributos a la relación"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Olvidar la tabla puente impide modelar correctamente la N:M.",
            "1": "Incorrecto. Usar PK compuesta es lo correcto.",
            "2": "Incorrecto. Las FKs deben estar en la tabla puente.",
            "3": "Incorrecto. Es correcto agregar atributos si la relación los requiere."
        }
    },
    {
        "topic": "AN. Mini-ejercicio aplicado",
        "universe": "ElectroHogar",
        "question": "¿Qué entidades y relaciones principales surgen de la HU: 'Como cliente, quiero registrar mis pedidos para recibir productos'?",
        "options": ["CLIENTE, PEDIDO, PRODUCTO, PEDIDO_ITEM", "CLIENTE, PRODUCTO", "PEDIDO, PRODUCTO", "CLIENTE, PEDIDO"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. CLIENTE realiza PEDIDO, PEDIDO contiene PRODUCTO vía PEDIDO_ITEM.",
            "1": "Incorrecto. Faltan entidades y relaciones.",
            "2": "Incorrecto. Faltan CLIENTE y PEDIDO_ITEM.",
            "3": "Incorrecto. Faltan PRODUCTO y PEDIDO_ITEM."
        }
    },
    {
        "topic": "AO. Decisiones de Modelado",
        "universe": "ElectroHogar",
        "question": "¿Por qué conviene modelar TELEFONO como entidad débil y no como atributo multivaluado en CLIENTE?",
        "options": ["Permite guardar tipo y preferido", "Reduce la cantidad de tablas", "Evita la normalización", "No hay diferencia"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Así se pueden guardar metadatos como tipo y preferido.",
            "1": "Incorrecto. Agrega una tabla, pero es necesario por los metadatos.",
            "2": "Incorrecto. No evita la normalización, la mejora.",
            "3": "Incorrecto. Sí hay diferencia en la capacidad de modelado."
        }
    },
    {
        "topic": "AP. Interpretación de Restricciones",
        "universe": "Universidad",
        "question": "¿Qué implica NOT NULL en la columna 'nombre' de la tabla MATERIA?",
        "options": ["El nombre es obligatorio", "El nombre debe ser único", "El nombre puede ser nulo", "No tiene efecto"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. NOT NULL obliga a que siempre se ingrese un nombre.",
            "1": "Incorrecto. Para unicidad se requiere UNIQUE.",
            "2": "Incorrecto. NOT NULL impide valores nulos.",
            "3": "Incorrecto. Sí tiene efecto en la obligatoriedad."
        }
    },
    {
        "topic": "AQ. Error Frecuente",
        "universe": "General",
        "question": "¿Qué error ocurre si se elige el email como PK en vez de un ID surrogado?",
        "options": ["Exponer datos sensibles y problemas si cambia", "Mejor rendimiento", "Mayor normalización", "No hay error"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. El email puede cambiar y es sensible; mejor usar un ID surrogado.",
            "1": "Incorrecto. No mejora el rendimiento.",
            "2": "Incorrecto. No afecta la normalización.",
            "3": "Incorrecto. Sí hay un error de diseño."
        }
    },
    {
        "topic": "AR. Mini-ejercicio aplicado",
        "universe": "Veterinaria",
        "question": "¿Qué PK elegirías para la tabla APLICACION_VACUNA (mascota, vacuna, fecha)?",
        "options": ["ID autonumérico", "(mascota_id, vacuna_id, fecha)", "vacuna_id solo", "mascota_id solo"],
        "type": "single",
        "correct_answers": [1],
        "justification": {
            "0": "Incorrecto. El ID autonumérico no evita duplicados de aplicación en la misma fecha.",
            "1": "Correcto. La PK compuesta asegura unicidad por mascota, vacuna y fecha.",
            "2": "Incorrecto. No distingue entre mascotas ni fechas.",
            "3": "Incorrecto. No distingue entre vacunas ni fechas."
        }
    },
    {
        "topic": "AS. Mini-ejercicio aplicado",
        "universe": "Marketplace",
        "question": "¿Qué atributos debe tener la tabla PUBLICACION (vendedor, producto) para cumplir con el patrón del cuadernillo?",
        "options": ["precio, stock, estado, fecha_publicacion", "solo precio", "solo stock", "ninguno, solo FKs"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. El patrón requiere esos atributos en la tabla de intersección.",
            "1": "Incorrecto. Faltan atributos clave.",
            "2": "Incorrecto. Faltan atributos clave.",
            "3": "Incorrecto. Faltan todos los atributos requeridos."
        }
    },
    {
        "topic": "AT. Interpretación de DDL",
        "universe": "ElectroHogar",
        "question": "¿Qué implica la restricción UNIQUE en el nombre de la tabla CATEGORIA?",
        "options": ["No puede haber dos categorías con el mismo nombre", "El nombre puede repetirse", "El nombre puede ser nulo", "No tiene efecto"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. UNIQUE obliga a que el nombre sea único en la tabla.",
            "1": "Incorrecto. UNIQUE impide repeticiones.",
            "2": "Incorrecto. La nulidad depende de NOT NULL, no de UNIQUE.",
            "3": "Incorrecto. Sí tiene efecto en la unicidad."
        }
    },
    {
        "topic": "AU. Error de Modelado",
        "universe": "Universidad",
        "question": "¿Qué error ocurre si no se define una FK entre INSCRIPCION y MATERIA?",
        "options": ["Se pueden inscribir materias inexistentes", "Mejor rendimiento", "Mayor normalización", "No hay error"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Sin FK, se pueden inscribir materias que no existen en la tabla MATERIA.",
            "1": "Incorrecto. No mejora el rendimiento.",
            "2": "Incorrecto. No afecta la normalización.",
            "3": "Incorrecto. Sí hay un error de integridad."
        }
    },
    {
        "topic": "AV. Mini-ejercicio aplicado",
        "universe": "ElectroHogar",
        "question": "¿Qué relación y cardinalidad existe entre CLIENTE y PEDIDO?",
        "options": ["1:N (un cliente, muchos pedidos)", "N:M", "1:1", "N:1 (muchos clientes, un pedido)"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Un cliente puede tener muchos pedidos, cada pedido pertenece a un cliente.",
            "1": "Incorrecto. No es N:M, cada pedido tiene un solo cliente.",
            "2": "Incorrecto. No es 1:1.",
            "3": "Incorrecto. No es N:1, el sentido es 1:N."
        }
    },
    {
        "topic": "AW. Patrón Práctico",
        "universe": "Veterinaria",
        "question": "¿Por qué la tabla APLICACION_VACUNA debe tener fecha como parte de la PK?",
        "options": ["Permite registrar varias aplicaciones de la misma vacuna a la misma mascota", "Evita la redundancia", "Mejora el rendimiento", "No es necesario"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. Así se pueden registrar varias aplicaciones en fechas distintas.",
            "1": "Incorrecto. No evita redundancia por sí sola.",
            "2": "Incorrecto. No mejora el rendimiento.",
            "3": "Incorrecto. Sí es necesario para la unicidad."
        }
    },
    {
        "topic": "AX. Mini-ejercicio aplicado",
        "universe": "Marketplace",
        "question": "¿Qué PK compuesta es adecuada para la tabla PUBLICACION?",
        "options": ["(vendedor_id, producto_id)", "producto_id solo", "vendedor_id solo", "ID autonumérico"],
        "type": "single",
        "correct_answers": [0],
        "justification": {
            "0": "Correcto. La PK compuesta asegura unicidad por vendedor y producto.",
            "1": "Incorrecto. No distingue entre vendedores.",
            "2": "Incorrecto. No distingue entre productos.",
            "3": "Incorrecto. El ID autonumérico no evita duplicados de publicación."
        }
    },
    # ... continuar hasta completar 300 preguntas ...
        # --- AY. Caso ElectroHogar: DDL y Restricciones ---
        {
            "topic": "AY. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción física asegura que no se puedan cargar dos productos con el mismo código en la tabla PRODUCTO?",
            "options": ["PRIMARY KEY", "UNIQUE", "CHECK", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [1],
            "justification": {
                "0": "Incorrecto. PRIMARY KEY suele usarse para el ID, pero el código puede no ser la PK principal.",
                "1": "Correcto. UNIQUE asegura que el código no se repita aunque no sea PK.",
                "2": "Incorrecto. CHECK valida condiciones, pero no unicidad.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no unicidad."
            }
        },
        # --- AZ. Caso Universidad: Mini-ejercicio de Inscripción ---
        {
            "topic": "AZ. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué tablas mínimas se requieren para modelar inscripciones de alumnos a materias con registro de fecha?",
            "options": ["ALUMNO, MATERIA, INSCRIPCION", "ALUMNO, INSCRIPCION", "MATERIA, INSCRIPCION", "ALUMNO, MATERIA"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se necesita una tabla puente (INSCRIPCION) con FKs y fecha.",
                "1": "Incorrecto. Falta la tabla MATERIA.",
                "2": "Incorrecto. Falta la tabla ALUMNO.",
                "3": "Incorrecto. Faltaría la relación y la fecha."
            }
        },
        # --- BA. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "BA. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si se modela la relación mascota-vacuna solo como atributo multivaluado?",
            "options": ["No se pueden registrar fechas ni dosis", "Se mejora la normalización", "Se optimiza el rendimiento", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. El atributo multivaluado no permite guardar metadatos como fecha y dosis.",
                "1": "Incorrecto. Se pierde normalización y flexibilidad.",
                "2": "Incorrecto. No se optimiza el rendimiento, se limita el modelo.",
                "3": "Incorrecto. Sí hay un error de modelado."
            }
        },
        # --- BB. Caso Marketplace: Interpretación de DDL ---
        {
            "topic": "BB. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué implica la restricción FOREIGN KEY (producto_id) REFERENCES PRODUCTO(id) ON DELETE CASCADE en la tabla PUBLICACION?",
            "options": ["Se eliminan publicaciones al borrar el producto", "No se pueden borrar productos", "No tiene efecto", "Solo se eliminan productos sin publicaciones"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. ON DELETE CASCADE elimina las publicaciones asociadas al borrar el producto.",
                "1": "Incorrecto. Sí se pueden borrar productos, pero se eliminan en cascada las publicaciones.",
                "2": "Incorrecto. Sí tiene efecto en la integridad referencial.",
                "3": "Incorrecto. No es condición para eliminar productos."
            }
        },
        # --- BC. Mini-ejercicio aplicado: ElectroHogar ---
        {
            "topic": "BC. Mini-ejercicio aplicado",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla PEDIDO_ITEM según el patrón del cuadernillo?",
            "options": ["cantidad, precio_unitario", "solo cantidad", "solo precio_unitario", "ninguno, solo FKs"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar cantidad y precio_unitario por ítem.",
                "1": "Incorrecto. Falta el precio_unitario.",
                "2": "Incorrecto. Falta la cantidad.",
                "3": "Incorrecto. Faltan ambos atributos requeridos."
            }
        },
        # --- BD. Error Frecuente: Universidad ---
        {
            "topic": "BD. Error Frecuente",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si se permite que la columna 'fecha_inscripcion' sea NULL en la tabla INSCRIPCION?",
            "options": ["Se pierden datos clave", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. La fecha es clave para el registro y control de inscripciones.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de perder datos clave.",
                "2": "Incorrecto. Sí afecta la integridad y trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- BE. Mini-ejercicio aplicado: Marketplace ---
        {
            "topic": "BE. Mini-ejercicio aplicado",
            "universe": "Marketplace",
            "question": "¿Qué relación y cardinalidad existe entre VENDEDOR y PUBLICACION?",
            "options": ["1:N (un vendedor, muchas publicaciones)", "N:M", "1:1", "N:1 (muchos vendedores, una publicación)"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Un vendedor puede tener muchas publicaciones, cada publicación pertenece a un vendedor.",
                "1": "Incorrecto. No es N:M, cada publicación tiene un solo vendedor.",
                "2": "Incorrecto. No es 1:1.",
                "3": "Incorrecto. No es N:1, el sentido es 1:N."
            }
        },
        # --- BF. Caso Veterinaria: Mini-ejercicio de PK ---
        {
            "topic": "BF. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Cuál es la PK más adecuada para la tabla HISTORIAL_PROPIEDAD (mascota_id, fecha_inicio, fecha_fin)?",
            "options": ["(mascota_id, fecha_inicio)", "mascota_id solo", "fecha_inicio solo", "ID autonumérico"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. La combinación asegura unicidad por periodo de propiedad.",
                "1": "Incorrecto. No distingue entre distintos periodos.",
                "2": "Incorrecto. No distingue entre mascotas ni periodos.",
                "3": "Incorrecto. El ID autonumérico no evita duplicados de periodo."
            }
        },
        # --- BG. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "BG. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si no se define una FK entre PEDIDO_ITEM y PRODUCTO?",
            "options": ["Se pueden cargar ítems de productos inexistentes", "Mejora el rendimiento", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin FK, se pueden cargar ítems de productos que no existen en la tabla PRODUCTO.",
                "1": "Incorrecto. No mejora el rendimiento.",
                "2": "Incorrecto. Sí afecta la integridad referencial.",
                "3": "Incorrecto. Sí hay un error de integridad."
            }
        },
        # --- BH. Mini-ejercicio aplicado: Universidad ---
        {
            "topic": "BH. Mini-ejercicio aplicado",
            "universe": "Universidad",
            "question": "¿Qué atributos propios debe tener la tabla INSCRIPCION según el patrón del cuadernillo?",
            "options": ["fecha_inscripcion, estado", "solo fecha_inscripcion", "solo estado", "ninguno, solo FKs"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar fecha y estado de la inscripción.",
                "1": "Incorrecto. Falta el estado.",
                "2": "Incorrecto. Falta la fecha.",
                "3": "Incorrecto. Faltan ambos atributos requeridos."
            }
        },
        # --- BI. Caso Marketplace: Error de Modelado ---
        {
            "topic": "BI. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si se permite que el stock sea negativo en la tabla PUBLICACION?",
            "options": ["Se pueden vender productos inexistentes", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Permitir stock negativo puede llevar a ventas imposibles.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        }
        ,
        # --- BJ. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "BJ. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción SQL asegura que el precio_unitario de PEDIDO_ITEM sea mayor a cero?",
            "options": ["CHECK (precio_unitario > 0)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones sobre los valores de la columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores mayores a cero.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones de valor.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- BK. Caso Universidad: Error de Modelado ---
        {
            "topic": "BK. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla INSCRIPCION no tiene PK compuesta por alumno, materia y fecha?",
            "options": ["Se pueden duplicar inscripciones", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK compuesta, se pueden registrar inscripciones duplicadas para el mismo alumno, materia y fecha.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- BL. Caso Veterinaria: Mini-ejercicio de Relación ---
        {
            "topic": "BL. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué relación y cardinalidad existe entre MASCOTA y HISTORIAL_PROPIEDAD?",
            "options": ["1:N (una mascota, muchos historiales)", "N:M", "1:1", "N:1 (muchas mascotas, un historial)"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Una mascota puede tener muchos historiales de propiedad, cada historial pertenece a una mascota.",
                "1": "Incorrecto. No es N:M, cada historial es de una sola mascota.",
                "2": "Incorrecto. No es 1:1.",
                "3": "Incorrecto. No es N:1, el sentido es 1:N."
            }
        },
        # --- BM. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "BM. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'estado' de PUBLICACION solo acepte los valores 'activa' o 'pausada'?",
            "options": ["CHECK (estado IN ('activa','pausada'))", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite limitar los valores posibles de una columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores permitidos.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no valores permitidos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- BN. Caso ElectroHogar: Error de Modelado ---
        {
            "topic": "BN. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla PEDIDO_ITEM no tiene FK a PEDIDO?",
            "options": ["Se pueden cargar ítems sin pedido asociado", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin FK, se pueden cargar ítems que no pertenecen a ningún pedido existente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad referencial.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- BO. Caso Universidad: Mini-ejercicio de Restricción ---
        {
            "topic": "BO. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué restricción asegura que el estado de la inscripción solo pueda ser 'activa' o 'baja'?",
            "options": ["CHECK (estado IN ('activa','baja'))", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite limitar los valores posibles de una columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores permitidos.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no valores permitidos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        }
        ,
        # --- BW. Caso Marketplace: Mini-ejercicio de PK compuesta ---
        {
            "topic": "BW. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Cuál es la PK compuesta más adecuada para la tabla CARRITO_ITEM (carrito_id, producto_id)?",
            "options": ["(carrito_id, producto_id)", "carrito_id solo", "producto_id solo", "ID autonumérico"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. La combinación asegura unicidad por carrito y producto.",
                "1": "Incorrecto. No distingue entre productos en el mismo carrito.",
                "2": "Incorrecto. No distingue entre carritos ni productos.",
                "3": "Incorrecto. El ID autonumérico no evita duplicados de producto en el mismo carrito."
            }
        },
        # --- BX. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "BX. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'email' de CLIENTE sea único?",
            "options": ["UNIQUE", "CHECK", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. UNIQUE garantiza que no se repita el email en la tabla.",
                "1": "Incorrecto. CHECK valida condiciones, pero no unicidad.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, pero puede haber otros campos únicos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no unicidad."
            }
        },
        # --- BY. Caso Universidad: Error de DDL ---
        {
            "topic": "BY. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla INSCRIPCION no tiene FK a ALUMNO?",
            "options": ["Se pueden registrar inscripciones de alumnos inexistentes", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin FK, se pueden registrar inscripciones de alumnos que no existen en la tabla ALUMNO.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad referencial.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- BZ. Caso Veterinaria: Mini-ejercicio de Atributos ---
        {
            "topic": "BZ. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué atributos propios debe tener la tabla VACUNA según el patrón del cuadernillo?",
            "options": ["nombre, laboratorio, tipo", "solo nombre", "solo laboratorio", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, laboratorio y tipo.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        },
        # --- CA. Caso Marketplace: Error de Modelado ---
        {
            "topic": "CA. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla PUBLICACION no tiene PK compuesta por vendedor y producto?",
            "options": ["Se pueden publicar el mismo producto varias veces por el mismo vendedor", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK compuesta, se pueden duplicar publicaciones del mismo producto por el mismo vendedor.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CB. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "CB. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla PRODUCTO según el patrón del cuadernillo?",
            "options": ["nombre, descripcion, precio, stock", "solo nombre", "solo precio", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, descripción, precio y stock.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- CC. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "CC. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'precio' de PRODUCTO sea mayor o igual a 0?",
            "options": ["CHECK (precio >= 0)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones sobre los valores de la columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores mayores o iguales a cero.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones de valor.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- CD. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "CD. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla PEDIDO no tiene FK a CLIENTE?",
            "options": ["Se pueden registrar pedidos de clientes inexistentes", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin FK, se pueden registrar pedidos de clientes que no existen en la tabla CLIENTE.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad referencial.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CE. Caso Universidad: Mini-ejercicio de PK compuesta ---
        {
            "topic": "CE. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Cuál es la PK compuesta más adecuada para la tabla INSCRIPCION (alumno_id, materia_id, fecha_inscripcion)?",
            "options": ["(alumno_id, materia_id, fecha_inscripcion)", "alumno_id solo", "materia_id solo", "ID autonumérico"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. La combinación asegura unicidad por alumno, materia y fecha.",
                "1": "Incorrecto. No distingue entre distintas materias ni fechas.",
                "2": "Incorrecto. No distingue entre alumnos ni fechas.",
                "3": "Incorrecto. El ID autonumérico no evita duplicados de inscripción."
            }
        },
        # --- CF. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "CF. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si la tabla HISTORIAL_PROPIEDAD no tiene PK compuesta por mascota y fecha_inicio?",
            "options": ["Se pueden registrar historiales duplicados para la misma mascota y fecha", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK compuesta, se pueden duplicar historiales para la misma mascota y fecha de inicio.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CG. Caso Marketplace: Mini-ejercicio de Atributos ---
        {
            "topic": "CG. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué atributos propios debe tener la tabla VENDEDOR según el patrón del cuadernillo?",
            "options": ["nombre, email, reputacion", "solo nombre", "solo email", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, email y reputación.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- CH. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "CH. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'telefono' de CLIENTE solo acepte números de 10 dígitos?",
            "options": ["CHECK (LENGTH(telefono) = 10)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar la longitud del campo.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no longitud.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no longitud.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no formato."
            }
        },
        # --- CI. Caso Universidad: Error de DDL ---
        {
            "topic": "CI. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla MATERIA no tiene restricción UNIQUE en el campo 'codigo'?",
            "options": ["Se pueden registrar materias con el mismo código", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin UNIQUE, se pueden registrar materias con el mismo código, perdiendo unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CJ. Caso Veterinaria: Mini-ejercicio de Restricción ---
        {
            "topic": "CJ. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué restricción asegura que el campo 'fecha_aplicacion' de APLICACION_VACUNA no sea futura?",
            "options": ["CHECK (fecha_aplicacion <= CURRENT_DATE)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar que la fecha no sea posterior a la actual.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no rango de fechas.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no rango de fechas.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no rango de fechas."
            }
        },
        # --- CK. Caso Marketplace: Error de Modelado ---
        {
            "topic": "CK. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla VENDEDOR no tiene PK?",
            "options": ["Se pueden registrar vendedores duplicados", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK, se pueden registrar vendedores duplicados y no se garantiza unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CL. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "CL. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla CLIENTE según el patrón del cuadernillo?",
            "options": ["nombre, email, telefono", "solo nombre", "solo email", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, email y teléfono.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- CM. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "CM. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'reputacion' de VENDEDOR sea un valor entre 0 y 5?",
            "options": ["CHECK (reputacion >= 0 AND reputacion <= 5)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar el rango de valores permitidos.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no rango de valores.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no rango de valores.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no rango de valores."
            }
        },
        # --- CN. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "CN. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla PRODUCTO no tiene restricción CHECK en el campo 'stock' para evitar valores negativos?",
            "options": ["Se pueden registrar productos con stock negativo", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin CHECK, se pueden registrar productos con stock negativo, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CO. Caso Universidad: Mini-ejercicio de Restricción ---
        {
            "topic": "CO. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué restricción asegura que el campo 'creditos' de MATERIA sea mayor a 0?",
            "options": ["CHECK (creditos > 0)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones sobre los valores de la columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores mayores a cero.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones de valor.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- CP. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "CP. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si la tabla VACUNA no tiene PK?",
            "options": ["Se pueden registrar vacunas duplicadas", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK, se pueden registrar vacunas duplicadas y no se garantiza unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CQ. Caso Marketplace: Mini-ejercicio de Atributos ---
        {
            "topic": "CQ. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué atributos propios debe tener la tabla CLIENTE según el patrón del cuadernillo?",
            "options": ["nombre, email, direccion", "solo nombre", "solo email", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, email y dirección.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- CR. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "CR. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'nombre' de PRODUCTO no sea nulo ni vacío?",
            "options": ["NOT NULL y CHECK (nombre <> '')", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. NOT NULL impide nulos y CHECK impide cadenas vacías.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no obligatoriedad ni contenido.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para el nombre.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no obligatoriedad."
            }
        },
        # --- CS. Caso Universidad: Error de DDL ---
        {
            "topic": "CS. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla ALUMNO no tiene restricción NOT NULL en el campo 'nombre'?",
            "options": ["Se pueden registrar alumnos sin nombre", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin NOT NULL, se pueden registrar alumnos sin nombre, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CT. Caso Veterinaria: Mini-ejercicio de Restricción ---
        {
            "topic": "CT. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué restricción asegura que el campo 'tipo' de VACUNA solo acepte los valores 'viral' o 'bacteriana'?",
            "options": ["CHECK (tipo IN ('viral','bacteriana'))", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite limitar los valores posibles de una columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores permitidos.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no valores permitidos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- CU. Caso Marketplace: Error de Modelado ---
        {
            "topic": "CU. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla CLIENTE no tiene PK?",
            "options": ["Se pueden registrar clientes duplicados", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK, se pueden registrar clientes duplicados y no se garantiza unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CV. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "CV. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla PEDIDO según el patrón del cuadernillo?",
            "options": ["fecha_pedido, total, estado", "solo fecha_pedido", "solo total", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar fecha, total y estado del pedido.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- CW. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "CW. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'email' de CLIENTE tenga formato válido?",
            "options": ["CHECK (email LIKE '%_@_%._%')", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar el patrón del email.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no formato.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para el email.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no formato."
            }
        },
        # --- CX. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "CX. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla PEDIDO_ITEM no tiene restricción CHECK en el campo 'cantidad' para evitar valores menores a 1?",
            "options": ["Se pueden registrar ítems con cantidad cero o negativa", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin CHECK, se pueden registrar ítems con cantidad cero o negativa, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- CY. Caso Universidad: Mini-ejercicio de Restricción ---
        {
            "topic": "CY. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué restricción asegura que el campo 'estado' de INSCRIPCION solo acepte los valores 'activa', 'baja' o 'aprobada'?",
            "options": ["CHECK (estado IN ('activa','baja','aprobada'))", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite limitar los valores posibles de una columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores permitidos.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no valores permitidos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- CZ. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "CZ. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si la tabla HISTORIAL_PROPIEDAD no tiene FK a MASCOTA?",
            "options": ["Se pueden registrar historiales de mascotas inexistentes", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin FK, se pueden registrar historiales de mascotas que no existen en la tabla MASCOTA.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad referencial.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DA. Caso Marketplace: Mini-ejercicio de Atributos ---
        {
            "topic": "DA. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué atributos propios debe tener la tabla PEDIDO según el patrón del cuadernillo?",
            "options": ["fecha_pedido, total, estado", "solo fecha_pedido", "solo total", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar fecha, total y estado del pedido.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- DB. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "DB. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'total' de PEDIDO sea mayor a 0?",
            "options": ["CHECK (total > 0)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones sobre los valores de la columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores mayores a cero.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones de valor.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- DC. Caso Universidad: Error de DDL ---
        {
            "topic": "DC. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla INSCRIPCION no tiene restricción CHECK en el campo 'fecha_inscripcion' para evitar fechas futuras?",
            "options": ["Se pueden registrar inscripciones con fecha futura", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin CHECK, se pueden registrar inscripciones con fecha futura, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DD. Caso Veterinaria: Mini-ejercicio de Restricción ---
        {
            "topic": "DD. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué restricción asegura que el campo 'laboratorio' de VACUNA no sea nulo ni vacío?",
            "options": ["NOT NULL y CHECK (laboratorio <> '')", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. NOT NULL impide nulos y CHECK impide cadenas vacías.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no obligatoriedad ni contenido.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para el laboratorio.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no obligatoriedad."
            }
        },
        # --- DE. Caso Marketplace: Error de Modelado ---
        {
            "topic": "DE. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla PEDIDO no tiene PK?",
            "options": ["Se pueden registrar pedidos duplicados", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK, se pueden registrar pedidos duplicados y no se garantiza unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DF. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "DF. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla CATEGORIA según el patrón del cuadernillo?",
            "options": ["nombre, descripcion", "solo nombre", "solo descripcion", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre y descripción.",
                "1": "Incorrecto. Falta la descripción.",
                "2": "Incorrecto. Falta el nombre.",
                "3": "Incorrecto. Faltan ambos atributos requeridos."
            }
        }
        ,
        # --- DG. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "DG. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'stock' de PRODUCTO sea mayor o igual a 0?",
            "options": ["CHECK (stock >= 0)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones sobre los valores de la columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores mayores o iguales a cero.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones de valor.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- DH. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "DH. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla CATEGORIA no tiene restricción UNIQUE en el campo 'nombre'?",
            "options": ["Se pueden registrar categorías con el mismo nombre", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin UNIQUE, se pueden registrar categorías con el mismo nombre, perdiendo unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DI. Caso Universidad: Mini-ejercicio de Restricción ---
        {
            "topic": "DI. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué restricción asegura que el campo 'email' de ALUMNO sea único?",
            "options": ["UNIQUE", "CHECK", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. UNIQUE garantiza que no se repita el email en la tabla.",
                "1": "Incorrecto. CHECK valida condiciones, pero no unicidad.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, pero puede haber otros campos únicos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no unicidad."
            }
        },
        # --- DJ. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "DJ. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si la tabla VACUNA no tiene restricción UNIQUE en el campo 'nombre'?",
            "options": ["Se pueden registrar vacunas con el mismo nombre", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin UNIQUE, se pueden registrar vacunas con el mismo nombre, perdiendo unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DK. Caso Marketplace: Mini-ejercicio de Atributos ---
        {
            "topic": "DK. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué atributos propios debe tener la tabla CATEGORIA según el patrón del cuadernillo?",
            "options": ["nombre, descripcion", "solo nombre", "solo descripcion", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre y descripción.",
                "1": "Incorrecto. Falta la descripción.",
                "2": "Incorrecto. Falta el nombre.",
                "3": "Incorrecto. Faltan ambos atributos requeridos."
            }
        }
        ,
        # --- DL. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "DL. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'descripcion' de PRODUCTO tenga al menos 10 caracteres?",
            "options": ["CHECK (LENGTH(descripcion) >= 10)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar la longitud mínima de la descripción.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no longitud.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para la descripción.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no longitud."
            }
        },
        # --- DM. Caso Universidad: Error de DDL ---
        {
            "topic": "DM. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla MATERIA no tiene restricción CHECK en el campo 'creditos' para evitar valores negativos?",
            "options": ["Se pueden registrar materias con créditos negativos", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin CHECK, se pueden registrar materias con créditos negativos, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DN. Caso Veterinaria: Mini-ejercicio de Restricción ---
        {
            "topic": "DN. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué restricción asegura que el campo 'tipo' de VACUNA no sea nulo ni vacío?",
            "options": ["NOT NULL y CHECK (tipo <> '')", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. NOT NULL impide nulos y CHECK impide cadenas vacías.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no obligatoriedad ni contenido.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para el tipo.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no obligatoriedad."
            }
        },
        # --- DO. Caso Marketplace: Error de Modelado ---
        {
            "topic": "DO. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla CATEGORIA no tiene PK?",
            "options": ["Se pueden registrar categorías duplicadas", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK, se pueden registrar categorías duplicadas y no se garantiza unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la trazabilidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DP. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "DP. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla CLIENTE según el patrón del cuadernillo?",
            "options": ["nombre, email, telefono", "solo nombre", "solo email", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, email y teléfono.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- DQ. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "DQ. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'direccion' de CLIENTE no sea nulo ni vacío?",
            "options": ["NOT NULL y CHECK (direccion <> '')", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. NOT NULL impide nulos y CHECK impide cadenas vacías.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no obligatoriedad ni contenido.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para la dirección.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no obligatoriedad."
            }
        },
        # --- DR. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "DR. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla CLIENTE no tiene restricción UNIQUE en el campo 'email'?",
            "options": ["Se pueden registrar clientes con el mismo email", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin UNIQUE, se pueden registrar clientes con el mismo email, perdiendo unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DS. Caso Universidad: Mini-ejercicio de Restricción ---
        {
            "topic": "DS. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué restricción asegura que el campo 'nombre' de MATERIA no sea nulo ni vacío?",
            "options": ["NOT NULL y CHECK (nombre <> '')", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. NOT NULL impide nulos y CHECK impide cadenas vacías.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no obligatoriedad ni contenido.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para el nombre.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no obligatoriedad."
            }
        },
        # --- DT. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "DT. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si la tabla HISTORIAL_PROPIEDAD no tiene restricción CHECK en el campo 'fecha_inicio' para evitar fechas futuras?",
            "options": ["Se pueden registrar historiales con fecha futura", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin CHECK, se pueden registrar historiales con fecha futura, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DU. Caso Marketplace: Mini-ejercicio de Atributos ---
        {
            "topic": "DU. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué atributos propios debe tener la tabla PEDIDO_ITEM según el patrón del cuadernillo?",
            "options": ["cantidad, precio_unitario", "solo cantidad", "solo precio_unitario", "ninguno, solo FKs"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar cantidad y precio_unitario por ítem.",
                "1": "Incorrecto. Falta el precio_unitario.",
                "2": "Incorrecto. Falta la cantidad.",
                "3": "Incorrecto. Faltan ambos atributos requeridos."
            }
        }
        ,
        # --- DV. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "DV. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'estado' de PEDIDO solo acepte los valores 'pendiente', 'enviado' o 'cancelado'?",
            "options": ["CHECK (estado IN ('pendiente','enviado','cancelado'))", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite limitar los valores posibles de una columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores permitidos.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no valores permitidos.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- DW. Caso Universidad: Error de DDL ---
        {
            "topic": "DW. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla ALUMNO no tiene restricción UNIQUE en el campo 'email'?",
            "options": ["Se pueden registrar alumnos con el mismo email", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin UNIQUE, se pueden registrar alumnos con el mismo email, perdiendo unicidad.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DX. Caso Veterinaria: Mini-ejercicio de Restricción ---
        {
            "topic": "DX. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué restricción asegura que el campo 'fecha_fin' de HISTORIAL_PROPIEDAD no sea anterior a 'fecha_inicio'?",
            "options": ["CHECK (fecha_fin >= fecha_inicio)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones entre columnas.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no relaciones entre fechas.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no relaciones entre fechas.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no relaciones entre fechas."
            }
        },
        # --- DY. Caso Marketplace: Error de Modelado ---
        {
            "topic": "DY. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla PEDIDO_ITEM no tiene PK compuesta por pedido y producto?",
            "options": ["Se pueden registrar ítems duplicados para el mismo pedido y producto", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin PK compuesta, se pueden duplicar ítems para el mismo pedido y producto.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la unicidad.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- DZ. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "DZ. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla PEDIDO_ITEM según el patrón del cuadernillo?",
            "options": ["cantidad, precio_unitario", "solo cantidad", "solo precio_unitario", "ninguno, solo FKs"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar cantidad y precio_unitario por ítem.",
                "1": "Incorrecto. Falta el precio_unitario.",
                "2": "Incorrecto. Falta la cantidad.",
                "3": "Incorrecto. Faltan ambos atributos requeridos."
            }
        }
        ,
        # --- EA. Caso Marketplace: Mini-ejercicio de Restricción ---
        {
            "topic": "EA. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué restricción asegura que el campo 'precio_unitario' de PEDIDO_ITEM sea mayor a 0?",
            "options": ["CHECK (precio_unitario > 0)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar condiciones sobre los valores de la columna.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no valores mayores a cero.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no condiciones de valor.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no de dominio."
            }
        },
        # --- EB. Caso ElectroHogar: Error de DDL ---
        {
            "topic": "EB. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué error ocurre si la tabla PEDIDO_ITEM no tiene restricción CHECK en el campo 'precio_unitario' para evitar valores negativos?",
            "options": ["Se pueden registrar ítems con precio negativo", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin CHECK, se pueden registrar ítems con precio negativo, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- EC. Caso Universidad: Mini-ejercicio de Restricción ---
        {
            "topic": "EC. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué restricción asegura que el campo 'codigo' de MATERIA sea único y no nulo?",
            "options": ["UNIQUE y NOT NULL", "CHECK", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. UNIQUE y NOT NULL garantizan unicidad y obligatoriedad.",
                "1": "Incorrecto. CHECK puede validar condiciones, pero no unicidad.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para el código.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no unicidad ni obligatoriedad."
            }
        },
        # --- ED. Caso Veterinaria: Error de Modelado ---
        {
            "topic": "ED. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué error ocurre si la tabla VACUNA no tiene restricción NOT NULL en el campo 'nombre'?",
            "options": ["Se pueden registrar vacunas sin nombre", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin NOT NULL, se pueden registrar vacunas sin nombre, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- EE. Caso Marketplace: Mini-ejercicio de Atributos ---
        {
            "topic": "EE. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué atributos propios debe tener la tabla CLIENTE según el patrón del cuadernillo?",
            "options": ["nombre, email, direccion", "solo nombre", "solo email", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar nombre, email y dirección.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
        ,
        # --- EF. Caso ElectroHogar: Mini-ejercicio de Restricción ---
        {
            "topic": "EF. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué restricción asegura que el campo 'fecha_pedido' de PEDIDO no sea futura?",
            "options": ["CHECK (fecha_pedido <= CURRENT_DATE)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. CHECK permite validar que la fecha no sea posterior a la actual.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no rango de fechas.",
                "2": "Incorrecto. PRIMARY KEY asegura unicidad y no nulos, no rango de fechas.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no rango de fechas."
            }
        },
        # --- EG. Caso Universidad: Error de DDL ---
        {
            "topic": "EG. Caso Universidad",
            "universe": "Universidad",
            "question": "¿Qué error ocurre si la tabla INSCRIPCION no tiene restricción NOT NULL en el campo 'estado'?",
            "options": ["Se pueden registrar inscripciones sin estado", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin NOT NULL, se pueden registrar inscripciones sin estado, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- EH. Caso Veterinaria: Mini-ejercicio de Restricción ---
        {
            "topic": "EH. Caso Veterinaria",
            "universe": "Veterinaria",
            "question": "¿Qué restricción asegura que el campo 'fecha_aplicacion' de APLICACION_VACUNA no sea nulo ni futuro?",
            "options": ["NOT NULL y CHECK (fecha_aplicacion <= CURRENT_DATE)", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. NOT NULL impide nulos y CHECK impide fechas futuras.",
                "1": "Incorrecto. UNIQUE asegura unicidad, no obligatoriedad ni rango de fechas.",
                "2": "Incorrecto. PRIMARY KEY suele usarse para el ID, no para la fecha.",
                "3": "Incorrecto. FOREIGN KEY asegura integridad referencial, no obligatoriedad ni rango de fechas."
            }
        },
        # --- EI. Caso Marketplace: Error de Modelado ---
        {
            "topic": "EI. Caso Marketplace",
            "universe": "Marketplace",
            "question": "¿Qué error ocurre si la tabla CLIENTE no tiene restricción NOT NULL en el campo 'nombre'?",
            "options": ["Se pueden registrar clientes sin nombre", "Mejora la flexibilidad", "No afecta la integridad", "No hay error"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Sin NOT NULL, se pueden registrar clientes sin nombre, lo cual es inconsistente.",
                "1": "Incorrecto. No se debe permitir flexibilidad a costa de la integridad.",
                "2": "Incorrecto. Sí afecta la integridad y la lógica de negocio.",
                "3": "Incorrecto. Sí hay un error de diseño."
            }
        },
        # --- EJ. Caso ElectroHogar: Mini-ejercicio de Atributos ---
        {
            "topic": "EJ. Caso ElectroHogar",
            "universe": "ElectroHogar",
            "question": "¿Qué atributos propios debe tener la tabla PEDIDO según el patrón del cuadernillo?",
            "options": ["fecha_pedido, total, estado", "solo fecha_pedido", "solo total", "ninguno, solo PK"],
            "type": "single",
            "correct_answers": [0],
            "justification": {
                "0": "Correcto. Se requiere registrar fecha, total y estado del pedido.",
                "1": "Incorrecto. Faltan atributos clave.",
                "2": "Incorrecto. Faltan atributos clave.",
                "3": "Incorrecto. Faltan todos los atributos requeridos."
            }
        }
]

# Ejemplo de formato de pregunta (las 300 reales serán generadas y colocadas aquí):
# {
#   "topic": "C. Atributos",
#   "universe": "Hospital",
#   "question": "Si solo guardamos la fecha de nacimiento de un paciente, su 'edad' es un atributo de tipo:",
#   "options": [
#     "Compuesto",
#     "Multivaluado",
#     "Derivado",
#     "Simple"
#   ],
#   "type": "single",
#   "correct_answers": [2],
#   "justification": {
#     "0": "Incorrecto. Un atributo compuesto es aquel que puede descomponerse en partes más pequeñas, como dirección (calle, número, ciudad).",
#     "1": "Incorrecto. Un atributo multivaluado es aquel que puede tener varios valores para una misma entidad, como teléfonos.",
#     "2": "Correcto. Un atributo derivado es aquel cuyo valor se puede calcular a partir de otro, como la edad desde la fecha de nacimiento.",
#     "3": "Incorrecto. Un atributo simple es indivisible, pero la edad aquí se deriva de la fecha de nacimiento."
#   }
# }
