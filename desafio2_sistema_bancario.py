import textwrap

def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar conta
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        valor = round(valor,3)
        saldo += valor
        extrato += f'Depósito = R$ {valor:.2f}\n'
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso")
    else:
        print("Somente são permitidos depósitos maiores do que R$ 0,00. Por favor, tente novamente.")
    return saldo,extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor = round(valor,3)

    if valor > limite:
        print("Tentativa de saque com valor superior ao limite (limite = R$ 500,00).\n Tente novamente, com um valor menor ou igual ao limite")
    elif numero_saques >= limite_saques:
        print("Não foi possível completar a operação.\nVocê atingiu o número máximo de saques por dia (3), retorne amanhã.")
    else:
        if saldo >= valor and valor > 0:
            numero_saques += 1
            saldo -= valor
            extrato += f'Saque = R$ {valor:.2f}\n'
            print(f"Saque de R$ {valor:.2f} realizado com sucesso")

        else:
            print(f"Saldo insuficiente para realizar a operação desejada.\nTentativa de saque = R$ {valor}\nSaldo em conta = R$ {saldo}")
    return saldo,extrato,numero_saques

def exibir_extrato(saldo,/,*,extrato):
    if extrato:
        print(extrato)
        print(f"\nSaldo atual = R$ {saldo}")
    else:
        print("Não foram realizadas movimentações.")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nUsuário já cadastrado na base de dados!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data e nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário cadastrao com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [ usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado!\nCadastre o usuário ou confira se digitou o cpf corretamente.")


def filtrar_conta(numero_conta,numero_agencia,contas):
    contas_filtradas = [ conta for conta in contas if (conta["numero_conta"] == numero_conta and conta["numero_agencia"] == numero_agencia)]
    return contas_filtradas[0] if contas_filtradas else None
def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"""
Agência: \t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
            print("=" * 60)
            print(textwrap.dedent(linha))
    else:
        print("Não existem contas cadastradas!")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            print("Menu [1] Depósito\n")
            valor = float(input("Digite o valor que deseja depositar: "))
            
            saldo, extrato = depositar(saldo,valor,extrato)
        elif opcao == '2':
            print("Menu [2] Saque\n")
            print(f"Quantidade de saques dispóníveis, {LIMITE_SAQUES-numero_saques}\n")
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato,numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )
    
        elif opcao == '3':
            print("Menu [3] Extrato\n")
            exibir_extrato(saldo,extrato=extrato)
        elif opcao == '0':
            break
        elif opcao == '4':
            print("Menu [4] Criação de novo usuário\n")
            criar_usuario(usuarios)
        elif opcao == '5':
            print("Menu [5] Criação de nova conta\n")

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == '6':
            print("Menu [6] Listagem de contas cadastradas\n")
            listar_contas(contas)
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()