# Caso Guía: Tienda de Ventas - Unidad 1, Semana 1

## 1. Revisión y explicación de los temas tratados

### Contexto y problema
Una tienda minorista de artículos para el hogar necesita centralizar el registro de clientes y sus datos de contacto. Actualmente, la información está dispersa en papeles y planillas, lo que genera duplicados, inconsistencias y dificulta la comunicación confiable con los clientes.

### Dolencias detectadas
- No existe un registro único de clientes.
- Los teléfonos están anotados en distintos lugares; algunos clientes tienen varios y otros ninguno.
- No se puede responder con certeza: “¿Cómo contactamos a este cliente?”

### Objetivo del primer ciclo
Construir una base sólida para registrar clientes y sus teléfonos (múltiples por cliente), y poder consultarlos de forma simple. El trabajo se enfoca en una sola entidad de negocio: Cliente.

### Alcance del primer ciclo
- Registrar clientes con datos básicos (nombre, documento opcional, correo opcional).
- Almacenar uno o más teléfonos por cliente (móvil/fijo), cada uno con su número y tipo.
- Permitir consultas básicas de clientes por nombre, documento, teléfono o correo.

#### Fuera de alcance (por ahora)
- Ventas, pedidos, ítems de venta, precios y productos.
- Gestión de stock, proveedores y promociones.
- Histórico de cambios de teléfono o auditoría de contacto.
- Dirección postal compuesta y georreferenciación.

### Reglas de negocio mínimas
- Cada cliente posee un identificador único (id_cliente) generado por el sistema.
- Un cliente puede tener uno o más teléfonos; el número no se repite para el mismo cliente.
- Cada teléfono tiene tipo (móvil/fijo) y número con formato validado.
- Debe existir al menos un dato de contacto (teléfono o correo) para considerar al cliente “contactable”.

### Conceptos clave
- **Entidad:** Objeto de negocio que queremos registrar (Cliente).
- **Atributo:** Propiedad simple de una entidad (nombre, documento, correo).
- **Atributo multivaluado:** Puede tener más de un valor por entidad (teléfono).
- **Teléfono multivaluado:** Requiere tabla propia en el modelo lógico.

### Decisiones de diseño
- Teléfono se modela como atributo multivaluado (0..n por cliente), por lo que en el modelo lógico se usará una tabla aparte.
- Convenciones de nombres: singular, prefijos, legibilidad.

---

## 2. Documento de alcance

El sistema a modelar corresponde a la gestión de clientes para la "Tienda de Ventas". El objetivo es registrar información relevante de cada cliente para facilitar la administración y el contacto confiable. El universo de discurso incluye personas físicas y jurídicas que contratan servicios, y se busca almacenar datos que permitan identificar, contactar y segmentar a los clientes. El alcance del primer ciclo se limita a la entidad Cliente y sus teléfonos asociados.

---

## 3. Lista de atributos de la entidad Cliente

| Atributo      | Tipo           | Justificación                                                        |
|---------------|----------------|---------------------------------------------------------------------|
| id_cliente    | Clave primaria | Identificador único para cada cliente.                               |
| nombre        | Texto          | Permite identificar al cliente.                                      |
| documento     | Texto/Numérico | Opcional, útil para validaciones y trámites legales.                 |
| correo        | Texto          | Opcional, medio de contacto digital.                                 |
| telefono      | Multivaluado   | Permite registrar varios teléfonos por cliente (móvil/fijo, etc.).   |

---

## 4. Decisión sobre teléfono como atributo multivaluado

**Justificación:**
El atributo teléfono se define como multivaluado porque en el universo de discurso actual es común que un cliente posea más de un número de contacto (por ejemplo, teléfono fijo, celular, laboral, etc.). Esto permite una mayor flexibilidad y asegura que la empresa pueda contactar al cliente por diferentes vías según la situación. Además, evita la pérdida de información relevante y facilita la actualización de datos. En el modelo lógico, esto se implementará con una tabla aparte para los teléfonos asociados a cada cliente.

---

## 5. Resumen de acuerdos y convenciones
- El foco del ciclo es solo el cliente y su contacto.
- Teléfono no debe guardarse en una sola columna ni duplicar clientes para agregar teléfonos.
- Teléfono es multivaluado y requiere tabla propia.
- Convenciones de nombres: singular, prefijos, legibilidad.
- Alcance y exclusiones documentados para evitar crecimiento no planificado.

---

**Fin del entregable.**