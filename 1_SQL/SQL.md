# SQL y Python

Utilizaremos sentencias SQL a traves de Python, por lo que utilizaremos el gestor de base de datos MySQL, utilizaremos la siquiente libreria: **PyMySQL**.

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
