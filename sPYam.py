#-*-coding: utf-8-*-
import smtplib
import subprocess
import getpass
if __name__ == '__main__':
	subprocess.call(["cmd.exe","/c","cls"])
	print("de momento esto solo funciona con gmail.")
	print("debes de tener 2 archivos de texto, uno con una lista")
	print("de correos que esten cada uno en una linea distinta y un archivo")
	print("con el mensaje que desea mandar.")
	user = str(raw_input("introduzca su correo electronico: "))
	passw = getpass.getpass("introduzca su clave: ")
	spamlist = str(raw_input("intrduzca la ruta del archivo .txt con la lista de correos: "))
	fmsg = str(raw_input("intrduzca la ruta de un archivo .txt con el mensaje: "))
	mails = []
	spamfile = open(spamlist, 'r')
	for line in spamlist:
		mails.append(line)
	spamfile.close()
	rmsg = open(fmsg, 'r')
	msg = str()
	for line in fmsg:
		msg += line
	rmsg.close()
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	try: 
		server.login(user, passw)
	except Exception as e:
		print("hubo un problema en el login")
		exit()
	for mail in mails:
		try:
			server.sendmail(user, mail, msg)
		except Exception as e:
			print("hubo un error y no se puedo enviar el correo a {}".format())
	server.quit()




