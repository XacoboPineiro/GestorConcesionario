import DBconnection
import QueryConstructor

dbConnection = DBconnection.DBconnection("DBconcesionario.db")
queryConstructor = QueryConstructor.QueryConstructor()
print(queryConstructor.noParametersQuery("coches", "fabricante", "modelo"))
print(queryConstructor.singleWhereQuery("coches", "id", "=", "fabricante", "modelo"))
