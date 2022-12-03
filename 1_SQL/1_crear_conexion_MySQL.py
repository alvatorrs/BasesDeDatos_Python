# Crear conexión MySQL
import pymysql # importamos PyMySQL

# Crearemos un objeto de tipo Connect para establecer una conexion
# entre nuestra aplicación y el gestor de base de datos.

if __name__ == '__main__':
    try:
        # generando la conexión a traves de una instancia
        connect = pymysql.Connect(
            host='localhost', # ruta de la DB a utilizar
            port=3306, # puerto donde se realiza la conexión
            user='root', # usuario
            passwd='56208856', # contraseña del usuario
            db='python_db' # base de datos a utilizar
        )
        # verificamos que se haya realizado la conexión
        print('Conexión realizada de forma exitosa.')
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión.')
        print(err)
        # lo mejor que podemos hacer al crear una conexión
        # es utilizar un try/except para manejar los errores.
