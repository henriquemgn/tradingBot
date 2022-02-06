import sqlite3
conn = sqlite3.connect('soldatdata.db')
c = conn.cursor()

def insertSold(Price):
	c.execute("INSERT INTO VALUE(sold) VALUES (?)",(Price,))
	conn.commit()
	return 0

def getSold():
	c.execute("SELECT * FROM VALUE")
	SOLDAT = c.fetchall()
	return(SOLDAT)

def removeSold():
	c.execute('''
			DELETE from VALUE
			''')
	conn.commit()
	return 0

def formatSold(SOLDAT):
	if SOLDAT != []:
		return SOLDAT[0][0]
	else:
		return 0

def checkEmpty():
	c.execute("SELECT COUNT(*) FROM VALUE")
	if c.fetchall()[0][0] == 0:
		print("1")
		return 1
	else:
		print("0")
		return 0

#insertSold("1000")
#removeSold()
#print(getSold())
checkEmpty()
