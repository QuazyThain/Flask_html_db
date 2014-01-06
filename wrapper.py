# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:32:52 2013

@author: quazythain
"""
# hdb.insert('users', {'name':'HeyHey', 'last_name':'Namaste',
#            'user_login':'rishikesh'})
# hdb.select('*', 'users', 'user_id=2')
import MySQLdb


class HeyheyDB(object):
    def __init__(self):
        try:
            self.db = MySQLdb.connect(host="localhost", user="root",
                                      passwd="rishikesh", db="heyhey")
            self.cursor = self.db.cursor()
        except:
            print "Can't connect to database"

    def select(self, fields, table, where):
        if fields == "*":
            q = "SELECT * FROM {0}".format(table)
        else:
            get_fields = fields
            fields = ', '.join(get_fields)

            q = "SELECT {0} FROM {1} WHERE {2};".format(fields, table, where)
        try:
            self.cursor.execute(q)
            output = self.cursor.fetchall()
            print output
            return output
        except:
            print "Can't execute sql query"

    def insert(self, table, fields):
        get_columns = fields.keys()
        columns = ', '.join(get_columns)
        get_values = fields.values()
        cortege_values = []
        for value in get_values:
            cortege_values.append("'{0}'".format(value))
        values = ', '.join(cortege_values)

        q = "INSERT INTO {0} ({1}) VALUE ({2});".format(table, columns, values)
        try:
            self.cursor.execute(q)
            self.db.commit()
        except:
            print "Can't execute insert query"
            self.db.rollback()

    def update(self, table, fields, where):
        get_fields = fields.items()
        cortege_fields = []
        for key, value in get_fields:
            cortege_fields.append("{0}='{1}'".format(key, value))
        complete_fields = ', '.join(cortege_fields)

        q = "UPDATE {0} SET {1} WHERE {2}".format(table, complete_fields,
                                                  where)
        print q
        try:
            self.cursor.execute(q)
            self.db.commit()
        except:
            print "Can't execute update query"
            self.db.rollback()

    def delete(self, table, where):

        q = "DELETE FROM {0} WHERE {1};".format(table, where)
        try:
            self.cursor.execute(q)
            self.db.commit()
        except:
            print "Cant execute delete query"
            self.db.rollback()

    def disconnect(self):
        if self.db is not None:
            try:
                self.db.close()
                self.db = None
            except:
                print "Can't disconnect from database"

if __name__ == "__main__":
    hdb = HeyheyDB()
