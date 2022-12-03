# Cerrar conexión
import pymysql

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

# Al trabajar con objetos de tipo conexion y tipo cursor es que
# una vez utilizados debemos finalizarlos para liberar espacio
# en memoria RAM.

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='56208856',
            db='python_db'
        )
        cursor = connect.cursor()
        cursor.execute(DROP_TABLE_USERS)
        cursor.execute(USERS_TABLE)
    except pymysql.err.OperationalError as err:
        print('No fue posible completar la operación.\n')
        print(err)
    finally:
        # una vez ejecutados los métodos close() no podremos
        # utilizarlos más.
        cursor.close()
        connect.close()
        print('Conexión finalizada de forma exitosa.')

