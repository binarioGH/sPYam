#-*-coding: utf-8-*-
import smtplib
import subprocess
import getpass
def send_mail(usr, psw, msg, mailist, service):
	server = smtplib.SMTP(service)
	server.starttls()
	try:
		server.login(usr, psw)
	except Exception as e:
		print("hubo un error en el inicio de secion.")
		exit()
	for mail in mailist:
		try:
			server.sendmail(usr, mail, msg)
		except Exception as e:
			print("no se le pudo mandar el mensaje a {}".format(mail))
	server.quit()



if __name__ == '__main__':
	subprocess.call(["cmd.exe","/c","cls"])
	print("debes de tener 2 archivos de texto, uno con una lista")
	print("de correos que esten cada uno en una linea distinta y un archivo")
	print("con el mensaje que desea mandar.")
	print("")
	getpass.getpass("presiona enter para continuar...")
	subprocess.call(["cmd.exe","/c","cls"])
	user = str(input("introduzca su correo electronico: "))
	passw = getpass.getpass("introduzca su clave: ")
	spamlist = str(input("intrduzca la ruta del archivo .txt con la lista de correos: "))
	fmsg = str(input("intrduzca la ruta de un archivo .txt con el mensaje: "))
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
	ghmail = str(input("si quieres usar hotmail pon 'h' y 'g' para gmail: "))	

	if ghmail == 'g':
		send_mail(user, passw, msg, spamlist, 'smtp.gmail.com:587')
	elif ghmail == 'h':
		send_mail(user, passw, msg, spamlist, 'smtp.live.com:25')
	
