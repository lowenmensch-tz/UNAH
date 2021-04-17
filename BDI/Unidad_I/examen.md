@author jose.inestroza@unah.edu.hn
@version 0.1.0
@date 2021/03/19

### 0701-BASE DE DATOS I
### Examen 1 Práctico


# Examen #1 Práctico Unidad 1

El examen a continuación se compone de un enunciado que corresponde con el 100% de la calificación.
Lea primero 

- Entre más enriquecidas sean sus respuestas, usted obtendrá una mejor calificación. El ejercicio le ofrece un escenario y le entrega información obligatoria a obtener, sin embargo, se espera que usted complete dicha información mediante la abstracción de la vida real.

- No se confíe de los comentarios que escuchó o de afirmaciones que nunca probó. Muchos comentarios en clase se complementaron con “excelente, pruebe lo que indica su compañero” ya que dichos comentarios podrían tener algo de “correctitud” pero al mismo tiempo podrían no entregar el resultado esperado. Sin haberlo probado usted por su cuenta, arrastrará omisiones en la implementación de código. 

- Haga uso del 100% del conocimiento exclusivo de la Unidad 1 de esta asignatura (no se aceptará otro contenido como procedimientos almacenados, triggers, UDF, expresiones regulares, entre muchos muchos otros no son parte de la unidad 1 de BDI). 

- El SGBD de examen es idéntico al usado en clase. 

- Es obligatorio el aliasing en el DML y los comments en el DDL.

- No se aceptará plagio. Esto aplica en todo sentido.

    Para asegurar una buena revisión haga su código claro, implementando TABULADOS y SALTOS DE LÍNEA en su escritura a mano en su SQL. Ejemplo:

```SQL
SELECT

      FIELD,

      FIELD,

      FIELD,...

FROM 

      TABLE EXPRESSION

JOIN

      TABLE EXPRESSION

...

      ...

GROUP BY

      ...

ORDER BY

      ...

;
```

## Enunciado de Examen

Una empresa de desarrollo lo está contratando para implementar un catálogo de histórico de celulares android, donde se desea almacenar toda la información de los dispositivos y sus accesorios, para todas las marcas en inventario. Eventualmente los desarrolladores de una plataforma Web permitirán que los usuarios hagan búsquedas de la información resguardada en este sistema por lo que será necesario crear una tabla que lleve un registro de todas las búsquedas realizadas en el sistema. Al continuar con la lectura de este texto el estudiante/desarrollador aprenderá más información sobre el problema.

Ejercicio 1 (30 puntos): Haga el diagrama ER y modelado UML que resuelve el problema planteado. Siga leyendo para tener más contexto.

Ejercicio 2 (40 puntos): Haga el SQL de creación de la base de datos en 2.5 NF. Este SQL debe coincidir con el ejercicio #1 junto con todas sus restricciones de integridad referencial y buenas prácticas. Siga leyendo para tener más contexto.

Ejercicio 3 (30 puntos):  Haga las instrucciones SQL que permitan resolver los siguientes escenarios.

- Muchos clientes o entusiastas que entrarán en el sistema en línea, estarán interesados en conocer sobre todo el histórico de dispositivos, buscando aquellos ejemplares que coincidan con alguna versión o marca de procesador; marca de vidrio templado de pantalla; resolución, ratio, brillo y tecnología de pantalla;puertos disponibles; parlantes y tecnología de audio; tipos de botones físicos; manual del celular; fotografías de ejemplar del celular; información de sus cámaras; información de sus micrófonos. Por tanto, esta instrucción SQL deberá: mostrar todos los dispositivos coincidan con el tamaño de palabra de sistema operativo, donde la lista muestra 50 dispositivos a la vez, ordenados ascendentemente por el año de lanzamiento, incluyendo obligatoriamente: la marca, el modelo, el fabricante, un enlace al manual del dispositivo, un enlace al sitio web oficial, una imagen de ejemplar del dispositivo, junto con otros campos de su preferencia. En total debe mostrar 10 atributos relevantes por lo que usted debe pensar cuáles serán los campos restantes a mostrar.

- Las empresas lanzadoras de dispositivos usualmente desarrollan una gran cantidad de ejemplares para distintos países y continentes. Por tanto, esta instrucción de SQL deberá: mostrar los datos del publicador del dispositivo (que deben ser al menos 7 atributos relevantes), donde en la misma tupla se incluye adicionalmente a los campos anteriores, la cantidad de modelos celulares de este fabricante con respecto a los siguientes países: JP, USA, HN, ESP, ENG, MEX. 

- Esta instrucción SQL deberá: mostrar el listado del ejercicio anterior para un fabricante específico, ordenando los resultados por fecha de publicación con modelos publicados para todos los países registrados en la plataforma.

- La empresa creadora de la plataforma está interesada en visualizar la cantidad de búsquedas que realizan los usuarios. Esta instrucción SQL deberá: mostrar las búsquedas agrupadas por hora del día, por cada día y por cada modelo de cada marca a la cual se le ha hecho un click por parte del usuario final.
