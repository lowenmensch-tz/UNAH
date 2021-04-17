@author jose.inestroza@unah.edu.hn
@version 0.1.0
@date 2021/04/16

0701-BASE DE DATOS I
Examen 3 Digital

Examen #3 Práctico - Unidad 2
Lea primero 

    Entre más enriquecidas sean sus respuestas, usted obtendrá una mejor calificación.

    No se confíe de los comentarios que escuchó o de afirmaciones que nunca probó. Muchos comentarios en clase se complementaron con “excelente, pruebe lo que indica su compañero” ya que dichos comentarios podrían tener algo de “correctitud” pero al mismo tiempo podrían no entregar el resultado esperado. Sin haberlo probado usted por su cuenta, arrastrará omisiones en la implementación de código. 

    Haga uso del 100% del conocimiento exclusivo de la Unidad 2 de esta asignatura (contenido como procedimientos almacenados, triggers, expresiones regulares, entre muchos muchos otros). 

    El SGBD de examen es idéntico al usado en clase. 

    Es obligatorio el aliasing en el DML y DDL.

    Mantenga sus clases (imports) separadas de su main de Jupyter.

    Para asegurar una buena revisión haga su código sumamente ordenado, implementando TABULADOS y SALTOS DE LÍNEA en su Python y SQL.

    El examen es a libro abierto. Hay ejercicios que usan código de clase, por lo que el mal uso de dicho código implica un ejercicio incorrecto (ya que el código no es creado por el estudiante sino copiado y modificado desde las evidencias de clase).


Enunciado de Examen

Objetivo

Se desea hacer una hoja de demostración de Jupyter Notebook con el código, la documentación, las clases, las instancias y el uso de las instancias para un sistema que abarque los componentes de construcción de tablas, llenado de datos y análisis de los datos, usando los contenidos de la Unidad 2 de la asignatura de BDI. Su entregable será un archivo .7z con todos los archivos necesarios.

Ejercicio

Haga un programa de Python que posea sus respectivas clases/objetos, consultas SQL e instancias para la generación de una conexión y uso de múltiples transacciones de SQL dentro de un SGBD MySQL/MariaDB que resuelvan el siguiente problema, tal y como se han ejecutado ejercicios en clase mediante Python3.

Para hacer este programa Python con acceso a base de datos, los diseñadores del sistema han establecido una serie de elementos que el programador debe traducir a código y documentación, los cuales se listan a continuación. 

En sus clases de Python (los archivos .py que viven afuera del archivo de Jupyter Main) deben de actualizarse los siguientes elementos. Estos archivos .py serán importados desde su Jupyter Main tal y como fue hecho en clase (10%).

    Debe existir un método select() el cual debe recibir la query, junto con un arreglo con el encabezado de la tabla a seleccionar, y junto con el máximo límite de resultados a imprimir. Este método ya debe imprimir el resultado directamente en pantalla, en lugar de retornarlo. Este método debe ir contando internamente cuántas ejecuciones select posee su programa, mediante una variable local a la clase.

    Debe existir un método dms() el cual debe servir para ejecutar exclusivamente instrucciones dms no fetch. Este método debe ir contando internamente cuántas ejecuciones dms posee su programa, mediante una variable local a la clase.

    Debe existir un método dds() el cual debe servir para ejecutar exclusivamente instrucciones dds no fetch. Este método debe ir contando internamente cuántas ejecuciones dds posee su programa, mediante una variable local a la clase.

    Usted creará los métodos necesarios para resolver el problema a continuación, reutilizando los tres elementos anteriores.

Cada elemento de la lista siguiente debe de estar compuesto de su respectivo código de Python y SQL, junto con la ejecución del método de la instancia. Su entregable debe ser un archivo .7z el cual debe contener un JupyterMain de Jupyter Notebook, junto con todos los archivos .py que use su main. Debe usar la misma nomenclatura enseñada por su profesor en clase, indicando así que el 100% de su examen fue generado por usted, quien conoce dicha nomenclatura (código python, queries SQL, comentarios markdown, respuestas, etc).

Su archivo principal de Jupyter Notebook debe contener:

- Instancia de conexión con la base de datos.
- Un mecanismo dentro de la instancia que permita la creación de las tablas de base de datos de "Red Social" sobre una base de datos llamada "Quiz". Su programa Python también debe crear la base de datos. El diseño debe permitir (30%):

  - Que cualquier usuario pueda mandar un mensaje público a la red.

  - Cada mensaje puede contener cualquier tipo de contenido web.

  - Cualquier usuario puede comentar en un mensaje público mediante otro mensaje. Los usuarios deben ser identificables, no pueden haber usuarios anónimos.

  - Cada vez que se envía un mensaje, debe existir un lugar donde se guarde inmediatamente una notificación de la nueva publicación. Estas notificaciones las puede ver cualquier usuario.

  - Cada vez que un usuario comenta un mensaje, debe existir un lugar donde se le notifique al usuario específico, que alguien le ha enviado un comentario a su mensaje. Se debe saber quién ha comentado y cuál es su comentario.

  - También es posible dar me gusta a cualquier mensaje.

- En Python "Imports" debe existir un método para cada una de las siguientes transacciones (60%). El estudiante deberá identificar qué parámetros necesita para resolver cada mecanismo. Cualquier otro requerimiento que se necesite debe ser creado por el estudiante. 

  - El administrador quiere saber cuáles son los usuarios que han enviado más mensajes en toda la plataforma. Deben aparecer máximo X cantidad de usuarios, con el que tiene más mensajes de primero, y solo pueden aparecer usuarios que han enviado mínimo Z cantidad de  mensajes.

  - El administrador quiere saber cuáles son los usuarios que han comentado mensajes en toda la plataforma. Deben aparecer máximo X cantidad de usuarios, con el que tiene más comentarios de primero, y solo pueden aparecer usuarios que han enviado mínimo Z cantidad de  comentarios.

  - El administrador quiere saber cuáles son los usuarios que han obtenido más "me gusta". Deben aparecer máximo X cantidad de usuarios, con el que tiene más "me gusta" de primero, y solo pueden aparecer usuarios que han enviado mínimo Z cantidad de "me gusta".

  - Crear un mensaje.

  - Comentar un mensaje.

  - Entregar "me gusta" a cualquier mensaje.

  - Actualizar un mensaje cualquiera y marcarlo como editado.

  - Un mecanismo que permita borrar un comentario (si este no tiene "me gusta").

  - Contar la cantidad de mensajes de un usuario para un rango de fechas.

  - Contar la cantidad de mensajes de un usuario.

  - Imprimir la cantidad de selects ejecutados por el sistema.

  - Imprimir la cantidad de dds ejecutados por el sistema.

  - Imprimir la cantidad de dms ejecutados por el sistema.
