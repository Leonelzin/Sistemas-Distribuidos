#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 09/05/2023 

import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta em que o servidor está escutando

# Cria um objeto de socket UDP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem = input('Digite a mensagem que deseja inverter: ')
    cliente_socket.sendto(mensagem.encode(), (HOST, PORT))
    dados, endereco_servidor = cliente_socket.recvfrom(1024)
    mensagem_invertida = dados.decode()
    print(f'Mensagem invertida: {mensagem_invertida}')
