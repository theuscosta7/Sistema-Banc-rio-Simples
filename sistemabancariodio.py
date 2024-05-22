saldo = 0
LIMITE_SAQUE = 3

while True:

    opcao = input("""

==============================
            MENU
==============================
                  
        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [0] - Sair

==============================
""")

    if opcao == "1":
        print("Informar valor do depósito: R$ ")
        deposito = float(input())
        if deposito > 0:
            saldo += deposito
            print(f"O valor de R$ {deposito:.2f} foi realizado com sucesso!")
        else:
            print("Valor invalido para depósito!")

    elif opcao == "2":
        print(f"Informar valor do saque: R$ ")
        saque = float(input())
        if saque > 0:
            saldo -= saque
            print("O valor de R$ {saque:.2f} foi realizado com sucesso!")
        else:
            print("Saque indísponivel. Limite insuficiente!")

    elif opcao == "3":
        print("=== EXTRATO CONTA ===")
        print(f"Saldo: {saldo:.2f}")

    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente!")
