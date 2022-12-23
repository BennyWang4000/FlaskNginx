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
        return self.db.query_read('select med_id, cli_id, cli_date, cli_day, cli_time, app_check, doc_name, dep_name from ( select med_id, cli_id, cli_date, cli_day, cli_time, app_check, d.dep_id, d.doc_name from ( select med_id, a.cli_id, cli_date, cli_day, cli_time, app_check, dep_id, doc_id from ( SELECT cli_id, med_id, app_check FROM hos_db.appointment WHERE med_id = %s ) as a inner join hos_db.clinic as c on a.cli_id = c.cli_id ) as ac inner join hos_db.doctor as d on ac.doc_id = d.doc_id ) as acd inner join hos_db.department as p on acd.dep_id = p.dep_id order by cli_date, cli_time', (med_id)).fetchall()
        # return self.db.query_read('select cli_id, cli_date, cli_day, cli_time, doc_name, dep_name from (select cli_id, cli_date, cli_day, cli_time, d.doc_name, d.dep_id from (select * from hos_db.clinic where cli_id in (select cli_id, app_check from appointment where med_id = %s)) as c inner join doctor as d on d.doc_id=c.doc_id) as cd inner join department on department.dep_id=cd.dep_id order by cli_date, cli_time', (med_id)).fetchall()

    def insert_app(self, med_id, cli_id):
        return self.db.query_write('insert into hos_db.appointment (med_id, cli_id, app_check) values (%s, %s, %s);', (med_id, cli_id, 0)).fetchall()

    def complete_app(self, med_id, cli_id):
        return self.db.query_write('UPDATE hos_db.appointment SET app_check = 1 WHERE med_id = %s AND cli_id = %s;', (med_id, cli_id)).fetchall()

    def cancel_app(self, med_id, cli_id):
        return self.db.query_write('UPDATE hos_db.appointment SET app_check = 2 WHERE med_id = %s AND cli_id = %s;', (med_id, cli_id)).fetchall()
