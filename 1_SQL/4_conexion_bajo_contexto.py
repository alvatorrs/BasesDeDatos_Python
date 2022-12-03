# Conexión bajo contexto
import pymysql

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

# Otra forma en la que podemos utilizar nuestro objeto de tipo
# connect o de tipo cursor, es mediante un contexto donde 
# obtenemos un código más pythonico.

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='56208856',
            db='python_db'
        )

        # cursor = connect.cursor()
        # cursor.execute(DROP_TABLE_USERS)
        # cursor.execute(USERS_TABLE)

        # manejador contextual
        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

    except pymysql.err.OperationalError as err:
        print('No fue posible completar la operación.\n')
        print(err)
    # Al terminar el bloque del manejador contextual, el objeto 
    # cursor de forma automática va a ejecutar su método close()
    # cerrando así dicha conexión.
    finally:
        # cursor.close()
        connect.close()
        print('Conexión finalizada de forma exitosa.')
    # podemos hacer lo mismo con el objeto de tipo connect
    # pero por legibilidad se dejará de la otra forma.
