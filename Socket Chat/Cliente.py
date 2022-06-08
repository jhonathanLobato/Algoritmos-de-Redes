import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('192.168.1.106', 8888))

terminado = False
print("Digite 'gg' para encerrar o chat")

while not terminado:
	cliente.send(input('Mensagem: ').encode('UTF-8'))
	msg = cliente.recv(1024).decode('UTF-8')
	if msg == 'gg':
		terminado = True

	else:
		print(msg)

cliente.close()
