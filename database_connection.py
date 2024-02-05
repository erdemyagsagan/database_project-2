# database_connection.py
import psycopg2
import psycopg2.extras

class DatabaseCon:
    hostname = 'localhost'
    database = 'dbms_projectDB'
    username = 'postgres'
    pwd = 'Tk240108'
    port_id = 5432

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host=self.hostname,
                dbname=self.database,
                user=self.username,
                password=self.pwd,
                port=self.port_id
            )
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception as error:
            print(error)

    def close_connection(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as error:
            print(error)
