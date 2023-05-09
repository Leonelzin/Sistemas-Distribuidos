#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 09/05/2023 

import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta em que o servidor irá escutar
BUFFER_SIZE = 1024  # Tamanho máximo do buffer de recepção

# Cria um objeto de socket UDP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereço e a porta em que o servidor irá escutar
servidor_socket.bind((HOST, PORT))
print(f'Servidor escutando em {HOST}:{PORT}...')

# Loop infinito que aguarda mensagens dos clientes e envia de volta a string invertida
while True:
    dados, endereco_cliente = servidor_socket.recvfrom(BUFFER_SIZE)
    mensagem = dados.decode()
    mensagem_invertida = mensagem[::-1]
    servidor_socket.sendto(mensagem_invertida.encode(), endereco_cliente)
    print(f'Mensagem recebida: {mensagem}. Mensagem enviada: {mensagem_invertida}')
