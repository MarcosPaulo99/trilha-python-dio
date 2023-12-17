conta_normal = 1
conta_universitaria = 2

conta_normal
conta_universitaria = int(input("informe sua idade: "))


saldo = 2000
saque = 3000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com suceddo!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque !")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("saldo insuficiente!")
else:
    print("O sistema não reconheceu seu tipo de conta!")
