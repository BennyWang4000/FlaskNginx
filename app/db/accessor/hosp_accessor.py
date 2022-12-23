from db.db_helper import DbHelper

class HospAccessor:
    def __init__(self, host, user, database, password):
        self.db = DbHelper(host=host, user=user,
                           password=password, database=database)

    def select_dep(self):
        '''select all department name
        returns
        -------
        
        '''
        return self.db.query_read('SELECT * FROM hos_db.department;', None).fetchall()

    def select_doc(self, dep_id):
        '''select 
        '''
        return self.db.query_read('SELECT * FROM hos_db.doctor WHERE dep_id = %s;', (dep_id)).fetchall()

    def select_cli(self, doc_id):
        return self.db.query_read("SELECT * FROM hos_db.clinic WHERE doc_id = %s;", (doc_id)).fetchall()

    def select_app(self, med_id, pat_date):
        return self.db.query_read('select cli_id, cli_date, cli_day, cli_time, doc_name, dep_name from (select cli_id, cli_date, cli_day, cli_time, d.doc_name, d.dep_id from (select * from hos_db.clinic where cli_id in (select cli_id from appointment where med_id = %s)) as c inner join doctor as d on d.doc_id=c.doc_id) as cd inner join department on department.dep_id=cd.dep_id', (med_id)).fetchall()

    def insert_app(self, med_id, cli_id):
        return self.db.query_write('insert into hos_db.appointment (med_id, cli_id, app_check) values (%s, %s, %s);', (med_id, cli_id, 0)).fetchall()
        # return self.db.query_write('UPDATE appointment SET app_check = 2 WHERE med_id = %s AND cli_id = %s;', (med_id, cli_id)).fetchall()

    def cancel_app(self, med_id, cli_id):
        return self.db.query_write('UPDATE appointment SET app_check = 2 WHERE med_id = %d AND cli_id = %d;', (med_id, cli_id)).fetchall()