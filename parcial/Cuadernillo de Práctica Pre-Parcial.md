# Guía Completa de Estudio: Gestión de Datos
## Todo lo que necesitas saber para dominar el Parcial

> **Objetivo**: Dominar completamente todos los conceptos desde el análisis de requisitos hasta la implementación física de bases de datos, pasando por MER y modelo lógico.

---

## 📚 Índice de Contenidos

1. [Análisis de Requisitos y Historias de Usuario](#1-análisis-de-requisitos-y-historias-de-usuario)
2. [Modelo Entidad-Relación (MER)](#2-modelo-entidad-relación-mer)
3. [Cardinalidades y Tipos de Relación](#3-cardinalidades-y-tipos-de-relación)
4. [Atributos: Tipos y Características](#4-atributos-tipos-y-características)
5. [Entidades Débiles](#5-entidades-débiles)
6. [Claves: Tipos y Características](#6-claves-tipos-y-características)
7. [Modelo Lógico Relacional](#7-modelo-lógico-relacional)
8. [Modelo Físico y DDL](#8-modelo-físico-y-ddl)
9. [Capas de Control de Restricciones](#9-capas-de-control-de-restricciones)
10. [Casos de Estudio Comparados](#10-casos-de-estudio-comparados)
11. [Respuestas Correctas del Cuadernillo](#11-respuestas-correctas-del-cuadernillo)

---

## 1. Análisis de Requisitos y Historias de Usuario

### 1.1 ¿Qué son las Historias de Usuario?

Las **Historias de Usuario (HU)** son descripciones simples y breves de una funcionalidad desde la perspectiva del usuario. Siguen el formato:

```
"Como [tipo de usuario], quiero [acción/funcionalidad] para [beneficio/objetivo]"
```

### 1.2 Identificación de Elementos del MER desde HU

Cuando analizas una HU, debes identificar:

#### **Sustantivos → Entidades**
- **Cliente**, **Producto**, **Pedido**, **Categoría**
- Son "cosas" del mundo real que necesitan almacenarse

#### **Verbos → Relaciones**
- **registrar**, **recibir**, **pertenece**, **contiene**
- Representan interacciones entre entidades

#### **Adjetivos/Propiedades → Atributos**
- **nombre**, **precio**, **fecha**, **cantidad**
- Características que describen las entidades

### 1.3 Ejemplo Práctico

**HU**: "Como cliente, quiero registrar mis pedidos para recibir productos."

**Análisis**:
- **cliente** = Entidad ✓
- **pedidos** = Entidad ✓
- **productos** = Entidad ✓
- **registrar** = Relación entre Cliente y Pedido ✓
- **recibir** = Relación entre Pedido y Producto ✓

---

## 2. Modelo Entidad-Relación (MER)

### 2.1 Conceptos Fundamentales

#### **Entidad**
- Representación de un objeto del mundo real
- Tiene existencia independiente
- Se representa con un **rectángulo**
- Ejemplos: Cliente, Producto, Pedido

#### **Relación**
- Asociación entre dos o más entidades
- Se representa con un **rombo**
- Ejemplos: Cliente "realiza" Pedido, Producto "pertenece" Categoría

#### **Atributo**
- Propiedad que describe una entidad o relación
- Se representa con un **óvalo**
- Ejemplos: nombre, precio, fecha

### 2.2 Notación Chen

```
[CLIENTE] ----< realiza >---- [PEDIDO] ----< contiene >---- [PRODUCTO]
    |                              |                           |
  nombre                         fecha                      precio
   DNI                         cantidad                      nombre
```

### 2.3 Ejemplo: ElectroHogar

```
Sistema ElectroHogar (sin facturación):

CLIENTE 1----N PEDIDO 1----N PEDIDO_ITEM N----1 PRODUCTO N----1 CATEGORIA
```

**Relaciones**:
- Cliente 1:N Pedido (Un cliente puede tener muchos pedidos)
- Pedido 1:N PedidoItem (Un pedido puede tener muchos items)
- Producto 1:N PedidoItem (Un producto puede estar en muchos items)
- Categoría 1:N Producto (Una categoría puede tener muchos productos)

---

## 3. Cardinalidades y Tipos de Relación

### 3.1 Tipos de Cardinalidad

#### **1:1 (Uno a Uno)**
- Una entidad se relaciona con exactamente una de la otra
- **Ejemplo**: Persona - Pasaporte
- Cada persona tiene un único pasaporte, cada pasaporte pertenece a una única persona

#### **1:N (Uno a Muchos)**
- Una entidad se relaciona con muchas de la otra, pero cada una de la segunda se relaciona con solo una de la primera
- **Ejemplo**: Cliente - Pedido
- Un cliente puede tener muchos pedidos, pero cada pedido pertenece a un único cliente

#### **N:M (Muchos a Muchos)**
- Ambas entidades pueden relacionarse con muchas de la otra
- **Ejemplo**: Estudiante - Materia
- Un estudiante puede cursar muchas materias, una materia puede ser cursada por muchos estudiantes

### 3.2 Participación

#### **Total (Obligatoria)**
- Toda instancia de la entidad debe participar en la relación
- Se representa con **línea doble**
- **Ejemplo**: Todo Pedido debe tener un Cliente

#### **Parcial (Opcional)**
- No todas las instancias deben participar
- Se representa con **línea simple**
- **Ejemplo**: No todo Cliente debe tener Pedidos

### 3.3 Relaciones Especiales

#### **Relación Unaria (Recursiva)**
- Una entidad se relaciona consigo misma
- **Ejemplo**: Empleado supervisa Empleado
- Un empleado puede supervisar a otros empleados

#### **Relación Binaria**
- Entre dos entidades diferentes
- **Ejemplo**: Cliente realiza Pedido

---

## 4. Atributos: Tipos y Características

### 4.1 Clasificación por Simplicidad

#### **Atributo Simple**
- No se puede descomponer en partes más pequeñas
- **Ejemplos**: edad, precio, cantidad
- Se almacena en una sola columna

#### **Atributo Compuesto**
- Se puede descomponer en partes más pequeñas
- **Ejemplo**: dirección (calle, número, ciudad, CP)
- En el modelo lógico se puede:
  - Almacenar como un solo campo concatenado
  - Dividir en múltiples columnas

### 4.2 Clasificación por Cardinalidad

#### **Atributo Monovaluado**
- Tiene un solo valor para cada entidad
- **Ejemplos**: DNI, nombre, fecha_nacimiento

#### **Atributo Multivaluado**
- Puede tener múltiples valores para una entidad
- **Ejemplos**: teléfonos, emails, idiomas
- Se representa con **óvalo doble**
- En el modelo lógico se resuelve creando una tabla separada

### 4.3 Clasificación por Origen

#### **Atributo Almacenado**
- Se almacena directamente en la base de datos
- **Ejemplos**: fecha_nacimiento, precio

#### **Atributo Derivado**
- Se calcula a partir de otros atributos
- **Ejemplos**: edad (desde fecha_nacimiento), total (desde precio × cantidad)
- Se representa con **óvalo punteado**
- Generalmente NO se almacena en el modelo lógico

### 4.4 Cuándo Convertir Multivaluado a Entidad

Convierte un atributo multivaluado a entidad cuando:

1. **Hay metadatos** por cada valor (tipo, preferido, activo)
2. **Se requiere histórico** de cambios
3. **Validaciones distintas** por tipo
4. **Relaciones complejas** con otras entidades

**Ejemplo**: Teléfonos con tipo (móvil, fijo) y preferencia

```
ANTES: Cliente [teléfonos]

DESPUÉS: 
CLIENTE 1----N TELEFONO
TELEFONO (cliente_id, numero, tipo, preferido)
```

---

## 5. Entidades Débiles

### 5.1 ¿Qué es una Entidad Débil?

Una **entidad débil** es aquella que:
- **No puede existir independientemente**
- Su **identidad depende** de otra entidad (propietaria)
- Tiene **participación total** en la relación identificadora
- Se representa con **rectángulo doble**

### 5.2 Características

#### **Dependencia de Existencia**
- No puede existir sin la entidad propietaria
- Su ciclo de vida está ligado al de la propietaria

#### **Dependencia de Identificación**
- Su clave primaria incluye la clave de la entidad propietaria
- Usa **clave primaria compuesta**

### 5.3 Ejemplo: Teléfono de Cliente

```
CLIENTE ====< tiene >==== TELEFONO
   |                         |
   id                    numero
   nombre                tipo
```

**Relación Identificadora** (línea doble):
- TELEFONO depende de CLIENTE
- No puede existir un teléfono sin cliente
- PK de TELEFONO: (cliente_id, numero)

### 5.4 Señales de Entidad Débil

✅ **SÍ es entidad débil cuando**:
- Identidad depende de otra entidad
- Participación total en relación con propietaria
- Los valores pueden repetirse entre diferentes propietarias
- Ciclo de vida dependiente

❌ **NO es entidad débil cuando**:
- Tiene identificación propia independiente
- Puede existir sin la otra entidad
- Ciclo de vida completamente independiente

---

## 6. Claves: Tipos y Características

### 6.1 Clave Candidata

**Definición**: Conjunto mínimo de atributos que identifica únicamente cada instancia de una entidad.

**Características**:
- **Unicidad**: No hay dos instancias con los mismos valores
- **Minimalidad**: No se puede quitar ningún atributo sin perder unicidad

**Ejemplos en CLIENTE**:
- (DNI)
- (email)
- (CUIL)
- (id) - surrogada

### 6.2 Clave Primaria (PK)

**Definición**: La clave candidata elegida como identificador principal.

**Criterios para elegir**:
✅ **Buenos criterios**:
- **Única**: Identifica unívocamente
- **Corta**: Pocas columnas, eficiente
- **Estable**: No cambia frecuentemente
- **No sensible**: No contiene datos personales críticos

❌ **Malos criterios**:
- Datos sensibles (DNI para privacidad)
- Valores que pueden cambiar (email)
- Demasiado larga

### 6.3 Clave Alternativa/Secundaria

**Definición**: Claves candidatas que NO fueron elegidas como PK.

**Uso**: Se implementan como UNIQUE constraints

**Ejemplo**:
```sql
CLIENTE (
    id INTEGER PRIMARY KEY,    -- PK elegida
    dni VARCHAR(8) UNIQUE,     -- Clave alternativa
    email VARCHAR(100) UNIQUE  -- Clave alternativa
)
```

### 6.4 Clave Foránea (FK)

**Definición**: Atributo(s) que referencian la PK de otra tabla.

**Reglas**:
- La FK está en la tabla del lado "N" de la relación 1:N
- Debe referenciar una PK o UNIQUE existente
- Mantiene la integridad referencial

**Ejemplo**:
```sql
PEDIDO (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER REFERENCES CLIENTE(id)  -- FK
)
```

### 6.5 Tipos de Claves por Origen

#### **Clave Natural**
- Surge del dominio del negocio
- Tiene significado para los usuarios
- **Ejemplos**: DNI, código de producto, patente

#### **Clave Surrogada**
- Identificador sintético sin significado de negocio
- Generada automáticamente
- **Ejemplos**: id autoincremental, UUID

**Ventajas de Surrogadas**:
- Estables (no cambian)
- Eficientes (números enteros)
- Sin restricciones de formato
- No revelan información sensible

### 6.6 Claves Compuestas

**Cuándo usar**:
- En tablas de intersección (N:M)
- Cuando la unicidad surge de múltiples columnas
- En entidades débiles

**Ejemplo**:
```sql
PEDIDO_ITEM (
    pedido_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    PRIMARY KEY (pedido_id, producto_id)  -- PK compuesta
)
```

---

## 7. Modelo Lógico Relacional

### 7.1 Transformación MER → Lógico

#### **Reglas de Transformación**:

1. **Entidad → Tabla**
   - Cada entidad se convierte en una tabla
   - Atributos simples → columnas

2. **Relación 1:N**
   - FK en la tabla del lado "N"
   - La relación "desaparece" como tabla separada

3. **Relación N:M**
   - Tabla de intersección con FKs de ambas entidades
   - PK compuesta con ambas FKs

4. **Atributo Multivaluado**
   - Tabla separada 1:N con la entidad principal

5. **Entidad Débil**
   - PK compuesta incluyendo FK de la propietaria

### 7.2 Ejemplo: ElectroHogar

**Modelo Lógico**:
```sql
CLIENTE (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE
)

PEDIDO (
    id INTEGER PRIMARY KEY,
    fecha DATE,
    cliente_id INTEGER REFERENCES CLIENTE(id)
)

CATEGORIA (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE
)

PRODUCTO (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2) CHECK (precio >= 0),
    categoria_id INTEGER NOT NULL REFERENCES CATEGORIA(id)
)

PEDIDO_ITEM (
    pedido_id INTEGER REFERENCES PEDIDO(id),
    producto_id INTEGER REFERENCES PRODUCTO(id),
    cantidad INTEGER CHECK (cantidad > 0),
    PRIMARY KEY (pedido_id, producto_id)
)

TELEFONO (
    cliente_id INTEGER REFERENCES CLIENTE(id),
    numero VARCHAR(15),
    tipo VARCHAR(10),
    PRIMARY KEY (cliente_id, numero)
)
```

### 7.3 Restricciones Importantes

#### **NOT NULL**
- El atributo debe tener valor
- **Ejemplo**: categoria_id en PRODUCTO

#### **UNIQUE**
- No se permiten valores duplicados
- **Ejemplo**: email en CLIENTE

#### **CHECK**
- Validación de dominio
- **Ejemplo**: precio >= 0, cantidad > 0

#### **REFERENCES (FK)**
- Integridad referencial
- **Ejemplo**: cliente_id REFERENCES CLIENTE(id)

---

## 8. Modelo Físico y DDL

### 8.1 Data Definition Language (DDL)

El **DDL** es el código SQL que define la estructura física de la base de datos.

### 8.2 Lectura de Restricciones

Cuando veas DDL, identifica:

#### **Restricciones de Dominio**
```sql
precio DECIMAL(10,2) CHECK (precio >= 0)
```
- No permite precios negativos

#### **Restricciones de Clave**
```sql
PRIMARY KEY (pedido_id, producto_id)
```
- Define la clave primaria compuesta

#### **Restricciones de Integridad Referencial**
```sql
categoria_id INTEGER NOT NULL REFERENCES CATEGORIA(id) ON UPDATE CASCADE
```
- FK obligatoria con propagación de actualizaciones

#### **Políticas de Borrado/Actualización**
- **CASCADE**: Propaga la operación
- **RESTRICT**: Impide la operación si hay referencias
- **SET NULL**: Asigna NULL a las FKs
- **SET DEFAULT**: Asigna valor por defecto

### 8.3 Interpretación de DDL

Si ves:
```sql
CREATE TABLE PRODUCTO (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    categoria_id INTEGER NOT NULL REFERENCES CATEGORIA(id),
    precio DECIMAL(10,2) CHECK (precio >= 0)
);
```

**Significa**:
- ✅ No se permite precio negativo (CHECK)
- ✅ Dos productos pueden repetir nombre (no hay UNIQUE)
- ❌ categoria_id NO puede ser NULL (NOT NULL)
- ✅ Al cambiar id de CATEGORIA, se actualiza producto.categoria_id (por defecto)
- ❌ NO se puede borrar una categoría con productos (por defecto RESTRICT)

---

## 9. Capas de Control de Restricciones

### 9.1 Las Tres Capas

#### **Capa Conceptual (MER)**
- **Qué controlar**: Reglas de negocio estructurales
- **Ejemplos**:
  - Cardinalidades (1:N, N:M)
  - Participación (total/parcial)
  - Jerarquías de especialización

#### **Capa Lógica (Relacional)**
- **Qué controlar**: Estructura de datos y relaciones
- **Ejemplos**:
  - Claves primarias y foráneas
  - Normalización
  - Integridad referencial básica

#### **Capa Física (DDL/Constraints)**
- **Qué controlar**: Validaciones específicas y restricciones detalladas
- **Ejemplos**:
  - Dominios (CHECK constraints)
  - Políticas de borrado/actualización
  - Índices y optimizaciones

### 9.2 Guía de Decisión

| Restricción | Capa Principal |
|-------------|----------------|
| "Pedido debe tener al menos un Ítem" | **Físico** (CHECK, trigger) |
| "Producto pertenece a una única Categoría" | **Conceptual** (MER: 1:N) |
| "Precio ≥ 0" | **Físico** (CHECK constraint) |
| "No eliminar Cliente con Pedidos" | **Físico** (RESTRICT) |
| "Cliente puede tener muchos Pedidos" | **Conceptual** (MER: 1:N) |
| "Email debe ser único" | **Físico** (UNIQUE) |

### 9.3 ¿Por qué esta División?

#### **Conceptual**: Diseño del negocio
- Define QUÉ necesita el negocio
- Independiente de la tecnología
- Comunicación con stakeholders

#### **Lógico**: Estructura de datos
- Define CÓMO organizar los datos
- Independiente del SGBD específico
- Base para múltiples implementaciones

#### **Físico**: Implementación específica
- Define restricciones exactas y optimizaciones
- Específico del SGBD
- Máximo control y validación

---

## 10. Casos de Estudio Comparados

### 10.1 Retail: ElectroHogar

**Problema**: Cliente con 0..N teléfonos, con "tipo" y "preferido"

**Solución**: Entidad débil TELEFONO
```sql
TELEFONO (
    cliente_id INTEGER REFERENCES CLIENTE(id),
    numero VARCHAR(15),
    tipo VARCHAR(10),      -- móvil, fijo, trabajo
    preferido BOOLEAN,
    PRIMARY KEY (cliente_id, numero)
)
```

**¿Por qué entidad débil?**
- Metadatos por teléfono (tipo, preferido)
- Dependencia de identificación
- No existe teléfono sin cliente

### 10.2 Veterinaria: Mascota-Vacuna

**Problema**: Mascota con varias Vacunas en distintas fechas; Vacuna aplicada a muchas Mascotas

**Análisis**:
- Una Mascota puede tener múltiples Vacunas
- Una Vacuna puede aplicarse a múltiples Mascotas
- Cada aplicación tiene fecha y dosis específica

**Solución**: N:M con tabla puente
```sql
MASCOTA (id, nombre, especie, ...)
VACUNA (id, nombre, laboratorio, ...)
APLICACION_VACUNA (
    mascota_id INTEGER REFERENCES MASCOTA(id),
    vacuna_id INTEGER REFERENCES VACUNA(id),
    fecha_aplicacion DATE,
    dosis VARCHAR(20),
    veterinario VARCHAR(100),
    PRIMARY KEY (mascota_id, vacuna_id, fecha_aplicacion)
)
```

### 10.3 Marketplace: Producto-Vendedor

**Problema**: Un Producto puede ser ofrecido por varios Vendedores; un Vendedor ofrece muchos Productos

**Análisis**:
- Relación N:M
- Cada publicación tiene precio específico, stock, estado

**Solución**: N:M con tabla puente PUBLICACION
```sql
VENDEDOR (id, nombre, email, ...)
PRODUCTO (id, nombre, descripcion, ...)
PUBLICACION (
    vendedor_id INTEGER REFERENCES VENDEDOR(id),
    producto_id INTEGER REFERENCES PRODUCTO(id),
    precio DECIMAL(10,2),
    stock INTEGER,
    estado VARCHAR(20),    -- activo, pausado, finalizado
    fecha_publicacion DATE,
    PRIMARY KEY (vendedor_id, producto_id)
)
```

### 10.4 Patrones de Decisión

#### **¿Atributo Multivaluado vs Entidad?**
- **Multivaluado simple**: valores simples sin metadatos
- **Entidad**: valores con metadatos, validaciones, o histórico

#### **¿1:N vs N:M?**
- **1:N**: Una entidad puede relacionarse con muchas, pero cada una de las "muchas" se relaciona con solo una
- **N:M**: Ambas pueden relacionarse con muchas de la otra

#### **¿Entidad Fuerte vs Débil?**
- **Fuerte**: Existencia independiente, identificación propia
- **Débil**: Dependencia existencial e identificación de otra entidad

---

## 11. Respuestas Correctas del Cuadernillo

### Sección A: Historias/Requisitos → MER
1. **[X] cliente = Entidad [X] pedidos = Entidad [X] productos = Entidad [X] recibir = Relación [ ] domicilio = Atributo**
2. **[X] 1:N (Categoría→Producto)**

### Sección B: Cardinalidades
3. **[X] 1:N**
4. **[X] 1:N**
5. **[X] Unaria (recursiva) 1:N**
6. **[X] Verdadero**

### Sección C: Atributos
7. **[X] Atributo multivaluado**
8. **[X] Atributo compuesto**
9. **[X] Hay metadatos por teléfono [X] Se requiere histórico/cambios [X] Validaciones distintas por tipo**
10. **[X] Tabla relacionada 1:N con la entidad principal**
11. **[X] Marcarse como derivado en MER y calcularse en Físico/consulta**
12. **[X] Verdadero**

### Sección D: Entidades Débiles
13. **[X] Entidad débil TELEFONO dependiente de CLIENTE**
14. **[X] (cliente_id, numero)**
15. **[X] Identidad depende de CLIENTE [X] Participación total [X] Número se reutiliza entre clientes**
16. **[X] telefono.cliente_id → cliente.id**
17. **[X] Verdadero**

### Sección E: Claves
18. **[X] DNI [X] Correo institucional único**
19. **[X] Identificador sintético sin significado de negocio**
20. **[X] (email) [X] (dni) [X] (id surrogada) [X] (cuil)**
21. **[X] Una candidata elegida como identificador principal**
22. **[X] Una candidata no elegida como PK**
23. **[X] (pedido_id, producto_id)**
24. **[X] Única [X] Corta [X] Estable**
25. **[X] email** (por privacidad/estabilidad)
26. **[X] PEDIDO (cliente_id)**
27. **[X] Verdadero**

### Sección F: DDL
28. **[X] No se permite precio negativo [X] Dos Productos pueden repetir nombre [X] Al cambiar id de CATEGORIA se actualiza**

### Sección G: Capas de Control
29. **[X] Físico (DDL/Constraints)**
30. **[X] Conceptual (MER)**
31. **[X] Físico (DDL/Constraints)**
32. **[X] Físico (DDL/Constraints)**

### Sección H: UoD Comparados
33. **[X] Entidad débil TELEFONO dependiente de CLIENTE**
34. **[X] N:M con tabla puente (fecha, dosis…)**
35. **[X] N:M con tabla puente PUBLICACIÓN**

---

## 🎯 Estrategias para el Parcial

### 1. Análisis Sistemático
- Lee cada pregunta 2 veces
- Identifica palabras clave (sustantivos, verbos, cardinalidades)
- Aplica las reglas de transformación paso a paso

### 2. Verificación de Respuestas
- En preguntas de múltiple opción, elimina las incorrectas primero
- Verifica que tu respuesta cubra todos los aspectos de la pregunta
- Revisa las respuestas "varias opciones" cuidadosamente

### 3. Gestión del Tiempo
- 45-60 minutos total
- ~1.5 minutos por pregunta
- Deja las más difíciles para el final
- Revisa todas antes de entregar

### 4. Errores Comunes a Evitar
- Confundir 1:N con N:M
- No identificar entidades débiles correctamente
- Elegir la capa incorrecta para restricciones
- No considerar todas las opciones en preguntas múltiples

---

## 📖 Referencias y Profundización

### Libros Recomendados
1. **Elmasri & Navathe** - Fundamentals of Database Systems
2. **Ramez & Shamkant** - Database System Concepts
3. **García-Molina, Ullman & Widom** - Database Systems: The Complete Book

### Temas para Estudio Adicional
- Normalización (1FN, 2FN, 3FN, BCNF)
- Álgebra relacional
- SQL avanzado (joins, subconsultas, agregaciones)
- Diseño físico (índices, particionamiento)
- Transacciones y concurrencia

---

**¡Éxito en tu parcial! 🚀**

> Recuerda: La clave está en entender los conceptos, no en memorizar. Practica con ejemplos reales y siempre pregúntate "¿por qué?" en cada decisión de diseño.

---

**Cuadernillo de Práctica Pre-parcial**

Materia: Gestión de Datos — Práctica integradora (Análisis ⇄ MER ⇄ Lógico ⇄ Físico)  
UoD base: ElectroHogar (sin facturación)

**Instrucciones**

* Marcá tu respuesta en cada ítem siguiendo la consigna: (una opción) o (varias opciones).

* Tiempo sugerido: 45–60 minutos.

**Contexto de referencia (se usa en varios ítems)**

MER (Chen) — ElectroHogar (sin facturación)

* Cliente 1—N Pedido (participación total en Pedido)

* Pedido 1—N PedidoÍtem (total en PedidoÍtem)

* Producto 1—N PedidoÍtem (total en PedidoÍtem)

* Categoría 1—N Producto (cada Producto en una sola Categoría)

* Teléfono se modela como entidad débil de Cliente cuando es multivaluado (en este cuadernillo).

Modelo Lógico (resumen)

* CLIENTE(id PK, …)

* PEDIDO(id PK, cliente\_id FK→CLIENTE.id, …)

* CATEGORIA(id PK, nombre UNIQUE, …)

* PRODUCTO(id PK, nombre, categoria\_id FK NOT NULL→CATEGORIA.id, precio CHECK precio≥0)

* PEDIDO\_ITEM(PK compuesta (pedido\_id, producto\_id), cantidad\>0, FKs a PEDIDO y PRODUCTO)

* TELEFONO(PK compuesta (cliente\_id, numero), FK a CLIENTE)

DDL de lectura (no escribir código; solo interpretar)

![TextoEl contenido generado por IA puede ser incorrecto.][image1]

**A. Historias / Requisitos narrativos → MER**

1. (varias opciones) HU: “Como cliente, quiero registrar mis pedidos para recibir productos.”  
   \[ \] cliente \= Entidad \[ \] pedidos \= Entidad/Relación \[ \] productos \= Entidad \[ \] recibir \= Relación \[ \] domicilio \= Atributo (si aparece)

2. (una opción) “Cada producto pertenece a una categoría.”  
   \[ \] 1:1 \[ \] 1:N (Categoría→Producto) \[ \] N:M \[ \] multivaluado

**B. Cardinalidades y tipos de relación**

3. (una opción) “Un Cliente puede tener muchos Pedidos; un Pedido tiene exactamente un Cliente.”  
   \[ \] 1:1 \[ \] 1:N \[ \] N:M \[ \] multivaluado

4. (una opción) “Cada Pedido debe tener al menos un Ítem.”  
   \[ \] 0:1 \[ \] 1:1 \[ \] 0:N \[ \] 1:N

5. (una opción) Relación “Empleado supervisa a Empleado (0..1 supervisor por empleado)”:  
   \[ \] Binaria 1:N \[ \] Unaria (recursiva) 1:N \[ \] Binaria N:M \[ \] Unaria 1:1

6. (V/F) “Una relación ‘Cliente recomienda Cliente’ con 0..N recomendaciones es un caso unario.”  
   \[ \] Verdadero \[ \] Falso

**C. Atributos (simple, compuesto, multivaluado, derivado)**

7. (una opción) En Cliente, “teléfonos” con varios números y “tipo” por número:  
   \[ \] Atributo simple \[ \] Atributo compuesto \[ \] Atributo multivaluado \[ \] Relación recursiva

8. (una opción) En Cliente, “dirección” con calle, número, ciudad, CP:  
   \[ \] Atributo simple \[ \] Atributo compuesto \[ \] Atributo multivaluado \[ \] Atributo derivado

9. (varias opciones) ¿Cuándo conviene pasar de atributo multivaluado “teléfonos” a entidad/tabla TELEFONO?  
   \[ \] Hay metadatos por teléfono (tipo, preferido)  
   \[ \] Se requiere histórico/cambios por número  
   \[ \] Siempre habrá 1 teléfono exacto  
   \[ \] Validaciones distintas por tipo

10. (una opción) En el Lógico, un multivaluado resuelto se ve como:  
    \[ \] Columna repetida en la misma tabla  
    \[ \] Tabla relacionada 1:N con la entidad principal  
    \[ \] Un CHECK  
    \[ \] Una vista

11. (una opción) “Edad del Cliente” (desde fecha\_nacimiento) debe:  
    \[ \] Guardarse como columna obligatoria del Lógico  
    \[ \] Marcarse como derivado en MER y calcularse en Físico/consulta  
    \[ \] No existir en ningún modelo  
    \[ \] Ser PK

12. (V/F) “Un atributo derivado puede marcarse en MER; en Lógico no se persiste como columna necesaria; en Físico puede calcularse (vista/columna generada/consulta).”  
    \[ \] Verdadero \[ \] Falso

**D. Teléfonos como entidad débil (multivaluado)**

13. (una opción) En ElectroHogar, Cliente con 0..N teléfonos no compartidos entre clientes. ¿Cómo modelar “Teléfono”?  
    \[ \] Atributo multivaluado en CLIENTE  
    \[ \] Entidad débil TELEFONO dependiente de CLIENTE  
    \[ \] Entidad fuerte TELEFONO \+ N:M  
    \[ \] Columna “telefonos” VARCHAR

14. (una opción) PK más apropiada para TELEFONO (entidad débil):  
    \[ \] telefono\_id (surrogada)  
    \[ \] (cliente\_id, numero)  
    \[ \] (numero)  
    \[ \] (cliente\_id, tipo)

15. (varias opciones) Señales de entidad débil:  
    \[ \] Identidad depende de CLIENTE  
    \[ \] Participación total en relación con CLIENTE  
    \[ \] Número se reutiliza entre clientes  
    \[ \] Ciclo de vida completamente independiente

16. (una opción) FK correcta en el Lógico para TELEFONO (entidad débil):  
    \[ \] cliente.id → telefono.cliente\_id  
    \[ \] telefono.cliente\_id → cliente.id  
    \[ \] telefono.numero → cliente.id  
    \[ \] cliente.telefono\_id → telefono.id

17. (V/F) “Si Teléfono es entidad débil, la relación con Cliente es identificadora.”  
    \[ \] Verdadero \[ \] Falso

**E. Claves (naturales, surrogadas, candidatas, alternativas, PK, FK)**

18. (varias opciones) Ejemplos de clave natural:  
    \[ \] DNI (si la org. lo usa como identificador)  
    \[ \] Correo institucional único  
    \[ \] id autoincremental

19. (una opción) Clave surrogada es:  
    \[ \] Identificador que surge del negocio  
    \[ \] Identificador sintético sin significado de negocio  
    \[ \] Columna única alternativa  
    \[ \] Combinación de columnas del negocio

20. (varias opciones) Son claves candidatas de CLIENTE:  
    \[ \] (email) \[ \] (dni) \[ \] (id surrogada) \[ \] (cuil)

21. (una opción) La clave primaria es:  
    \[ \] Una candidata elegida como identificador principal  
    \[ \] Siempre la más larga  
    \[ \] Siempre surrogada  
    \[ \] La foránea más usada

22. (una opción) Clave alternativa/secundaria es:  
    \[ \] Una FK principal  
    \[ \] Una candidata no elegida como PK  
    \[ \] Un índice no único  
    \[ \] Un atributo derivado

23. (una opción) En PEDIDO\_ITEM (intersección), ¿qué PK evita duplicados?  
    \[ \] id surrogado  
    \[ \] (pedido\_id, producto\_id)  
    \[ \] (producto\_id)  
    \[ \] (pedido\_id)

24. (varias opciones) Buenos criterios para elegir PK:  
    \[ \] Única \[ \] Corta \[ \] Estable (no cambiante) \[ \] Sensible (datos personales)

25. (una opción) ¿Mala elección de PK para CLIENTE (privacidad/estabilidad)?  
    \[ \] id (surrogada)  
    \[ \] email  
    \[ \] id UUID  
    \[ \] id numérico

26. (una opción) La FK que enlaza PEDIDO con CLIENTE está en:  
    \[ \] CLIENTE  
    \[ \] PEDIDO (cliente\_id)  
    \[ \] PRODUCTO  
    \[ \] PEDIDO\_ITEM

27. (V/F) Una PK compuesta puede ser adecuada si la unicidad surge de dos columnas del negocio (p. ej., (pedido\_id, producto\_id)).  
    \[ \] Verdadero \[ \] Falso

**F. Lectura de restricciones en Físico (sin escribir código)**

28. (varias opciones) Según el DDL de PRODUCTO, es verdadero que:  
    \[ \] No se permite precio negativo  
    \[ \] Se puede borrar una Categoría con Productos  
    \[ \] Dos Productos pueden repetir nombre si son de distinta Categoría  
    \[ \] categoria\_id puede ser NULL  
    \[ \] Al cambiar el id de CATEGORIA, se actualiza producto.categoria\_id

**G. Dónde controlar (capa principal)**

Todas de opción única. Elegí la capa principal donde corresponde controlar cada regla.

29. (una opción) “Pedido debe tener al menos un Ítem.”  
    \[ \] Conceptual (MER) \[ \] Lógico (Relacional) \[ \] Físico (DDL/Constraints)

30. (una opción) “Producto pertenece a una única Categoría.”  
    \[ \] Conceptual (MER) \[ \] Lógico (Relacional) \[ \] Físico (DDL/Constraints)

31. (una opción) “Precio de Producto ≥ 0.”  
    \[ \] Conceptual (MER) \[ \] Lógico (Relacional) \[ \] Físico (DDL/Constraints)

32. (una opción) “No se puede eliminar un Cliente que tenga Pedidos.”  
    \[ \] Conceptual (MER) \[ \] Lógico (Relacional) \[ \] Físico (DDL/Constraints)

**H. UoD comparados (para ver que no todo se modela igual)**

33. (una opción) Retail (ElectroHogar): teléfonos de Cliente (0..N), con “tipo” y “preferido”. En la materia solo vimos teléfonos como multivaluado modelado como entidad débil. Mejor diseño:  
    \[ \] Atributo multivaluado en CLIENTE  
    \[ \] Entidad débil TELEFONO dependiente de CLIENTE (PK compuesta, por ej., (cliente\_id, numero))  
    \[ \] Entidad fuerte \+ N:M  
    \[ \] Columna “telefonos” VARCHAR

34. (una opción) Veterinaria: Mascota con varias Vacunas en distintas fechas; Vacuna aplicada a muchas Mascotas.  
    \[ \] 1:N Mascota–Vacuna  
    \[ \] N:M con tabla puente (fecha, dosis…)  
    \[ \] Atributo multivaluado “vacunas” en Mascota  
    \[ \] Columna “vacunas” VARCHAR

35. (una opción) Marketplace: un Producto puede ser ofrecido por varios Vendedores; un Vendedor ofrece muchos Productos. Mejor diseño:  
    \[ \] 1:N Vendedor–Producto  
    \[ \] N:M con tabla puente PUBLICACIÓN (campos propios como precio)  
    \[ \] Atributo multivaluado “vendedores” en Producto  
    \[ \] No se modela

[image1]: <data:image/png;base64,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>