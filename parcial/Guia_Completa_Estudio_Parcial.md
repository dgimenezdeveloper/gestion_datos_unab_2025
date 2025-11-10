# Guía Teórica Integral para el Pre‑Parcial de Gestión de Datos

Domina los conceptos clave para convertir requisitos en modelos conceptuales (MER), pasar a modelo lógico relacional y razonar sobre restricciones físicas (DDL). Está pensada para que, al terminarla, puedas resolver solos ejercicios como los del cuadernillo sin memorizar respuestas.

---

## Índice

1. De historias de usuario a MER (receta práctica)
2. Modelo Entidad‑Relación (Chen): entidades, relaciones y cardinalidades
3. Atributos: simple, compuesto, multivaluado, derivado (con decisiones de diseño)
4. Entidades débiles: criterios, PK compuesta y relación identificadora
5. Claves: natural, surrogada, candidatas, primaria, alternativa, foránea; criterios de elección
6. Transformación MER → Modelo Lógico Relacional (reglas de mapeo)
7. Lectura de DDL: NOT NULL, UNIQUE, CHECK, FK y políticas ON UPDATE/DELETE
8. ¿Dónde controlar cada regla? Conceptual vs Lógico vs Físico (heurística)
9. UoD comparados y patrones: Retail, Veterinaria, Marketplace
10. Mini‑ejercicios guiados (solo teoría aplicada y pistas)
11. Checklist de examen y errores frecuentes
12. Glosario mínimo

---

## 1) De historias de usuario a MER (receta práctica)

Formato típico de HU: "Como [rol], quiero [acción] para [beneficio]".

Cómo extraer piezas del MER:
- Sustantivos principales → Entidades (Cliente, Pedido, Producto, Categoría).
- Verbos de interacción → Relaciones (realiza, contiene, pertenece, supervisa).
- Propiedades/condiciones → Atributos (nombre, precio, fecha, cantidad, dirección).

Ejemplo base (ElectroHogar):
- HU: "Como cliente, quiero registrar mis pedidos para recibir productos".
	- cliente → Entidad
	- pedidos → Entidad (y relación Cliente–Pedido: "realiza")
	- productos → Entidad (y relación Pedido–Producto: vía Ítem/Detalle)
	- recibir → sugiere la relación de cumplimiento/entrega (no siempre modelada si no hay logística)

Tips:
- Si un verbo implica datos propios (fecha, cantidad, precio), la relación suele materializarse como entidad intermedia (tabla puente), p. ej., PEDIDO_ITEM con cantidad.
- Si la HU menciona "cada", "muchos", "varios", anticipa cardinalidades.

---

## 2) Modelo Entidad‑Relación (Chen)

Elementos básicos:
- Entidad (rectángulo): objeto con identidad propia (CLIENTE, PRODUCTO).
- Relación (rombo): asociación entre entidades (CLIENTE realiza PEDIDO).
- Atributo (óvalo): propiedad de entidad/relación (precio, fecha, cantidad).

Cardinalidades y participación:
- 1:1, 1:N, N:M; participación total (obligatoria) vs parcial (opcional).
- Heurística rápida:
	- 1:N: la FK va en el lado N.
	- N:M: se implementa con una tabla de intersección.

Relaciones especiales:
- Unarias/recursivas: una entidad se relaciona consigo misma (Empleado supervisa Empleado). 
	- Lo usual es 1:N (cada empleado tiene 0..1 supervisor; un supervisor puede supervisar a N).

Patrón ElectroHogar (sin facturación):
- CLIENTE 1—N PEDIDO (participación total en PEDIDO: todo pedido tiene cliente).
- PEDIDO 1—N PEDIDO_ITEM.
- PRODUCTO 1—N PEDIDO_ITEM.
- CATEGORIA 1—N PRODUCTO (cada producto en una sola categoría).

---

## 3) Atributos: tipos y decisiones de diseño

Tipos por descomposición:
- Simple: indivisible (precio, edad).
- Compuesto: se descompone (dirección → calle, número, ciudad, CP).

Por cardinalidad de valores:
- Monovaluado: un solo valor por entidad (DNI, email principal).
- Multivaluado: varios valores por entidad (teléfonos, emails alternativos). En Chen: óvalo doble.

Por origen:
- Almacenado: persiste como columna.
- Derivado: se calcula (edad desde fecha_nacimiento; total = cantidad×precio). En Chen: óvalo punteado.

¿Cuándo pasar de multivaluado a entidad propia?
- Hay metadatos por valor (tipo, preferido, verificado).
- Se requiere histórico (altas/bajas/cambios por valor).
- Validaciones diferentes según tipo.
- El valor puede relacionarse con otras entidades.

Ejemplo (teléfonos de cliente):
- Atributo multivaluado simple si solo guardas números.
- Entidad TELEFONO (débil) si además hay tipo, preferido, validaciones o histórico.

Regla práctica en el modelo lógico:
- Un multivaluado se implementa como tabla separada 1:N con la entidad principal.

---

## 4) Entidades débiles

Definición: entidad cuya existencia e identificación dependen de otra (propietaria).

Señales de entidad débil:
- Identidad depende de la propietaria → PK incluye la PK de la propietaria.
- Participación total en la relación con la propietaria.
- Ciclo de vida ligado; no existe sin la propietaria.

Relación identificadora:
- Se dibuja con líneas dobles en Chen.
- En el lógico: PK compuesta y FK a la propietaria.

Ejemplo TELEFONO de CLIENTE:
- PK apropiada: (cliente_id, numero).
- FK: telefono.cliente_id → cliente.id.

Anti‑patrones:
- Surrogada aislada (telefono_id) sin necesidad: rompe dependencia natural si el negocio no la requiere.

---

## 5) Claves (keys)

Tipos y definiciones:
- Clave natural: proviene del negocio (DNI, CUIL, código de producto).
- Clave surrogada: sintética sin significado (id autoincremental, UUID).
- Claves candidatas: conjuntos mínimos que identifican una fila (email, DNI, CUIL…); una de ellas será la PK.
- Clave primaria (PK): candidata elegida como identificador principal.
- Clave alternativa: candidata no elegida como PK (se implementa con UNIQUE).
- Clave foránea (FK): referencia a la PK (o UNIQUE) de otra tabla.

Criterios para elegir PK (preferibles):
- Única y estable (no cambia con el tiempo).
- Corta (eficiente en FKs e índices).
- No sensible (evita exponer datos personales).

Cuándo usar PK compuesta:
- Tablas de intersección (N:M): p. ej., (pedido_id, producto_id) en PEDIDO_ITEM.
- Entidades débiles: incluir PK de la propietaria + discriminador.

Privacidad/estabilidad (malas PK típicas):
- Email, teléfono: cambian y exponen datos; mejor surrogada.

Ejemplos:
```sql
-- PK surrogada + claves alternativas
CREATE TABLE CLIENTE (
	id           BIGSERIAL PRIMARY KEY,
	dni          VARCHAR(10) UNIQUE,
	cuil         VARCHAR(13) UNIQUE,
	email        VARCHAR(120) UNIQUE,
	nombre       VARCHAR(100) NOT NULL
);

-- Intersección con PK compuesta
CREATE TABLE PEDIDO_ITEM (
	pedido_id    BIGINT NOT NULL REFERENCES PEDIDO(id),
	producto_id  BIGINT NOT NULL REFERENCES PRODUCTO(id),
	cantidad     INTEGER NOT NULL CHECK (cantidad > 0),
	PRIMARY KEY (pedido_id, producto_id)
);
```

---

## 6) Transformación MER → Lógico (reglas de mapeo)

Reglas generales:
1. Entidad fuerte → Tabla (atributos → columnas).
2. Relación 1:N → FK en el lado N (la relación no va como tabla).
3. Relación N:M → Tabla puente con FKs a ambas y, usualmente, PK compuesta.
4. Atributo multivaluado → Tabla 1:N con PK compuesta (pk_propietaria + valor) o surrogada si conviene.
5. Entidad débil → Tabla con PK compuesta incluyendo PK de propietaria; relación identificadora implícita por la FK.
6. Atributos derivados → se calculan (consulta/vista/columna generada), no se almacenan obligatoriamente.

Ejemplo ElectroHogar (resumen SQL):
```sql
CREATE TABLE CATEGORIA (
	id      BIGSERIAL PRIMARY KEY,
	nombre  VARCHAR(80) UNIQUE NOT NULL
);

CREATE TABLE PRODUCTO (
	id           BIGSERIAL PRIMARY KEY,
	nombre       VARCHAR(120) NOT NULL,
	precio       NUMERIC(10,2) NOT NULL CHECK (precio >= 0),
	categoria_id BIGINT NOT NULL REFERENCES CATEGORIA(id)
);

CREATE TABLE CLIENTE (
	id     BIGSERIAL PRIMARY KEY,
	nombre VARCHAR(120) NOT NULL,
	email  VARCHAR(120) UNIQUE
);

CREATE TABLE PEDIDO (
	id          BIGSERIAL PRIMARY KEY,
	fecha       DATE NOT NULL,
	cliente_id  BIGINT NOT NULL REFERENCES CLIENTE(id)
);

CREATE TABLE PEDIDO_ITEM (
	pedido_id    BIGINT NOT NULL REFERENCES PEDIDO(id),
	producto_id  BIGINT NOT NULL REFERENCES PRODUCTO(id),
	cantidad     INTEGER NOT NULL CHECK (cantidad > 0),
	PRIMARY KEY (pedido_id, producto_id)
);

CREATE TABLE TELEFONO (
	cliente_id BIGINT NOT NULL REFERENCES CLIENTE(id),
	numero     VARCHAR(20) NOT NULL,
	tipo       VARCHAR(15),
	preferido  BOOLEAN DEFAULT false,
	PRIMARY KEY (cliente_id, numero)
);
```

---

## 7) Lectura de DDL (interpretación)

Qué buscar siempre:
- NOT NULL: obligatoriedad del dato.
- UNIQUE: unicidad (claves alternativas).
- CHECK: reglas de dominio (precio ≥ 0, cantidad > 0).
- FK + ON UPDATE/DELETE: integridad referencial y políticas.

Políticas típicas de FK:
- ON DELETE RESTRICT/NO ACTION (por defecto): impide borrar si hay referidos.
- ON DELETE CASCADE: borra hijos al borrar padre (útil pero peligroso).
- ON DELETE SET NULL: conserva hijos con FK a NULL (si la FK lo permite).
- ON UPDATE CASCADE: propaga cambios de PK/UNIQUE (poco frecuente en PK reales).

Ejemplo de lectura:
```sql
CREATE TABLE PRODUCTO (
	id           BIGSERIAL PRIMARY KEY,
	nombre       VARCHAR(120),
	categoria_id BIGINT NOT NULL REFERENCES CATEGORIA(id),
	precio       NUMERIC(10,2) CHECK (precio >= 0)
);
```
Interpretación:
- No se permiten precios negativos.
- El nombre puede repetirse (no hay UNIQUE).
- categoria_id es obligatorio (NOT NULL) y debe existir en CATEGORIA.
- Si no se declara ON DELETE, por defecto no podrás borrar una categoría con productos (RESTRICT/NO ACTION).
- ON UPDATE de id de CATEGORIA no suele usarse; si se declara CASCADE, actualizará producto.categoria_id.

---

## 8) ¿Dónde controlar cada regla? (capa principal)

Heurística rápida:
- Conceptual (MER): estructura del negocio (cardinalidades, participación, exclusividades, jerarquías).
- Lógico (Relacional): forma relacional, normalización, ubicación de FKs, claves candidatas.
- Físico (DDL/constraints): validaciones de dominio, unicidad, integridad referencial efectiva, políticas de borrado/actualización.

Ejemplos:
- "Producto pertenece a una única Categoría" → Conceptual (relación 1:N), y se materializa con FK NOT NULL en Físico.
- "Precio ≥ 0" → Físico (CHECK).
- "No se puede eliminar un Cliente con Pedidos" → Físico (FK con RESTRICT/NO ACTION).
- "Pedido debe tener al menos un Ítem" → Requiere control en Físico (trigger, constraint de negocio) o a nivel de aplicación/servicio.

---

## 9) UoD comparados y patrones

Retail (ElectroHogar): teléfonos 0..N con tipo/preferido
- Mejor como entidad dependiente (débil) TELEFONO con PK (cliente_id, numero) para poder guardar tipo/preferido.

Veterinaria: Mascota ↔ Vacuna con fecha y dosis
- Relación N:M con tabla APLICACION_VACUNA que incluye atributos propios (fecha, dosis, profesional). La PK puede ser (mascota_id, vacuna_id, fecha).

Marketplace: Vendedor ↔ Producto con precio de publicación y stock
- Relación N:M con tabla PUBLICACION (vendedor_id, producto_id) + atributos (precio, stock, estado, fecha_publicacion).

Matriz de decisión (simplificada):
- ¿La relación tiene datos propios? → N:M con tabla puente.
- ¿El atributo tiene metadatos/histórico? → Modelar como entidad.
- ¿Identidad dependiente? → Entidad débil + PK compuesta.

---

## 10) Mini‑ejercicios guiados (sin resolver)

1) HU: "Como alumno, quiero inscribirme a cursos para aprobar materias".
- Identifica entidades, relaciones, cardinalidades y si hay tabla puente.
- ¿Qué atributos tendría la inscripción?

2) "Un vehículo puede tener 0..N conductores autorizados; cada conductor autorizado tiene fecha_desde/hasta".
- ¿Es atributo multivaluado o entidad/relación? Modela en MER y mapea a lógico.

3) "Cada empleado tiene 0..1 supervisor; un supervisor supervisa a N empleados".
- Modela la relación unaria y su FK en el lógico.

4) DDL de LÍNEA_FACTURA con CHECK (cantidad>0) y FK a FACTURA y PRODUCTO.
- ¿Qué PK elegirías para evitar ítems duplicados? ¿Por qué?

5) Teléfonos de proveedor con tipo (fijo/móvil) y prioridad; pueden cambiar en el tiempo.
- ¿Entidad débil? Propón PK y columnas.

---

## 11) Checklist de examen y errores frecuentes

Checklist rápido:
- [ ] Marqué correctamente entidades, relaciones y atributos.
- [ ] Elegí cardinalidades y participación con base en el enunciado.
- [ ] Decidí bien entre atributo multivaluado vs entidad propia.
- [ ] Identifiqué claves candidatas y elegí una PK adecuada.
- [ ] Mapeé 1:N (FK en el lado N) y N:M (tabla puente).
- [ ] Revisé restricciones en DDL: NOT NULL, UNIQUE, CHECK, FKs.
- [ ] Ubicación de control: conceptual vs físico.

Errores frecuentes:
- Confundir N:M con 1:N por leer "muchos" solo en un lado.
- Elegir email/DNI como PK sin evaluar privacidad/estabilidad.
- No usar PK compuesta en tablas de intersección (permitiendo duplicados).
- Guardar atributos derivados como columnas obligatorias sin justificación.
- Suponer que el SGBD borra en cascada sin que esté declarado.

---

## 12) Glosario mínimo

- Cardinalidad: número de ocurrencias que pueden/ deben relacionarse entre entidades (1:1, 1:N, N:M).
- Participación total/parcial: obligatoriedad de la relación para una entidad.
- Atributo derivado: se calcula a partir de otros (edad desde fecha_nacimiento).
- Entidad débil: depende de otra para existir e identificarse; PK compuesta.
- Clave candidata: conjunto mínimo que identifica filas; una se elige PK.
- Clave alternativa: candidata no elegida, se implementa con UNIQUE.
- Clave foránea (FK): referencia a la PK/UNIQUE de otra tabla.
- Tabla puente: tabla de intersección para relaciones N:M.

---

Sugerencia de estudio: repasa esta guía y, por cada sección del cuadernillo, identifica qué concepto aplica. Practica dibujando el MER, luego mapea al lógico y, por último, escribe (o al menos lee) el DDL resultante para verificar que tus decisiones se reflejan en restricciones concretas.

