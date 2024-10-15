def exibir_menu():
    print(''' 
              [0] - Sair do programa
              [1] - Verificar maioridade
              [2] - Calcular IMC.\n''')
    
    
def verificar_maioridade(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."
    
calcular_imc = lambda peso, altura: peso/(altura**2)

