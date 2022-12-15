# Insertar registros
import pymysql
from decouple import config

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"


if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user=config('USER_MYSQL'),
            passwd=config('PASSWORD_MYSQL'),
            db=config('DB_MYSQL')
        )
        
        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)
            # Insertando registros 
            # para reutilizar la sentencia usamos place holders
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            values = ('Alvaro', '1234', 'alva@roto.com') # valores a almacenar
            cursor.execute(query, values) # ejecutamos la sentencia sql
            # Como al hacer un INSERT INTO estamos modificando la tabla
            # es necesario confirmar los cambios a la tabla, para que estos
            # sean observados el hacer un SELECT, por lo que haremos un commit.
            # El commit no lo va a realizar el cursor, sino connect.
            connect.commit() # persiste todos los cambios realizados hasta ahora.
     
    except pymysql.err.OperationalError as err:
        print('No fue posible completar la operación.\n')
        print(err)
    finally:
        connect.close()
        print('Conexión finalizada de forma exitosa.')