#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 09/05/2023 

#O código do cliente também será escrito em Python e utilizará a biblioteca de sockets para se conectar ao servidor e enviar mensagens de acordo com o protocolo definido acima. 

#Aqui está um exemplo básico de código de cliente que implementa o protocolo de comunicação:

import socket

# Definir a porta do servidor e o endereço de host
HOST = '127.0.0.1'
PORT = 12345

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket a um endereço e porta
client_socket.connect((HOST, PORT))

# Enviar uma mensagem de exemplo ao servidor
message = 'SEND_MESSAGE:alice:Hello, Alice!'
client_socket.sendall(message.encode('utf-8'))

# Recebe a resposta do servidor
response = client_socket.recv(1024).decode('utf-8')

# Processa a resposta do servidor
response_parts = response.split(':')
response_type = response_parts[0]
response_body = response_parts[1]

# Fecha o socket do cliente
client_socket.close()
