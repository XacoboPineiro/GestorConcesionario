class QueryConstructor:

    def __init__(self):
        self.table = None
        self.fields = None
        self.paramenters = None

    def noParametersQuery(self, table, *fields):
        query = "SELECT "
        for i in fields:
            query = query + i + ", "
        query = query[:-2]
        query = query + " FROM " + table
        return query

    def singleWhereQuery(self, table, parameter, operand, *fields):
        query = self.noParametersQuery(table, *fields)
        query = query + " WHERE " + parameter + " " + operand + " ?"
        return query
