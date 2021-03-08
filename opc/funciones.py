
import sqlite3 as sql

def consulta(name):

	nombre = [(name)]

	conex = sql.connect('../BD_Test/BD.env')
	cursor = conex.cursor()

	cursor.execute("SELECT * FROM LEADS_NOMBRE_TELEFONO WHERE NOMRE=(?)",nombre)
	info = cursor.fetchone()
	print('Telefono: ',info[-1])

	cursor.execute("SELECT * FROM LEADS_NOMBRE_EMAIL WHERE NOMRE=(?)",nombre)
	info = cursor.fetchone()
	print('Email: ',info[-1])

	cursor.execute("SELECT * FROM LEADS_NOMBRE_NOTA WHERE NOMRE=(?)",nombre)
	info = cursor.fetchone()
	print('Nota: ',info[-1])

	conex.commit()
	conex.close()

	print(' ')
	print(' ')



def actualizar(name, n_tlf, n_mail, n_nota):

	nombre = [(name)]


	conex = sql.connect('../BD_Test/BD.env')
	cursor = conex.cursor()


	info = cursor.execute("SELECT * FROM LEADS_NOMBRE_TELEFONO WHERE NOMRE=(?)", nombre).fetchone()
	cursor.execute("UPDATE LEADS_NOMBRE_TELEFONO SET TELEFONO=(?) WHERE TELEFONO=(?)", (n_tlf, info[-1]))


	info = cursor.execute("SELECT * FROM LEADS_NOMBRE_EMAIL WHERE NOMRE=(?)", nombre).fetchone()
	cursor.execute("UPDATE LEADS_NOMBRE_EMAIL SET EMAIL=(?) WHERE EMAIL=(?)", (n_mail, info[-1]))


	info = cursor.execute("SELECT * FROM LEADS_NOMBRE_NOTA WHERE NOMRE=(?)", nombre).fetchone()
	cursor.execute("UPDATE LEADS_NOMBRE_NOTA SET NOTAS=(?) WHERE NOTAS=(?)", (n_nota, info[-1]))


	conex.commit()
	conex.close()

	print('¡Listo!')
	print(' ')
	print(' ')



def alta(name, tlf, mail, nota):

	conex = sql.connect('../BD_Test/BD.env')
	cursor = conex.cursor()


	cursor.execute("INSERT INTO LEADS_NOMBRE_TELEFONO VALUES(NULL,?,?)", (name, tlf))
	cursor.execute("INSERT INTO LEADS_NOMBRE_EMAIL VALUES(NULL,?,?)", (name, mail))
	cursor.execute("INSERT INTO LEADS_NOMBRE_NOTA VALUES(NULL,?,?)", (name, nota))


	conex.commit()
	conex.close()

	print('¡Listo!')
	print(' ')
	print(' ')



def baja(name):

	nombre = [(name)]

	conex = sql.connect('../BD_Test/BD.env')
	cursor = conex.cursor()


	cursor.execute("DELETE FROM LEADS_NOMBRE_TELEFONO WHERE NOMRE=(?)", nombre)
	cursor.execute("DELETE FROM LEADS_NOMBRE_EMAIL WHERE NOMRE=(?)", nombre)
	cursor.execute("DELETE FROM LEADS_NOMBRE_NOTA WHERE NOMRE=(?)", nombre)


	conex.commit()
	conex.close()

	print('¡Listo!')
	print(' ')
	print(' ')