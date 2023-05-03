#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 03/05/2023 

import socket

HOST = '127.0.0.1' # endereço IP do servidor
PORT = 8080 # porta a ser usada

# cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # associa o socket ao endereço e porta
    s.bind((HOST, PORT))
    # define o número máximo de conexões pendentes
    s.listen()
    print('Servidor iniciado...')
    # aguarda uma conexão
    conn, addr = s.accept()
    with conn:
        print('Conexão estabelecida por', addr)
        while True:
            # recebe a mensagem do cliente
            data = conn.recv(1024)
            if not data:
                break
            # apresenta a mensagem no console do servidor
            print('Mensagem recebida:', data.decode())
