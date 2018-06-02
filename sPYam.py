#-*-coding: utf-8-*-
from smtplib import SMTP
from sys import argv

if __name__ == '__main__':
	if len(argv) <= 1:
		print("{} necesita más argumentos para funcionar, usa:\n{} -h para ver las opciones".format(argv[0],argv[0]))
	else:
		count = 0
		unabomber = False
		multi = False
		for arg in argv:
			if arg[0] != "-":
				count += 1
				continue
			else:
				if unabomber == True and multi == True:
					print("No se puede usar '--unabomber' y '--multi' al mismo tiempo.")
					exit()
				if arg == "--unabomber":
					unabomber = True
				elif arg == "--multi":
					multi = True


