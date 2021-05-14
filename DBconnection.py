import sqlite3 as dbapi


class DBconnection:

    def __init__(self, dbRoute):
        """
        Crea as propiedades e as inicializa
        :param dbRoute: Ruta onde se encontra o ficheiro da base de datos SQlite
        """
        self.dbRoute = dbRoute
        self.connection = None
        self.cursor = None

        """
        Codigo que crea a conexión da base de datos.
        Para realizar a conexión precisa da ruta onde está a base de datos.
        """

        try:
            if self.connection is None:
                if self.dbRoute is None:
                    print("A ruta da base de datos é: None ")
                else:
                    self.connection = dbapi.connect(self.dbRoute)
            else:
                print("Base de datos conectada: " + self.connection)

        except dbapi.StandardError as e:
            print("Erro o facer a conexión a base de datos " + self.dbRoute + ": " + e)
        else:
            print("Conexión á base de datos realizada")

        """
        Codigo que crea o cursor da base de datos.
        Para realizar o cursor precísase previamente da conexión da BD, que crea a conexión a base de
        datos na ruta dada.
        """

        try:
            if self.connection is None:
                print("Creando o cursor: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    self.cursor = self.connection.cursor()
                else:
                    print("O cursor xa esta inicializado: " + self.cursor)

        except dbapi.Error as e:
            print(e)
        else:
            print("Cursor preparado")

    def genericQuery(self, query):
        result = list()
        try:
            if self.connection is None:
                print("É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("É necesario crear un cursor previamente")
                else:
                    self.cursor.execute(query)

                    for i in self.cursor.fetchall():
                        result.append(i)
        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return result
