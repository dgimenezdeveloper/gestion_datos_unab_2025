# Resumen — Unidad 1: Bases de datos y usuarios de bases de datos

Este documento contiene un resumen conciso y estructurado del Capítulo 1 (Fundamentos de Bases de Datos) para estudiar para un parcial. Incluye definiciones clave, ejemplos, características, actores, capacidades de un DBMS, historia breve, cuándo no usar un DBMS, preguntas de repaso y recomendaciones sobre imágenes a incluir.

## Resumen ejecutivo
- Las bases de datos son colecciones de datos relacionados que representan un aspecto del mundo real (mini-mundo o UoD).
- Un DBMS (Database Management System) es el software que permite definir, construir, manipular y compartir una base de datos. Base de datos + DBMS = sistema de bases de datos.
- Las bases de datos son críticas en muchas aplicaciones: banca, comercio electrónico, bibliotecas, GIS, multimedia, OLAP, sistemas en tiempo real, etc.

## Definiciones clave
- Datos: hechos grabados con significado implícito.
- Base de datos: colección de datos relacionados, coherente y diseñada con un propósito y usuarios específicos.
- DBMS: conjunto de programas que facilita definición (metadatos), construcción, manipulación y protección de la base de datos.
- Catálogo / Diccionario de datos: metadatos que describen la base de datos.
- Transacción: programa o proceso que lee y/o escribe en la base de datos (véase propiedades de transacción).

## Propiedades implícitas de una base de datos
- Representa el mini-mundo; los cambios del minimundo deben reflejarse en la BD.
- Cohesión lógica y significado inherente (no datos aleatorios).
- Diseñada para usuarios y aplicaciones concretas; debe mantenerse precisa y actualizada.

## Ejemplo ilustrativo: BD `UNIVERSIDAD`
- Archivos/tabla principales: ESTUDIANTE, CURSO, SECCIÓN, INFORME_CALIF, PRERREQUISITO.
- Estructura: cada registro tiene elementos de datos con tipos (p. ej., NumEstudiante entero, Nota ∈ {A,B,C,D,F,I}).
- Consultas típicas: certificado de un estudiante, listado de alumnos y notas de una sección, prerrequisitos de un curso.
- Actualizaciones típicas: cambio de clase de un estudiante, crear sección nueva, introducir una nota.

## Características que distinguen la metodología BD del procesamiento por archivos
- Integración y reducción de redundancia controlada.
- Soporte multiusuario y control de concurrencia.
- Independencia entre programas y datos (niveles de abstracción: físico, lógico/conceptual, vista de usuario).
- Definición y aplicación centralizada de reglas y estándares.

## Capacidades que debe ofrecer un DBMS (resumen)
- Definición de datos y metadatos (catálogo).
- Construcción y almacenamiento persistente de datos.
- Manipulación: consultas, actualizaciones y generación de informes.
- Control de concurrencia y procesamiento de transacciones multiusuario (propiedades: atomicidad, aislamiento; también consistencia y durabilidad en práctica).
- Seguridad y autorización (control de accesos y privilegios).
- Copia de seguridad y recuperación ante fallos.
- Optimización y estructuras de almacenamiento (índices, búferes, planes de consulta).
- Soporte de múltiples interfaces (lenguajes de consulta, APIs, GUIs, formularios web).
- Soporte de integridad y reglas de negocio (restricciones, triggers, procedimientos almacenados, reglas deductivas en DB deductivos).
- Almacenamiento persistente de objetos (en OODB y sistemas objeto-relacionales) para evitar la incompatibilidad de impedancia.

## Actores principales y responsabilidades
- DBA (Database Administrator): administrar acceso, recursos, seguridad, rendimiento y mantenimiento.
- Diseñadores de BD: identificar datos, modelar estructuras, elaborar vistas y diseñar el esquema conceptual y lógico.
- Usuarios finales:
  - Casuales: consultas puntuales con lenguaje de consulta.
  - Paramétricos / principiantes: usan transacciones enlatadas (cajeros, agentes de viajes, formularios).
  - Sofisticados: ingenieros, analistas, que desarrollan consultas complejas y aplicaciones.
  - Independientes: usuarios de paquetes para BD personales.

## Ventajas de usar un DBMS (principales)
- Tiempo de desarrollo reducido para nuevas aplicaciones.
- Flexibilidad ante cambios en requisitos.
- Disponibilidad de información actualizada (multiusuario/OLTP).
- Economías de escala (consolidación de datos y recursos).
- Implementación de estándares y control centralizado.

## Límites y cuándo no usar un DBMS
- Coste inicial alto (hardware, software, formación).
- Sobrecoste por funcionalidades generales (seguridad, concurrencia, recuperación).
- Cuando la aplicación es muy simple, bien definida y no evolucionará.
- Requisitos de tiempo real muy estrictos que no toleran la sobrecarga de un DBMS.
- Ausencia de necesidad de acceso multiusuario.
- Aplicaciones muy especializadas que usan formatos/protocolos propietarios (p. ej., CAD, ciertos GIS, conmutación telefónica).

## Breve historia (puntos clave)
- Primeros sistemas (1960–1980): jerárquicos, en red; mezclaban almacenamiento físico y representación conceptual.
- Surgimiento del modelo relacional: separación concepto/almacenamiento y lenguajes de consulta de alto nivel (1970s–1980s).
- OODB y objetos-relacionales (1980s–): para objetos complejos y persistencia; penetración parcial.
- Web y e‑commerce: integración BD ↔ web, XML para intercambio de datos.
- Extensiones modernas: multimedia, series temporales, OLAP, minado de datos, GIS.

## Integridad y control de redundancia
- Controlada: redundancia deliberada para rendimiento o disponibilidad, gestionada por diseño.
- Descontrolada: redundancia accidental que provoca inconsistencias (ej.: registros incoherentes entre tablas).
- Restricciones de integridad: tipos de datos, unicidad, referencias entre registros (FK conceptuales), reglas de negocio. Algunas se implementan en el DBMS; otras en procesos de actualización.

## Reglas, inferencia y acciones
- Triggers: reglas que se ejecutan en actualizaciones.
- Procedimientos almacenados: lógica reutilizable en la BD.
- Sistemas deductivos: permiten definir reglas declarativas para inferir nueva información.

## Preguntas de repaso (selección importante para parcial)
1. Defina: datos, base de datos, DBMS, sistema de bases de datos, catálogo, independencia programa-datos, vista de usuario, DBA, usuario final, transacción enlatada, objeto persistente, metadatos.
2. Qué acciones implican bases de datos (recuperación/consulta, actualización, definición y control/administración) — explique cada una.
3. Señale las diferencias principales entre metodología BD y procesamiento por archivos.
4. Responsabilidades del DBA vs. diseñadores de BD.
5. Tipos de usuarios y actividades principales.
6. Capacidades que un DBMS debe proporcionar (listarlas y explicar brevemente).
7. Diferencias entre sistemas de bases de datos y recuperación de información (IR).

## Ejercicios sugeridos (práctica para parcial)
- Redacta 5 consultas y 3 actualizaciones informales para la BD `UNIVERSIDAD`.
- Identifica posibles restricciones de integridad en `UNIVERSIDAD` y cómo implementarlas en un DBMS.
- Dibuja las vistas solicitadas en la Sección de vistas (certificado, prerrequisitos) y escribe la consulta SQL aproximada para cada una.
- Explica con ejemplos la diferencia entre redundancia controlada y descontrolada.

## Consejos de estudio rápidos
- Aprende y define claramente los términos clave (pueden preguntarte definiciones literales).
- Memoriza las propiedades de transacción (atomicidad, aislamiento, coherencia/consistencia y durabilidad) y su significado.
- Practica preguntas tipo: diseñar vistas, identificar restricciones, proponer índices, y casos de concurrencia.
- Repasa el ejemplo `UNIVERSIDAD` y asegúrate de poder explicar relaciones entre tablas.

## Imágenes recomendadas y dónde pegarlas
Coloca las imágenes recortadas del PDF en `unidad-01/images/` con los nombres sugeridos y luego inserta las rutas correspondientes en este archivo si lo deseas. Extrae las figuras del Capítulo 1 del PDF adjunto (busca las leyendas "Figura 1.1", "Figura 1.2", "Figura 1.5", "Figura 1.6").

- `unidad-01/images/fig1_1_entorno.png` — Figura 1.1: Entorno simplificado de un sistema de bases de datos (colocar al inicio del resumen, sección Definiciones clave).
- `unidad-01/images/fig1_2_universidad.png` — Figura 1.2: Esquema y ejemplo de la BD `UNIVERSIDAD` (sección Ejemplo ilustrativo).
- `unidad-01/images/fig1_5_vistas.png` — Figura 1.5: Vistas (certificado y prerrequisitos) (sección Vistas / ejemplos de consultas).
- `unidad-01/images/fig1_6_integridad.png` — Figura 1.6: Ejemplo de coherencia/incoherencia entre archivos (sección Integridad).

Instrucciones para extraer imágenes del PDF:
1. Abre el PDF y localiza las leyendas "Figura 1.1", "Figura 1.2", "Figura 1.5" y "Figura 1.6".
2. Recorta cada figura (con herramienta de captura o exportando página a PNG) y guarda con los nombres indicados en `unidad-01/images/`.
3. Si quieres, dime y puedo extraer las imágenes por ti (necesitaría permiso para procesar el PDF en la sesión).

## Archivo y uso
- Archivo creado: `unidad-01/Resumen_Unidad_1.md` (esta ruta). Puedes abrirlo en tu editor o exportarlo a PDF para estudiar.

---
Si quieres, hago lo siguiente ahora:
- [ ] Extraer las figuras del PDF y guardarlas en `unidad-01/images/`.
- [ ] Insertar imágenes en este markdown con rutas relativas.
- [ ] Generar una versión en PDF del resumen lista para imprimir.

Indícame qué de esto quieres que haga a continuación.
