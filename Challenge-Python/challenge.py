import time

pontos = 0
qtd_pontos = 0
bilhetes = 0
historico = []
lista_menu = ("[1] Consultar pontos","[2] Adicionar pontos","[3] Atualizar pontos","[4] Excluir pontos",
              "[5] Conversões em bilhetes","[6] Consultar histórico de tarefas","[0] Sair")

def menu():
    print("\n - - - - - - | MENU | - - - - - - -")
    for item in lista_menu:
        print (item)
    return input("Escolha uma opção: ")

def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros.")


print(" - - - - - - - - - - - - - - - - - - - ")
print("|         U R B A N   L I N K         |")
print(" - - - - - - - - - - - - - - - - - - - ")

opcao = menu()

while opcao != "0":

    match opcao:

        case "1":
            print("------------------------------------")
            print(f"Pontos acumulados: {pontos}")
            print("------------------------------------")
            historico.append("Consulta de pontos")

        case "2":
            print("----------------------------------------------------")
            qtd_pontos = ler_inteiro("Digite a quantidade de pontos que deseja adicionar:\n")

            while qtd_pontos <= 0:
                qtd_pontos = ler_inteiro("Digite um valor inteiro maior que zero:\n")

            pontos += qtd_pontos
            print("Pontos adicionados com sucesso!")
            print("----------------------------------------------------")
            historico.append("Adição de pontos")

        case "3":
            print("----------------------------------------------")
            qtd_pontos = ler_inteiro("Digite a nova quantidade do saldo de pontos:\n")

            while qtd_pontos < 0:
                qtd_pontos = ler_inteiro("Digite um valor inteiro maior ou igual a zero:\n")

            pontos = qtd_pontos
            print("Pontos atualizados com sucesso!")
            print("----------------------------------------------")
            historico.append("Atualização de pontos")

        case "4":
            if pontos > 0:
                print("---------------------------------------------------")
                qtd_pontos = ler_inteiro("Digite a quantidade de pontos que deseja excluir:\n")

                while qtd_pontos < 0 or qtd_pontos > pontos:
                    qtd_pontos = ler_inteiro("Valor inválido! Não pode ser negativo nem maior que o saldo:\n")

                pontos -= qtd_pontos
                print("Pontos excluídos com sucesso!")
                print("---------------------------------------------------")
                historico.append("Exclusão de pontos")

            else:
                print("Você não possui pontos para excluir.")

        case "5":
            print("------------------------------------")
            bilhetes = int(pontos * 0.05)
            print(f"Pontos acumulados: {pontos}")
            print(f"Conversão em bilhetes: {bilhetes}")
            print("------------------------------------")
            historico.append("Consulta de bilhetes")

        case "6":
            print("\n- - - HISTÓRICO DE TAREFAS(DA MAIS ANTIGA ATÉ A MAIS RECENTE): - - -\n")
            cont = 1

            for item in historico:
                print(f"{cont}º {item}")
                cont +=1
            historico.append("Consulta do Histórico de Tarefas")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

        case _:
            print("Opção inválida! Tente novamente.")

    opcao = menu()

print("\nSaindo do sistema...")
time.sleep(2)