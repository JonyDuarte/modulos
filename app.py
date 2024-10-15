from modulo import *

# programa principal
if __name__ == "__main__":
    while True:
        nome = input("Informe seu nome: ")
        exibir_menu()
        opcao = input("Opção desejada: ")

        match opcao: 
            case "0":
                break
            case "1":
                idade = int(input("Informe sua idade: "))
                print(verificar_maioridade(nome, idade))
                continue
            case "2":
                peso = float(input("Informe o peso em kg: ").replace(",","."))
                altura = float(input("Informe a altura em metros: ").replace(",","."))
                print(calcular_imc(peso, altura))
                continue
            case _: 
                print("Opção Inválida.") 
