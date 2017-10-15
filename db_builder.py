import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
command1="CREATE TABLE classes (code TEXT, mark INTEGER, id INTEGER);"  #put SQL statement in this string
c.execute(command1)  #run SQL statement

with open('courses.csv','rb') as t:
    courses=csv.DictReader(t)
    for row in courses:
        values=[(row['code'],int(row['mark']), int(row['id']))]
        command2="INSERT INTO classes VALUES (?,?,?);"
        c.executemany(command2, values)  #run SQL statement
        
command3="CREATE TABLE people (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"  #put SQL statement in this string
c.execute(command3)  #run SQL statement

with open('peeps.csv','rb') as p:
    peeps=csv.DictReader(p)
    for row in peeps:
        values=[(row['name'],int(row['age']), int(row['id']))]
        command4="INSERT INTO people VALUES (?,?,?);"
        c.executemany(command4, values)  #run SQL statement



#==========================================================
db.commit() #save changes
db.close()  #close database


