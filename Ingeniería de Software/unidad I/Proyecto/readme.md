```
    @author: Kenneth Cruz
    @version 0.1.0    
    @date: 2021/06/03
```

# Configuración de Entorno: Django, MySQL 5.7, Python 3.8 en WSL (Windows Subsystem for Linux) 20.04 LTS

<br>

Entorno de configuración necesario para instalar las dependencias del proyecto correspondiente a la clase **Ingeniería de Software (IS 802)**

Este documento abarca la instalación del siguiente software:

- Python 3
- Django 3.2
- MySQL 5.7
- Windows 10
    - Ubuntu 20.04 LTS (WSL)
    - Windows Terminal

Se explota las capacidades y bondades de WSL (Windows Subsystem for Linux) por ser una máquina virtual nativa de Ubuntu en Windows, la mayoría de características han sido probadas.

## Índice

---

- [Configuración de Entorno: Django, MySQL 5.7, Python 3.8 en WSL (Windows Subsystem for Linux) 20.04 LTS](#configuración-de-entorno-django-mysql-57-python-38-en-wsl-windows-subsystem-for-linux-2004-lts)
  - [Índice](#índice)
  - [Visual Code](#visual-code)
  - [Configuración de WSL](#configuración-de-wsl)
  - [Configuración de MySQL 5.7](#configuración-de-mysql-57)
    - [Una vez desempaquetado los binarios, pasamos a la siguiente fase.](#una-vez-desempaquetado-los-binarios-pasamos-a-la-siguiente-fase)
    - [Últimos pasos](#últimos-pasos)
    - [Creación de usuario admin](#creación-de-usuario-admin)
  - [Python y entornos virtuales](#python-y-entornos-virtuales)
    - [**Uso del entorno virtual**](#uso-del-entorno-virtual)
  - [Configuración de Django](#configuración-de-django)
    - [**Estructura de Archivos:**](#estructura-de-archivos)

## Visual Code

---

Pluggins a instalar (no son indispensables, sin embargo son una herramienta útil)

- **GitLens:** eamodio.gitlens
- **ErrorLens:** usernamehw.errorlens
- **Django:** batisteo.vscode-django
- **Markdown All in One:** yzhang.markdown-all-in-one

Para instalar estos plugins en Visual Code es necesario copiar y pegar el id en la sección `Extensions` del editor de texto.

![images/Screenshot_(206).png](images/Screenshot_(206).png)

## Configuración de WSL

---

Para configurar WSL en Windows 10, debe seguir lo siguiente: 

Debe ir a la tienda de Microsoft y escribir **Ubuntu 20.04 LST** una vez hecho esto, clic en Launch

![images/Screenshot_(214).png](images/Screenshot_(214).png)

Una vez hecho esto puede buscar el programa en su máquina, escribiendo **ubuntu 20.04 LTS**

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

Al ejecutar el comando anterior se visuliza algo similar a lo siguiente: 

![images/Screenshot_(201).png](images/Screenshot_(201).png)

La versión resaltada en color gris, es la última disponible para este caso:

**<5.7.34-1ubuntu18.04>**

### Una vez desempaquetado los binarios, pasamos a la siguiente fase.

Instalación de las instancias del Servidor 

```bash
$ sudo apt install -f mysql-client=5.7.34-1ubuntu18.04

#En este paso pedirá configurar la contraseña del root
#NO OLVIDE EL PASSWORD INGRESADO
$ sudo apt install -f mysql-community-server=5.7.34-1ubuntu18.04

$ sudo apt install -f mysql-server=5.7.34-1ubuntu18.04
```

![images/Screenshot_(203).png](images/Screenshot_(203).png)

Realizar cambios de seguridad en el servidor de base de datos
Evitamos la actualización a MySQL 8.0 , utilizamos el editor por que trae por defecto Ubuntu, *nano*

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

Iniciamos el servicio de MySQL en WSL

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

Para desactivar el entorno virtual debemos ubicarnos en la carpeta raíz (la carpeta que contiene las dependencias de Python) del proyecto y escribir en la línea de comando lo siguiente

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

```bash
$ python3 manage.py migrate
```

Ejecutar proyecto 

```bash
$ python3 manage.py runserver
```

Sí todo esta bien, podemos ingresar a nuestro navegador a la siguiente dirección: 

```bash
http://127.0.0.1:8000/
```

### **Estructura de Archivos:**

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
- El archivo **[urls.py](http://urls.py/)** define el punto de entrada para todas las peticiones que lleguen al proyecto.
- El archivo **[wsgi.py](http://wsgi.py/)** es utilizado para el deployment a producción.
- El archivo **[manage.py](http://manage.py/)** es uno que no se debe tocar y permite ejecutar todos los comandos que se hayan definido en las applicaciones instaladas del proyecto (entre ellas las del comando **django-admin**).
    - Cuando se ejecuta **python3 [manage.py](http://manage.py/)** por cada [nombre_app] se visualizarán los diferentes comandos que se pueden ejecutar por cada aplicación instalada del proyecto (auth, contenttypes, django, sessions, staticfiles).

    **Referencia**

    - [https://docs.djangoproject.com/en/3.2/intro/tutorial01/](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)