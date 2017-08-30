#!/usr/bin/python

import MySQLdb

db=MySQLdb.connect("localhost","root","root","test")

cursor=db.cursor()

sql="""insert into employee(first_name,
       last_name, sex, age, income)
       values("rupak","rokade","Male",29,50000)"""

try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()

db.close()
