#!/usr/bin/python
#-*-coding: utf-8-*-
from smtplib import SMTP
from sys import argv

def text(msgfile):
	msgstr = str()
	try:
		file = open(msgfile, "r")
	except:
		print("no se ha podido abrir el siguiente archivo:\n{}".format(msg))
		exit()
	else:
		for line in file:
			msgstr += line
	file.close()
	return msgstr

def unabombermod(mailist, msg, usr, rge):
	for mail in mailist:
		for num in range(rnge):
			try:
				server.sendmail(usr, mail, msg)
			except Exception as e:
				print("No se ha podido enviar correo a: {}\n{}".format(mail,e))
			else:
				print("Correo enviado a: {}".format(mail))
def h():	
	print("Guía de {}:".format(argv[0]))
	print("\nDe momento solo puedes enviar correos desde una cuenta de gmail.\n")
	print("-u:\nSirve para establecer el usuario que usarás (correo electronico).\n")
	print("-p:\nEstablecer la contraseña de tu correo.\n")
	print("-msg:\nEstablecer el archivo donde está el mensaje de tu correo.\n")
	#print("-mail:\nAñadir un correo a la lista de blancos.\n")
	print("-mfile:\nEstablecer archivo de correos.\n")
	print("\n\nEsta bandera es solo si está activado el modo unabomber:")
	print("-r:\nEstablecer la cantidad de veces que se enviará (si no lo usas se mandará una vez). ")
	print("-gm:\nSi tu correo es de gmail debes de usar esta bandera.\n-hm:\nSi tu correo es de hotmail.")
if __name__ == '__main__':
	if len(argv) <= 1:
		print("{} necesita más argumentos para funcionar, usa:\n{} -h para ver las opciones.".format(argv[0],argv[0]))
	else:
		mails = []
		count = 0
		unabomber = False
		user, passw, msgfile =  str(), str(), str()
		rnge = 1
		gm, hm = False, False
		for arg in argv:
			if arg[0] != "-":
				count += 1
				continue
			if arg == "--unabomber":
				unabomber = True
			elif arg == "-gm":
				gm = True
			elif arg == "-hm":
				hm = True
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
			#elif arg == "-mail":
				#mails.append(argv[count + 1])
			elif arg == "-r":
				try:
					rnge = int(argv[count + 1])
				except:
					print("{} no es un numero entero.".format(argv[count + 1]))
					exit()  
			else:
				print("No se reconoce la bandera '{}'".format(arg))
				exit()
			count += 1
		if gm == True and hm == True:
			print("No se puede usar -gm y -hm al mismo tiempo.")
			exit()
		elif gm == True:
			smtpserver = 'smtp.gmail.com:587'
		elif hm == True:
			smtpserver = 'smtp.live.com:587'
		else:
			print("No se ha establecido si se usara gmail o hotmail.")
			exit()
		try:
			server = SMTP(smtpserver)
			server.starttls()
		except Exception as e:
			print("problemas al iniciar el servidor:\n{}".format(e))
			exit()
		try:
			server.login(user, passw)
		except Exception as e:
			print("No se ha podido iniciar seción:\n{}".format(e))
			exit()
		msgstr = text(msgfile)
		
		unabombermod(mails, msgstr, user, rnge)
		
			