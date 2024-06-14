import os
import psycopg2

def connect_to_postgres(host, port, dbname, user, password):
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=dbname,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        # Выполнение запроса для получения информации о версии PostgreSQL
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        
        # Выполнение запроса для получения текущей базы данных
        cursor.execute("SELECT current_database();")
        current_db = cursor.fetchone()
        
        # Выполнение запроса для получения текущего пользователя
        cursor.execute("SELECT current_user;")
        current_user = cursor.fetchone()
        
        print(f"Connected to PostgreSQL server - {version[0]}")
        print(f"Current database: {current_db[0]}")
        print(f"Current user: {current_user[0]}\n")
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    # Подключение к первому экземпляру PostgreSQL
    print("Connecting to first PostgreSQL instance...")
    connect_to_postgres(
        host=os.getenv("POSTGRES1_HOST"),
        port=os.getenv("POSTGRES1_PORT"),
        dbname=os.getenv("POSTGRES1_DB"),
        user=os.getenv("POSTGRES1_USER"),
        password=os.getenv("POSTGRES1_PASSWORD")
    )
    
    # Подключение ко второму экземпляру PostgreSQL
    print("Connecting to second PostgreSQL instance...")
    connect_to_postgres(
        host=os.getenv("POSTGRES2_HOST"),
        port=os.getenv("POSTGRES2_PORT"),
        dbname=os.getenv("POSTGRES2_DB"),
        user=os.getenv("POSTGRES2_USER"),
        password=os.getenv("POSTGRES2_PASSWORD")
    )
