
from opc.funciones import *


while True:

	print('\tBase de Datos')
	print('1. Consultar.')
	print('2. Actualizar.')
	print('3. Dar de Alta.')
	print('4. Dar de Baja.')
	print('5. Salir.')

	print(' ')
	opc = int(input('Opción: '))
	print(' ')


	if (opc == 1):
		name = input('Nombre: ')
		consulta(name)

	elif (opc == 2):
		name = input('Nombre: ')
		n_tlf = input('Nuevo Telf: ')
		n_mail = input('Nuevo Email: ')
		n_nota = input('Nueva Nota: ')
		actualizar(name, n_tlf, n_mail, n_nota)

	elif (opc == 3):
		name = input('Nombre: ')
		tlf = input('Telf: ')
		mail = input('Email: ')
		nota = input('Nota: ')
		alta(name, tlf, mail, nota)

	elif (opc == 4):
		name = input('Nombre: ')
		baja(name)

	elif (opc == 5):
		break

