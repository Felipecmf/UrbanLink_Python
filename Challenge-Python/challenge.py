import time

pontos = 0
qtd_pontos = 0
bilhetes = 0


def menu():
    print("\n - - - - | MENU | - - - -")
    print("[1] Consultar pontos")
    print("[2] Adicionar pontos")
    print("[3] Atualizar pontos")
    print("[4] Excluir pontos")
    print("[5] Conversões")
    print("[0] Sair \n")


print(" - - - - - - - - - - - - - - - ")
print("|     U R B A N   L I N K     |")
print(" - - - - - - - - - - - - - - - ")


menu()
opcao = input("Escolha uma opção\n")

while opcao != "0":

    if opcao == "1":
        print(f"Pontos acumulados: \n{int(pontos)}")

    elif opcao == "2":
        qtd_pontos = float(input("Digite a quantidade de pontos que você deseja adicionar:\n"))

        while qtd_pontos <= 0 or (qtd_pontos % 1) != 0:
            qtd_pontos = float(input("Digite um valor inteiro e maior que zero:\n"))

        pontos += qtd_pontos
        print("Pontos adicionados!")
        qtd_pontos = 0


    elif opcao == "3":
        qtd_pontos = float(input("Digite a nova quantidade do seu saldo de pontos:\n"))

        while qtd_pontos <= 0 or (qtd_pontos % 1) != 0:
            qtd_pontos = float(input("Digite um valor inteiro e maior(ou igual) a zero:\n"))
            
        pontos = qtd_pontos
        print("Pontos atualizados!")
        qtd_pontos = 0


    elif opcao == "4":
        
        if pontos > 0:

            qtd_pontos = float(input("Digite a quantidade de pontos que você deseja excluir: \n"))

            while qtd_pontos > pontos or (qtd_pontos % 1) != 0:
                qtd_pontos = float(input("O valor deve ser inteiro e não pode ser maior que o seu saldo de pontos agora!: \n Digite novamente \n"))

            print("Pontos excluídos.")
            qtd_pontos = 0

        else:
            print("Não é possível excluir pontos, pois não há saldo.")


    elif opcao == "5":
        bilhetes = int(pontos*0.05)
        print(f"Quantidade de pontos acumuldados:{int(pontos)} \nConversão em bilhetes: \n{bilhetes}")
        
        
    else:
        print("Opção inválida, tente novamenete.\n")


    menu()
    opcao = input("Escolha uma opção\n")


print("Saindo do sistema...")
time.sleep(2)