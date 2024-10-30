#!/usr/bin/python
import MySQLdb
import cgi
import cgitb
import json


db = MySQLdb.connect(
host="",
user="",
password="",
database="")

c=db.cursor()

form = cgi.FieldStorage()
ip = None
email = form["email"].value
fill = form.getvalue('fillout')

if fill == '0':
    setAlreadyParticipantsepent = False
    c.execute("SELECT * FROM gewinnspiel_table WHERE email = (%s);", (email,))
    out = c.fetchone()
    if out is not None:
        setAlreadyParticipantsepent = True

    if not setAlreadyParticipantsepent:
        try:
            c.execute("INSERT INTO gewinnspiel_table (email, ip) VALUES((%s),(%s));", (email, ip))
            db.commit()
        
            c.close()    
            print ("Location: https://teilnahme-gewinnspiel.de/successful\r\n")
        except MySQLdb.IntegrityError:
            print ("Location: https://teilnahme-gewinnspiel.de/unsuccessful\r\n")
            

    else:
        c.close()
        print ("Location: https://teilnahme-gewinnspiel.de/rejected\r\n")
else:
    c.close()
    print ("Location: https://teilnahme-gewinnspiel.de/notfillout\r\n")
   


