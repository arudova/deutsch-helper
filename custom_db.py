from PySide import QtSql


class CustomDB:
    def __init__(self):
        databaseType = "QSQLITE"
        databaseLocation = "db/"
        databaseName = "deutsch_helper"
        hostName = "localhost"
        userName = "adi"
        password = "password"

        database = QtSql.QSqlDatabase.addDatabase(databaseType)
        database.setHostName(hostName)
        database.setDatabaseName(databaseLocation + databaseName)
        database.setUserName(userName)
        database.setPassword(password)

        self.database = database

    def open(self):
        self.database.open()

    def close(self):
        self.database.close()

    def getDictionary(self):
        query_text = """
                        SELECT
                            words.english,
                            words.deutsch,
                            words.nominativ,
                            words.akkusativ,
                            words.dativ,
                            words.genitiv
                        FROM
                            words
                    """

        query = QtSql.QSqlQuery(query_text)

        result = []

        while query.next():
            row = {}
            row['english'] = query.value(query.record().indexOf("english"))
            row['deutsch'] = query.value(query.record().indexOf("deutsch"))
            row['nominativ'] = query.value(query.record().indexOf("nominativ"))
            row['akkusativ'] = query.value(query.record().indexOf("akkusativ"))
            row['dativ'] = query.value(query.record().indexOf("dativ"))
            row['genitiv'] = query.value(query.record().indexOf("genitiv"))
            result.append(row)

        if query.lastError().type() != QtSql.QSqlError.ErrorType.NoError:
            print(query.lastError())

        return result
