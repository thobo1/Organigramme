import adodbapi

class Database:
    def __init__(self, path=None, password=None):
        self.__path = path
        self.__password=password
        self.__connection = adodbapi

    def setPassword(self, password):
        self.__password = password

    def setPath(self, path):
        self.__path = path

    def connect(self):
        try:
            conn_string = "Provider=Microsoft.SQLSERVER.CE.OLEDB.4.0;Data Source=%s; SSCE:Database Password=%s;" %(self.__path,self.__password)
            self.__connection = adodbapi.connect(conn_string)
            self.__connection.connector.CursorLocation = 2
            return True
        except (adodbapi.DatabaseError, adodbapi.InterfaceError) as e:
            print(e)
            return False

    def select(self, table):
        query = "SELECT * FROM [%s]" % (table)
        curs = self.__connection.cursor()
        curs.execute(query)
        return curs.fetchall()

    def select_condition(self, table, condition):
        query = "SELECT * FROM [%s] WHERE %s" % (table, condition)
        curs = self.__connection.cursor()
        curs.execute(query)
        return curs.fetchall()

    def update(self, query):
        curs = self.__connection.cursor()
        curs.execute(query)
        self.__connection.commit()


    def insert(self, query):
        curs = self.__connection.cursor()
        curs.execute(query)
        self.__connection.commit()
