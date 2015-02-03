import psycopg2

class Dao:
    def __init__(self, db_name, db_user, db_password):
        self._name = db_name
        self._user = db_user
        self._pass = db_password

    def __enter__(self):
        conn = psycopg2.connect("dbname=%s user=%s password=%s" %
            (self._name, self._user, self._pass))
        self.conn = conn

        class _Dao:
            def get(self, table, orderBy="id", limit=None):
                cursor = conn.cursor()
                sql = "SELECT * FROM %s ORDER BY %s" % (table, orderBy)
                if limit:
                    sql += " LIMIT %i" % limit
                cursor.execute(sql)
                return cursor.fetchall()

        return _Dao()

    def __exit__(self, type, value, traceback):
        self.conn.close()
