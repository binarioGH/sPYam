#-*-coding: utf-8-*-
from smtplib import SMTP
from sys import argv


def smap(mailist, msg, usr, psw):
	pass
def unabomber(mailist, msg, usr, psw, rge):
	try:
		server.login(usr, pasw)
	except Exception as e:
		print("No se ha podido iniciar seción:\n{}".format(e))
		exit()
	else:
		for mail in mailist:
			for num in rge:
				server.sendmail(usr, mail, msg)

def h():	
	print("Guía de {}:".format(argv[0]))
	print("\nDe momento solo puedes enviar correos desde una cuenta de gmail.\n")
	print("--unabomber:\nSirve para activar el modo mail bomber (Sí, como en los 90's)\n")
	print("-u:\nSirve para establecer el usuario que usarás (correo electronico).\n")
	print("-p:\nEstablecer la contraseña de tu correo.\n")
	print("-msg:\nEstablecer el archivo donde está el mensaje de tu correo.\n")
	print("-mail:\nAñadir un correo a la lista de blancos.\n")
	print("-mfile:\nEstablecer archivo de correos.\n")
	print("\n\nEsta bandera es solo si está activado el modo unabomber:")
	print("-r:\nEstablecer la cantidad de veces que se enviará ")
if __name__ == '__main__':
	if len(argv) <= 1:
		print("{} necesita más argumentos para funcionar, usa:\n{} -h para ver las opciones.".format(argv[0],argv[0]))
	else:
		mails = []
		count = 0
		unabomber = False
		user, passw, msgfile =  str(), str(), str()
		rnge = str()
		for arg in argv:
			if arg[0] != "-":
				count += 1
				continue
			if arg == "--unabomber":
				unabomber = True
			elif arg == "-h":
				h()
				exit()
			elif arg == "-u":
				user = argv[count + 1]
			elif arg == "-p":
				passw = argv[count + 1]
			elif arg == "-msg":
				msgfile = argv[count + 1]
			elif arg == "-mfile":
				mailfile = open(argv[count + 1], "r")
				for mail in mailfile:
					mails.append(mail)
			elif arg == "-mail":
				mails.append(argv[count + 1])
			elif arg == "-r":
				try:
					rnge = int(argv[count + 1])
				except:
					print("{} no es un numero entero".format(argv[count + 1]))
					exit()
			else:
				print("No se reconoce la bandera '{}'".format(arg))
				exit()
			count += 1
		try:
			server = SMTP('smtp.gmail.com:587')
			server.starttls()
		except Exception as e:
			print("problemas al iniciar el servidor:\n{}".format(e))
			exit()
		msgstr = str()
		try:
			file = open(msg, "r")
		except:
			print("no se ha podido encontrar el siguiente archivo:\n{}".format(msg))
			exit()
		else:
			for line in file:
			    #Se que esto puede afectar el rendimiento en archivos grandes, pienso cambiarlo.
			    msgstr += line
		if user != "" and passw and "":
			