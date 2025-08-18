menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == '1':
        print("Menu [1] Depósito\n")
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 0:
            deposito = round(deposito,3)
            saldo += deposito
            extrato += f'Depósito = R$ {deposito:.2f}\n'
            print(f"Deposito de R$ {deposito:.2f} realizado com sucesso")
        else:
            print("Somente são permitidos depósitos maiores do que R$ 0,00. Por favor, tente novamente.")

    elif opcao == '2':
        print("Menu [2] Saque\n")
        print(f"Quantidade de saques dispóníveis, {3-numero_saques}\n")
        saque = float(input("Digite o valor que deseja sacar: "))
        saque = round(saque,3)

        if saque > limite:
            print("Tentativa de saque com valor superior ao limite (limite = R$ 500,00).\n Tente novamente, com um valor menor ou igual ao limite")
        elif numero_saques >= LIMITE_SAQUES:
            print("Não foi possível completar a operação.\nVocê atingiu o número máximo de saques por dia (3), retorne amanhã.")
        else:
            if saldo >= saque:
                numero_saques += 1
                saldo -= saque
                extrato += f'Saque = R$ {saque:.2f}\n'
                print(f"Saque de R$ {saque:.2f} realizado com sucesso")

            else:
                print(f"Saldo insuficiente para realizar a operação desejada.\nTentativa de saque = R$ {saque}\nSaldo em conta = R$ {saldo}")
    
    elif opcao == '3':
        print("Menu [3] Extrato\n")

        if extrato:
            print(extrato)
            print(f"\nSaldo atual = R$ {saldo}")
        else:
            print("Não foram realizadas movimentações.")
    elif opcao == '0':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

