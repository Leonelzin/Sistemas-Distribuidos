#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 22/06/2023 

import Pyro4

def main():
    # Obter a referência do servidor
    string_inverter = Pyro4.Proxy("PYRONAME:string.inverter")

    # Solicitar a mensagem do usuário
    message = input("Digite uma mensagem para inverter: ")

    # Chamar o método invert_string do servidor
    inverted_message = string_inverter.invert_string(message)

    # Exibir o resultado
    print("Mensagem invertida:", inverted_message)

if __name__ == "__main__":
    main()
