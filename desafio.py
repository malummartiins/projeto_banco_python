import textwrap


def menu():
    menu = """\n
    ================= MENU =============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito: R$ {valor:.2f} \n"
        print ("--  Depósito realizado com sucesso -- ")
            
    else:
        print ("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print ("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print ("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print ("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque: R$ {valor:.2f}\n "
        numero_saques += 1
        print (" -- Saque realizado com sucesso! -- ")

    else:
        print ("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n ============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques  = 0
    usuarios = []
    contas = []
    

    while True:

        opcao = input (menu)

        if opcao == "d":
            valor = float (input("Informe o valor do depósito: "))

            saldo, extrato = depositar (saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar (
                 saldo = saldo,
                 valor = valor,
                 extrato = extrato,
                 limite = limite,
                 numero_saques = numero_saques,
                 limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato (saldo, extrato=extrato)
        
        elif opcao == "q":
                break

        else:
                print("Operação inválida, por favor, selecione novamente a operação desejada.")