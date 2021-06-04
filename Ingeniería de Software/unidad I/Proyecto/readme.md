```
    @author: Kenneth Cruz
    @version 0.1.0    
    @date: 2021/06/03
```

# Configuración de Entorno: Django, MySQL 5.7, Python 3.8 en WSL (Windows Subsystem for Linux) 20.04 LTS

<br>

Este documento abarca la configuración del entorno necesario para la ejecución del proyecto correspondiente a la clase de **Ingeniería de Software (IS 802)**, este documento esta diseñado para solventar y eficientar el tiempo con respecto a problemas de configuración. Cabe resaltar que cierta nomenclatura no se trata a profundiad, sí desea expandir su conocimiento puede realizar una investigación propia.  

Se abarca la instalación del siguiente software:

- Python 3.8
- Django 3.2
- MySQL 5.7
- Windows 10
    - Ubuntu 20.04 LTS ([WSL](https://docs.microsoft.com/en-us/windows/wsl/))
    - Windows Terminal

WSL (Windows Subsystem for Linux) es una virtualización nativa de Ubuntu para Windows 10, funciona como máquina virtual optimizada, con la salvedad que utiliza el minímo de recursos y viene con algunas configuraciones por defecto (python, git, net-tools...).

Podemos utilizar [WSL](https://docs.microsoft.com/en-us/windows/wsl/) como una máquina virtual instalando programas de distinta índole (MySQL, MariaDB, Python, SQLite3...) sin afectar el sistema de archivos de Windows.  
Es decir, se puede ejecutar scripts de Python desde WSL sin la necesidad de instalar Python en Windows.

Se explota las capacidades y bondades de [WSL](https://docs.microsoft.com/en-us/windows/wsl/) (Windows Subsystem for Linux) por ser una máquina virtual nativa de Ubuntu en Windows 10, la mayoría de características han sido probadas antes de la realización de este documento.  

Algunas ventajas de realizar este proyecto con esta configuración
- MySQL tiene soporte con Workbench   
- Puede ejecutar el servidor de Django desde las instancias de [WSL](https://docs.microsoft.com/en-us/windows/wsl/) y visualizar esos resultados en un navegador desde Windows 10 (accediendo al localhost) 
- Bajo consumo de recursos
- Puede utilizar una terminal de Linux en Windows
- Puede crear varias instancias de una terminal a la vez (Powershell, CMD, Ubuntu, Azure)
- Los programas instalados en WSL no afectan de forma directa el sistema de archivos de Windows



## Índice

---

- [Configuración de Entorno: Django, MySQL 5.7, Python 3.8 en WSL (Windows Subsystem for Linux) 20.04 LTS](#configuración-de-entorno-django-mysql-57-python-38-en-wsl-windows-subsystem-for-linux-2004-lts)
  - [Índice](#índice)
  - [Visual Code](#visual-code)
  - [Configuración de WSL](#configuración-de-wsl)
  - [Configuración de MySQL 5.7](#configuración-de-mysql-57)
    - [Últimos pasos](#últimos-pasos)
    - [Creación de usuario admin](#creación-de-usuario-admin)
  - [Python y entornos virtuales](#python-y-entornos-virtuales)
    - [**Uso del entorno virtual**](#uso-del-entorno-virtual)
  - [Configuración de Django](#configuración-de-django)
    - [**Estructura de Archivos**](#estructura-de-archivos)
    - [Conexión: Dango con MySQL 5.7](#conexión-dango-con-mysql-57)

## Visual Code

---

**Pluggins a instalar.**  
No es necesario ni indispensables su instalación, sin embargo son una herramienta útil que ayuda en la productividad
- [**GitLens:**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) eamodio.gitlens
- [**ErrorLens:**](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) usernamehw.errorlens
- [**Django:**](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) batisteo.vscode-django
- [**Markdown All in One:**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) yzhang.markdown-all-in-one

Para instalar estos plugins en Visual Code es necesario copiar y pegar el id en la sección `Extensions` del editor de texto.

![images/Screenshot_(206).png](images/Screenshot_(206).png)

## Configuración de WSL

---

Para configurar [WSL](https://docs.microsoft.com/en-us/windows/wsl/) en Windows 10, debe hacer lo siguiente: 

Ir a la tienda de Microsoft y escribir **Ubuntu 20.04 LST**; clic en Launch

![images/Screenshot_(214).png](images/Screenshot_(214).png)

Buscar el programa en su máquina; escriba **ubuntu 20.04 LTS**

Aparece una terminal, la Shell de Linux. 

Puede aparecer un mensaje similar al siguiente:

![https://i.stack.imgur.com/pQPhx.png](https://i.stack.imgur.com/pQPhx.png)

Debe activar hyper-v y otras características que Windows 10 no trae activas por defecto.

Para activar el entorno debe seguir este tutorial: 

- [Activar la terminal](https://medium.com/@rodritorrico/tutorial-como-activar-la-terminal-de-linux-en-windows-10-beta-52769b5cab7e)

Una vez hecho esto, debe buscar e instalar en la tienda de Microsoft: **Windows Terminal**  

![images/Screenshot_(220).png](images/Screenshot_(220).png)

Busque y ejecute **Windows Terminal** en su computadora 

![images/Screenshot_(222).png](images/Screenshot_(222).png)

Esta es la nueva terminal mejorada de Windows.

La ventaja es la integración que mantiene con otras líneas de comando 

![images/Screenshot_(223).png](images/Screenshot_(223).png)

![images/Screenshot_(224).png](images/Screenshot_(224).png)

## Configuración de MySQL 5.7

---

Se enumera la configuración siguiente para la instalación de MySQL:  

```bash
#Actualización del sistema de paquetes
$ sudo apt update

#Instalación de wget
$ sudo apt install wget

#Obtener el paquete que incluye diferentes versiones de MySQL 
$ wget http://repo.mysql.com/mysql-apt-config_0.8.10-1_all.deb
```

*Anotaciones*:

- **wget** es una herramienta que permite la descarga de contenidos desde servidores web

Instalación del paquete por medio del comando **dpkg**

```bash
$ sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb
$ sudo dpkg-reconfigure mysql-apt-config

#Actualizamos el sistema de paquete
$ sudo apt update
```

Al desempaquetar y configurar el paquete verá una ventana similar a la siguiente: 

![images/Screenshot_(199).png](images/Screenshot_(199).png)

*Recuerde debe seleccionar mysql-5.7*

Puede seleccionar esta versión, al seleccionar la primera opción de la lista (ENTER), luego de ello aparece la versión requerida, seleccione y continue . 

Al momento de tener los settings completado, debe dar ENTER a la opción **<Ok>**

![images/Screenshot_(202).png](images/Screenshot_(202).png)

Anotar la versión más reciente que se encuentre en el sistema de paquetes

```bash
$ sudo apt-cache policy mysql-server
```

Al ejecutar el comando anterior se visuliza un mensaje similar al siguiente: 

![images/Screenshot_(201).png](images/Screenshot_(201).png)

La versión resaltada en color gris, es la última disponible para este caso:

**<5.7.34-1ubuntu18.04>**

**Una vez desempaquetado los binarios, pasamos a la siguiente fase**

Instalación de las instancias del Servidor 

```bash
$ sudo apt install -f mysql-client=5.7.34-1ubuntu18.04

#En este paso pedirá configurar la contraseña del root
#NO OLVIDE EL PASSWORD INGRESADO
$ sudo apt install -f mysql-community-server=5.7.34-1ubuntu18.04

$ sudo apt install -f mysql-server=5.7.34-1ubuntu18.04
```

![images/Screenshot_(203).png](images/Screenshot_(203).png)

Realizamos cambios de seguridad en el servidor de base de datos  
Utilizamos el editor `nano` que trae por defecto Ubuntu  

```bash
$ sudo nano /etc/apt/preferences.d/mysql
```

Copiamos y pegamos en el documento recien abierto, lo siguiente:

```
Package: mysql-server
Pin: version 5.7.34-1ubuntu18.04
Pin-Priority: 1001

Package: mysql-client
Pin: version 5.7.34-1ubuntu18.04
Pin-Priority: 1001

Package: mysql-community-server
Pin: version 5.7.34-1ubuntu18.04
Pin-Priority: 1001

Package: mysql-community-client
Pin: version 5.7.34-1ubuntu18.04
Pin-Priority: 1001

Package: mysql-apt-config
Pin: version 0.8.10-1
Pin-Priority: 1001
```

**Comandos en nano:** 

- Ctrl + O → Para guardar
- Ctrl + x → Para salir

### Últimos pasos

Iniciamos el servicio de MySQL en [WSL](https://docs.microsoft.com/en-us/windows/wsl/)

```bash
$ sudo /etc/init.d/mysql start
```

Ingresamos al CLI y listo :) 

**Flags:** 

- -u → User
- -p → Password

```bash
$ mysql -uroot -p
```

![images/Screenshot_(205).png](images/Screenshot_(205).png)

![images/Screenshot_(204).png](images/Screenshot_(204).png)

Referencias: 

- [https://tecadmin.net/install-mysql-on-ubuntu-18-04-bionic/](https://tecadmin.net/install-mysql-on-ubuntu-18-04-bionic/)
- [https://downloads.mysql.com/archives/community/](https://downloads.mysql.com/archives/community/)
- [https://askubuntu.com/questions/1232558/install-mysql-5-7-on-ubuntu-20-04](https://askubuntu.com/questions/1232558/install-mysql-5-7-on-ubuntu-20-04)
- [https://www.digitalocean.com/community/questions/completely-uninstall-mysql-server](https://www.digitalocean.com/community/questions/completely-uninstall-mysql-server)

### Creación de usuario admin

Este usuario será en común para todos los integrantes del equipo para acceder a la base de datos desde la aplicación de Django.   
Esta no es una buena práctica de programación, es un abuso a la integridad y seguridad de la base de datos.  
Queda para uso académico y con el fin de la practicidad para este proyecto.  


```SQL
CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
FLUSH PRIVILEGES;
```

![mysql](images/Screenshot_(227).png)


Se crea una base de datos de ejemplo
```SQL
CREATE DATABASE TestConnection CHARACTER SET utf8;
```

## Python y entornos virtuales

---

Para crear un entorno virtual 

```bash
$ sudo python3 -m venv /path/to/new/virtual/environment
```

Por convención el nombre donde se instalaran los paquetes necesarios para crear el entorno virtual, se usa el nombre `venv`  

```bash
$ sudo python3 -m venv venv
```

### **Uso del entorno virtual**

Se genera una carpeta que contiene una versión de python en la cual se instalan las dependencias (paquetes) de manera ahislada, dentro de esta carpeta nos interesa la carpeta bin, en la que se encuentra el comando de activación `activate`

**Activación de entorno**

Debe recordar que `venv` es la carpeta donde se encuentran los paquetes del entorno virtual. En la línea de comandos ejecutamos lo siguiente

```bash
$ source venv\bin\activate
```

En este caso, el entorno virtual tiene una ruta diferente

![images/Screenshot_(212).png](images/Screenshot_(212).png)

El diferenciador entre haber activado el entorno virtual se nota en lado derecho de la consola 

`py Platzi`

Generalmente aparece al lado izquiero de la consola como `<venv>`

Anterior a esto no aparecía, indica que el entorno virtual contenido en la carpeta `Platzi` ha sido activado

![images/Screenshot_(210).png](images/Screenshot_(210).png)

**Desactivar el entorno**

Para desactivar el entorno virtual debe ubicarse en la carpeta raíz (la carpeta que contiene las dependencias de Python, es decir la carpeta superior a a la carpeta `venv`) del proyecto y escribir en la línea de comando lo siguiente

```bash
$ deactivate
```

## Configuración de Django

---

Explotamos las bondades y ventajas de los entornos virtuales en Python, dado que tienen flexibilidad, de esta forma cuidamos nuestras instancias globales de paquetes que no son relevantes para nosotros. 

Para ello activamos el entorno virtual recién creado en la carpeta `venv`

Como observación la carpeta `venv` tiene las dependencias de Python, es decir cualquier paquete que instalamos, se incluirá aquí.

Una vez activado el entorno continuamos con lo siguiente.

 

Instalación de Django

```bash
$ python3 -m pip install Django
```

Creamos un proyecto con el comando `django-admin startproject` 

```bash
$ django-admin startproject <name project> .
```

Resolver las dependencias
`migrate` Aplicará cambios en nuestra base de datos
```bash
$ python3 manage.py migrate
```

Ejecutar proyecto 

```bash
$ python3 manage.py runserver
```

Sí todo esta bien, puede ingresar al navegador colocando la siguiente dirección: 

```bash
http://127.0.0.1:8000/
```

### **Estructura de Archivos**

- El archivo vacío **init.py** indica que la carpeta es un módulo de python.
- El archivo **[settings.py](http://settings.py/)** define todas las configuraciones del proyecto.
    - BASE_DIR: Define la ubicación donde se está corriendo el proyecto.
    - SECRET_KEY: Es usado para el hashing de las contraseñas y las sesiones que se almacenan en la BD.
    - DEBUG: Define si el proyecto está en desarrollo para realizar debugging.
    - ALLOWED_HOSTS: Define que hosts están permitidos para que interactuen en nuestro proyecto.
    - INSTALLED_APPS: Aplicaciones ligadas al proyecto. Por defecto agrega la app de administrador, autenticación, contentypes (conexión a la BD), sesiones, mensajes y archivos estáticos.
    - MIDDLEWARE:
    - ROOT_URLCONF: Ubicación del principal de urls.
    - TEMPLATES:
    - WSGI_APPLICATION: Ubicación del principal de deployment.
    - DATABASES: Configuración y conexión a la BD.
    - AUTH_PASSWORD_VALIDATORS: Validadores de contraseñas. Si se está usando la app de autenticación, que la contraseña pase por las validaciones definidas:
        - Los valores de la contraseña no sean similares a los valores del usuario.
        - Que tenga una mínima longitud.
        - Validar la contraseña con un diccionario de contraseñas comunes.
        - Que la contraseña no sea numérica.
    - LANGUAGE_CODE: Lenguaje o idioma que está utilizando la aplicación.
    - TIME_ZONE: Se define el sistema horario en donde está corriendo la aplicación.
    - USE_I18N: Librería para traducción de textos.
    - USE_L10N: Librería para traducción de textos.
    - USE_TZ: Librería de timezone.
    - STATIC_URL: Define la ubicación de los archivos estáticos como css, js, img.
- El archivo **urls.py** define el punto de entrada para todas las peticiones que lleguen al proyecto.
- El archivo **wsgi.py** es utilizado para el deployment a producción.
- El archivo **manage.py** es uno que no se debe tocar y permite ejecutar todos los comandos que se hayan definido en las applicaciones instaladas del proyecto (entre ellas las del comando **django-admin**).
    - Cuando se ejecuta **python3 manage.py** por cada [nombre_app] se visualizarán los diferentes comandos que se pueden ejecutar por cada aplicación instalada del proyecto (auth, contenttypes, django, sessions, staticfiles).

    **Referencia**

    - [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)


### Conexión: Dango con MySQL 5.7

Active su entorno virtual.
Ejecutamos los siguientes comandos, utilizando el instalador de paquetes `pip` 

```Bash
#Para parsear archivos .ini
$ pip3 configparser

#conector de mysql desarrollado por Oracle
$ pip3 install mysql-connector-python


$ pip3 install pymysql
```

![](images/Screenshot_(231).png)

Una vez hecho esto, debe ir a la carpeta raíz del proyecto y buscar el archivo `__init__.py`, coloca lo siguiente
```Python
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
``

Guarda y cierre el archivo.

Para crear la conexión de la base de datos con Django, debe realizar ciertos cambios. 
Modificar el archivo `settings.py` que se encuentra en la carpeta principal del proyecto, buscar la variable `DATABASES`
```Python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
```

Cambiar por lo siguiente
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS':{
            'init_command': 'SET default_storage_engine=INNODB',
        },
        'NAME':'TestConnection',
        'USER':'admin',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```


Al iniciar el server `python3 manage.py runserver`

![](images/Screenshot_(241).png)

Podemos corregir estas migraciones

```Bash
python3 manage.py migrate
```

![](images/Screenshot_(243).png)


Como últimas anotaciones haremos la conexión de Workbench a las instancias de MySQL 5.7 instaladas en WSL.  

Descargamos e instalamos el MySQL Workbench
- [Workbench](https://dev.mysql.com/downloads/workbench/)


Ejecutamos el programas 
![](images/Screenshot_(235).png)


Iniciamos una nueva conexión, colocamos un nombre a la conexión y utilizamos las credenciles del usuario `admin`
![](images/Screenshot_(236).png)

Hacemos un test a la conexión
![](images/Screenshot_(237).png)

Tenemos una conexión hacia el DBMS utilizando Workbench
![](images/Screenshot_(238).png)