# Variables de entorno
import pymysql
from decouple import config # nos permite leer variables de entorno

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

# Colocar directamente en el script las credenciales necesarias
# para conectarse a la DB puede traer vulnerabilidades.
# Una buena forma de salvaguardar informacion sensible, es
# almacenandola dentro de variables de entorno.

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user=config('USER_MYSQL'),
            passwd=config('PASSWORD_MYSQL'),
            db=config('DB_MYSQL')
            # la función config() recibe como argumento el nombre
            # de la variable de entorno, si existe el valor es
            # retornado, sino podremos establecer un valor por
            # default y castearlo.
        )

        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

    except pymysql.err.OperationalError as err:
        print('No fue posible completar la operación.\n')
        print(err)
    finally:
        connect.close()
        print('Conexión finalizada de forma exitosa.')
