######################
#Anthony Rivera#######
#CIS 117 OL###########
######################
#Program to create database

import sqlite3 // importing sqllite
conn = sqlite3.connect('yourlastname.db') // connecting to the database
cur = conn.cursor()
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)') // creating tables
cur.execute('INSERT INTO PopByRegion VALUES ("Central Africa",330993)') // inserting row
cur.execute('INSERT INTO PopByRegion VALUES ("Southeastern Africa",743112)') // inserting row
cur.execute('INSERT INTO PopByRegion VALUES ("Japan",100562)') // inserting row
cur.execute('SELECT Region, Population FROM PopByRegion') // A series of sql statements to be executed  
cur.fetchall()
cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
cur.fetchall()
cur.execute('SELECT Region FROM PopByRegion')
cur.fetchall()
cur.execute ('SELECT Region FROM PopbyRegion WHERE Population > 400000')
cur.fetchall()
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan" ')
cur.fetchone()
cur.execute('' 'UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan" '' ')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
cur.fetchone()
cur.execute('DELETE FROM PopByRegion WHERE Region < "S" ')
cur.execute('SELECT * FROM PopByRegion')
cur.fetchall()
cur.close()
conn.close()