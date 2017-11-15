################
#Anthony Rivera#
#CIS 117 OL    #
#Lab10         #
#11/10/2017    #
################
import sqlite3 
conn = sqlite3.connect('rivera.db') 
cur = conn.cursor()
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)') 
cur.execute('INSERT INTO PopByRegion VALUES ("Central Africa",330993)') 
cur.execute('INSERT INTO PopByRegion VALUES ("Southeastern Africa",743112)') 
cur.execute('INSERT INTO PopByRegion VALUES ("Japan",100562)') 
cur.execute('SELECT Region, Population FROM PopByRegion')   
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