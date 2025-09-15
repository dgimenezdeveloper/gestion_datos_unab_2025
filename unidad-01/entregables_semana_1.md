# Entregables Semana 1 - Unidad 1

## 1. Documento de alcance

El sistema a modelar corresponde a la gestión de clientes para una empresa de servicios. El objetivo es registrar información relevante de cada cliente para facilitar la administración, el contacto y la personalización de servicios. El universo de discurso incluye personas físicas y jurídicas que contratan servicios, y se busca almacenar datos que permitan identificar, contactar y segmentar a los clientes.

## 2. Lista de atributos de la entidad Cliente

| Atributo         | Tipo           | Justificación                                                                 |
|------------------|----------------|-------------------------------------------------------------------------------|
| id_cliente       | Clave primaria | Identificador único para cada cliente.                                        |
| nombre           | Texto          | Permite identificar al cliente (persona física o jurídica).                   |
| apellido         | Texto          | Necesario para personas físicas, ayuda en la identificación.                  |
| razon_social     | Texto          | Para personas jurídicas, identifica la empresa.                               |
| tipo_cliente     | Enumerado      | Diferencia entre persona física y jurídica.                                   |
| documento        | Texto/Numérico | DNI/CUIT/CUIL según tipo de cliente, para validación y trámites legales.      |
| direccion        | Texto          | Ubicación física del cliente, útil para envíos y visitas.                     |
| email            | Texto          | Medio de contacto digital, notificaciones y marketing.                        |
| telefono         | Multivaluado   | Permite registrar varios teléfonos por cliente (fijo, móvil, laboral, etc.).  |
| fecha_alta       | Fecha          | Control de antigüedad y segmentación.                                         |
| estado           | Enumerado      | Activo/Inactivo, para gestión operativa.                                      |
| observaciones    | Texto          | Campo libre para notas adicionales relevantes.                                |

## 3. Decisión sobre teléfono como atributo multivaluado

**Justificación:**  
El atributo teléfono se define como multivaluado porque en el universo de discurso actual es común que un cliente posea más de un número de contacto (por ejemplo, teléfono fijo, celular, laboral, etc.). Esto permite una mayor flexibilidad y asegura que la empresa pueda contactar al cliente por diferentes vías según la situación. Además, evita la pérdida de información relevante y facilita la actualización de datos.

## 4. Justificación de los atributos

- **id_cliente:** Clave primaria, necesaria para identificar de forma única a cada cliente en la base de datos.
- **nombre y apellido:** Permiten identificar a personas físicas; en el caso de personas jurídicas, se utiliza razón social.
- **razon_social:** Específico para empresas, fundamental para facturación y contratos.
- **tipo_cliente:** Permite distinguir entre personas físicas y jurídicas, lo que afecta otros atributos y procesos.
- **documento:** Esencial para validaciones legales y administrativas.
- **direccion:** Importante para logística, envíos y visitas comerciales.
- **email:** Medio de contacto digital, cada vez más relevante en la comunicación empresarial.
- **telefono:** Multivaluado por la diversidad de medios de contacto actuales.
- **fecha_alta:** Permite analizar la antigüedad y segmentar clientes.
- **estado:** Facilita la gestión operativa y el filtrado de clientes activos/inactivos.
- **observaciones:** Permite registrar información adicional que no encaja en los atributos anteriores.

---

**Fin del entregable.**