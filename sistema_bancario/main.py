LIMITE = 500
LIMITE_DIARIO = 3

def deposito(num, saldo, extrato):
    if num > 0:
        saldo += num
        extrato += f"Depósito de R$ {num:.2f}\n"
    else:
        print("Digite um valor válido!\n")
    return saldo, extrato

def saque(num, saldo, extrato, num_saque):
    if num > saldo:
        print("O valor do saque deve ser menor que o saldo atual!\n")
    elif num > LIMITE:
        print("O valor deve ser menor que o seu limite!\n")
    elif num_saque >= LIMITE_DIARIO:
        print("Você já excedeu o seu limite diário de saque!\n")
    elif num > 0:
        saldo -= num
        extrato += f"Saque de R$ {num:.2f}\n"
        num_saque += 1
    else:
        print("Digite um valor válido!\n")
    return saldo, extrato, num_saque

def mostrar_extrato(extrato, saldo):
    print("<< SEU EXTRATO >>")
    print("Você não fez movimentações." if not extrato else extrato)
    print(f"Seu saldo é R$ {saldo:.2f}.\n")

saldo = 0
extrato = ""
num_saque = 0

while True:
    opcao = int(input("""<< MENU >>\n\n[1] Depósito\n[2] Saque\n[3] Extrato\n[4] Sair\n\nEscolha uma opção: """))

    if opcao == 1:
        num = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(num, saldo, extrato)
    elif opcao == 2:
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, extrato, num_saque = saque(valor_saque, saldo, extrato, num_saque)
    elif opcao == 3:
        mostrar_extrato(extrato, saldo)
    elif opcao == 4:
        print("Até a próxima :)\n")
        break
    else:
        print("Digite uma opção válida!\n")
