#!/usr/bin/python

import MySQLdb
data='rupak'
db=MySQLdb.connect("localhost","root","root","test")

cursor=db.cursor()

sql="""select * from account where username like '"""+data+"'"

try:
  cursor.execute(sql)
  result=cursor.fetchone()
  #db.commit()
except:
  db.rollback()

db.close()

print result
