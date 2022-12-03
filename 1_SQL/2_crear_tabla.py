# Crear tabla
import pymysql

# almacena la sentencia sql para crear la tabla
USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

# almacena la sentencia sql para eliminar la tabla
DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"


if __name__ == '__main__':
    try:
        # creamos la instancia
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='56208856',
            db='python_db'
        )
        # para ejecutar sentencias sql utilizaremos un cursor
        cursor = connect.cursor() # retorna un objeto de tipo cursor
        cursor.execute(DROP_TABLE_USERS) # ejecuta la sentencia sql
        cursor.execute(USERS_TABLE) # ejecuta la sentencia sql
        print('Conexión exitosa!.')
    except pymysql.err.OperationalError as err:
        print('No fue posible completar la operación.\n')
        print(err)

