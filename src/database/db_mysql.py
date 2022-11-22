import mysql.connector
from mysql.connector import Error


class DBConnection:

    _connect = None
    __access = {
    "host": "127.0.0.1",
    "username": "root",
    "password": "root",
    "db": "bancodb"
}

    def __init__(self) -> None:
        self._connect = mysql.connector.connect(**self.__access)
         
         
    def write_query(self, query: str):
        try:
            cursor = self._connect.cursor()
            cursor.execute(query)
            id = cursor.lastrowid
            self._connect.commit()
        except Error as err:
            print("\n")
            print(err)
            print("\n")
        else:
            return id

    
    def read_query(self, query: str):
        try:
            result = None
            cursor = self._connect.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as err:
            print("\n")
            print(err)
            print("\n")
        else:
            return result

connection: DBConnection = DBConnection()