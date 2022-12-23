import pymysql


class DbHelper:
    '''
    params:
    ------
        host: str
        user: str
        db: str
        password: str

    returns:
    ------
        none
    '''

    def __init__(self, host, user, database, password):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.connection_read = pymysql.connect(host=host,
                                               user=user,
                                               password=password,
                                               db=database,
                                               charset='utf8',
                                               cursorclass=pymysql.cursors.DictCursor,)

        self.connection_write = pymysql.connect(host=host,
                                                user=user,
                                                password=password,
                                                db=database,
                                                charset='utf8',
                                                cursorclass=pymysql.cursors.DictCursor,)
                                                
        # self.cursor_read = self.connection_read.cursor()
        # self.cursor_write = self.connection_write.cursor()

    def query_read(self, query, params=None):
        with self.connection_read.cursor() as cursor:
            cursor.execute(query, params)
            return cursor

    def query_write(self, query, params=None):
        with self.connection_write.cursor() as cursor:
            cursor.execute(query, params)
            self.connection_write.commit()
            self.connection_read.commit()
            return cursor

    def close(self):
        self.connection_read.close()
        self.connection_write.close()
