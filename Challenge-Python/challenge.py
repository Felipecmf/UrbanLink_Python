import time

pontos = 0
qtd_pontos = 0
bilhetes = 0
historico = []
historico_adicionados = []
historico_atualizados = []
historico_excluidos= []

lista_menu = (
    "[1] Consultar pontos",
    "[2] Adicionar pontos",
    "[3] Atualizar pontos",
    "[4] Excluir pontos",
    "[5] Conversões em bilhetes",
    "[6] Consultar histórico de tarefas",
    "[0] Sair")

def menu():

    print("\n - - - - - - | MENU | - - - - - - -")

    for item in lista_menu:
        print(item)

    return input("Escolha uma opção: ")


def ler_inteiro(msg):

    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros.")


def consultar_pontos():

    global pontos

    print("\nConsultando...")
    time.sleep(1.5)

    print("------------------------------------")
    print(f"Pontos acumulados: {pontos}")
    print("------------------------------------")

    historico.append("Consulta de pontos")


def adicionar_pontos():

    global pontos

    print("----------------------------------------------------")
    qtd_pontos = ler_inteiro("Digite a quantidade de pontos que deseja adicionar:\n")

    while qtd_pontos <= 0:
        qtd_pontos = ler_inteiro("Digite um valor inteiro maior que zero:\n")

    pontos += qtd_pontos
    historico_adicionados.append(qtd_pontos)
    print("\nAdicionando os pontos...")
    time.sleep(1.5)
    print("Pontos adicionados com sucesso!")
    print("----------------------------------------------------")
    historico.append("Adição de pontos")


def atualizar_pontos():

    global pontos

    print("----------------------------------------------")
    qtd_pontos = ler_inteiro("Digite a nova quantidade do saldo de pontos:\n")

    while qtd_pontos < 0:
        qtd_pontos = ler_inteiro("Digite um valor inteiro maior ou igual a zero:\n")

    pontos = qtd_pontos
    historico_atualizados.append(qtd_pontos)
    print("\nAtualizando os pontos...")
    time.sleep(1.5)
    print("Pontos atualizados com sucesso!")
    print("----------------------------------------------")
    historico.append("Atualização de pontos")


def excluir_pontos():

    global pontos

    if pontos > 0:

        print("---------------------------------------------------")
        qtd_pontos = ler_inteiro("Digite a quantidade de pontos que deseja excluir:\n")

        while qtd_pontos < 0 or qtd_pontos > pontos:
            qtd_pontos = ler_inteiro("Valor inválido! Não pode ser negativo nem maior que o saldo:\n")

        pontos -= qtd_pontos
        historico_excluidos.append(qtd_pontos)
        print("\nExcluindo os pontos...")
        time.sleep(2)
        print("Pontos excluídos com sucesso!")
        print("---------------------------------------------------")
        historico.append("Exclusão de pontos")

    else:
        print("Você não possui pontos para excluir.")


def converter_bilhetes():

    global bilhetes

    print("------------------------------------")
    bilhetes = int(pontos * 0.05)
    print("\nFazendo o cálculo da conversão...")
    time.sleep(1.5)
    print(f"Pontos acumulados: {pontos}")
    print(f"Conversão em bilhetes: {bilhetes}")

    print("------------------------------------")
    historico.append("Consulta de bilhetes")


def consultar_historico():

    print("\nBuscando o histórico...")
    time.sleep(1.5)
    print("\n- - - HISTÓRICO DE TAREFAS(DA MAIS ANTIGA ATÉ A MAIS RECENTE): - - -\n")

    for item in historico:
        print(f"->{item}")

    print(f"\nTotal de atividades realizadas:\n{len(historico)}")
    historico.append("Consulta do Histórico de Tarefas")

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

    if len(historico_adicionados) > 0:

        print("NA ADIÇÃO DE PONTOS:")
        print(f"Maior valor inserido: {max(historico_adicionados)}")
        print(f"Menor valor inserido: {min(historico_adicionados)}")
        print(f"Média geral dos pontos adicionados: {(sum(historico_adicionados))/len(historico_adicionados):.2f}")

    else:
        print("Ainda não foi feita nenhuma adição de pontos.")

    if len(historico_atualizados) > 0:

        print("----------")
        print("NA ATUALIZAÇÃO DE PONTOS:")
        print(f"Maior valor inserido: {max(historico_atualizados)}")
        print(f"Menor valor inserido na atualização de pontos: {min(historico_atualizados)}")
        print(f"Média geral dos pontos inseridos: {(sum(historico_atualizados))/len(historico_atualizados):.2f}")

    else:
        print("Ainda não foi feita nenhuma atualização de pontos.")
    
    if len(historico_excluidos) > 0:

        print("----------")
        print("NA EXCLUSÃO DE PONTOS:")
        print(f"Maior valor inserido: {max(historico_excluidos)}")
        print(f"Menor valor inserido: {min(historico_excluidos)}")
        print(f"Média geral dos pontos excluídos: {(sum(historico_excluidos))/len(historico_excluidos):.2f}")

    else:
        print("Ainda não foi feita nenhuma exclusão de pontos.")

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

print(" - - - - - - - - - - - - - - - - - - - ")
print("|         U R B A N   L I N K         |")
print(" - - - - - - - - - - - - - - - - - - - ")

opcao = menu()

while opcao != "0":

    match opcao:

        case "1":
            consultar_pontos()

        case "2":
            adicionar_pontos()

        case "3":
            atualizar_pontos()

        case "4":
            excluir_pontos()

        case "5":
            converter_bilhetes()

        case "6":
            consultar_historico()

        case _:
            print("Opção inválida! Tente novamente.")

    opcao = menu()

print("\nSaindo do sistema...")
time.sleep(2)