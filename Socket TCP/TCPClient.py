from socket import *

serverName = '192.168.1.112'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Insira a frase em minúscula: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print(f'Do servidor: {modifiedSentence}')
clientSocket.close()
