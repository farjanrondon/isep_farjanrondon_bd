import sqlite3 as sql

conex = sql.connect('BD.env')
cursor = conex.cursor()

cursor.execute('''

	CREATE TABLE LEADS_NOMBRE_TELEFONO(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMRE VARCHAR(50), 
	TELEFONO VARCHAR(50)
	)

	''')

cursor.execute('''
	
	CREATE TABLE LEADS_NOMBRE_EMAIL(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMRE VARCHAR(50),
	EMAIL VARCHAR(50))

	''')

cursor.execute('''
	
	CREATE TABLE LEADS_NOMBRE_NOTA(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMRE VARCHAR(50),
	NOTAS VARCHAR(50))

	''')


telefonos = [

	('Farjan Rondon', '+584142593777'),
	('Violeta Santos', '+584244593755'),
	('Jairo Rondon', '+584162993424'),
	('Francia Rondon', '+584122093242')

]

emails = [

	('Farjan Rondon', 'santosfarjan@gmail.com'),
	('Violeta Santos', 'violetasantos@gmail.com'),
	('Jairo Rondon', 'jairorondon@gmail.com'),
	('Francia Rondon', 'franciarondon@gmail.com')

]

notas = [

	('Farjan Rondon', 'Lorem ipsum dolor sit amet consectetur, adipiscing elit a per.'),
	('Violeta Santos', 'Lorem ipsum dolor sit amet consectetur, adipiscing elit fames laoreet arcu, massa ut parturient aliquet.'),
	('Jairo Rondon', 'Lorem ipsum dolor sit, amet.'),
	('Francia Rondon', 'Lorem ipsum dolor sit amet, consectetur adipiscing.')

]


cursor.executemany("INSERT INTO LEADS_NOMBRE_TELEFONO VALUES(NULL,?,?)", telefonos)
cursor.executemany("INSERT INTO LEADS_NOMBRE_EMAIL VALUES(NULL,?,?)", emails)
cursor.executemany("INSERT INTO LEADS_NOMBRE_NOTA VALUES(NULL,?,?)", notas)

conex.commit()
conex.close()
