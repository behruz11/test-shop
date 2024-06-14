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
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"You are connected to - {record}\n")
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    # Connect to first PostgreSQL instance
    connect_to_postgres(
        host=os.getenv("POSTGRES1_HOST"),
        port=os.getenv("POSTGRES1_PORT"),
        dbname=os.getenv("POSTGRES1_DB"),
        user=os.getenv("POSTGRES1_USER"),
        password=os.getenv("POSTGRES1_PASSWORD")
    )
    # Connect to second PostgreSQL instance
    connect_to_postgres(
        host=os.getenv("POSTGRES2_HOST"),
        port=os.getenv("POSTGRES2_PORT"),
        dbname=os.getenv("POSTGRES2_DB"),
        user=os.getenv("POSTGRES2_USER"),
        password=os.getenv("POSTGRES2_PASSWORD")
    )
