#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 03/05/2023 

import socket

HOST = '127.0.0.1' # endereço IP do servidor
PORT = 8080 # porta a ser usada

# cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # conecta ao servidor
    s.connect((HOST, PORT))
    # entra com a mensagem
    message = input('Digite a mensagem a ser enviada: ')
    # envia a mensagem para o servidor
    s.sendall(message.encode())
