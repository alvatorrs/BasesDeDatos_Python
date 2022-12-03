# SQL y Python

Utilizaremos sentencias SQL a traves de Python, por lo que utilizaremos el gestor de base de datos MySQL, utilizaremos la siquiente libreria: [PyMySQL](https://pypi.org/project/PyMySQL/).

Para ello primero crearemos nuestro entorno de desarrollo.

1) Creamos el entorno virtual. Utilizando conda usamos el comando 
``conda create --name 1_SQL python=3.9``.

2) Activamos nuestro entorno virtual con : 
`conda activate nombreEntorno`.

3) Intalamos el paquete con: 
`pip install PyMySQL`````````.



##Observaciones sobre MySQL

- Para instalar MySQL en Ubuntu, podemos utilizar el comando:
`sudo apt install mysql-server`.

- Para reiniciar el servidor de MySQL:
`sudo service mysql start`.

- Para ver la versión de MySQL:
`mysql --version`.

- Para abrir MySQL:
`sudo mysql`.

- Para salir de MySQL:
`exit`.

- Para parar el servicio de MySQL:
`service mysql stop`.

- Acceder a mysql por medio del usuario root:
`mysql -u root -p`.

##Variables de entorno

Nos ayudan a evitar vulnerabilidades y salvaguardar nuestra información sensible.
Para crear una variable de entorno en un sistema operativo basado en UNIX, crear variables de entorno es bastante sencillo.
Nos colocamos en nuestra terminal y escribimos: 
`export nombre_variable=valor_almacenado`.
Ejemplos:
- export USER_MYSQL=root
- export PASSWORD_MYSQL=56208856
- export DB_MYSQL=python_db

En Python existen diferentes formas en las que podemos obtener valores de variables de entorno:
- La forma más comun es con el modulo **os**.
- Otra alternativa es utilizando el modulo [decouple](https://pypi.org/project/python-decouple/) que es fácil de utilizar y nos permite leer variables de entorno. Para instalarla utilizamos el comando:
 `pip install python_decouple`.
