#!/usr/bin/python
import MySQLdb
import cgi
import json

try:
    db = MySQLdb.connect(
	host="",
	user="",
	password="",
    database=""
	
)
	
    c=db.cursor()
    c.execute("""SELECT * FROM umfragen_besitzer""")
    row_headers = [x[0] for x in c.description]
    out = c.fetchall()
    json_data = []
    for result in out:
        json_data.append(dict(zip(row_headers,result)))
    
 
  
 
except Exception as err:
	db = "Fail"
    



print ('Content-Type: application/json\n\n')
print (json.dumps(json_data))