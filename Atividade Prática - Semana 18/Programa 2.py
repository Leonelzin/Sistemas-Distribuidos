#Curso de Engenharia de Software - UniEVANGÉLICA 
#Disciplina de Sistemas Distribuidos 
#Dev: Douglas Leonel de Almeida
#DATA: 21/06/2023 

import Pyro4

def main():
    # Obter a referência do servidor
    number_adder = Pyro4.Proxy("PYRONAME:number.adder")

    # Solicitar os números do usuário
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Chamar o método add_numbers do servidor
    result = number_adder.add_numbers(num1, num2)

    # Exibir o resultado
    print("Resultado da soma:", result)

if __name__ == "__main__":
    main()
