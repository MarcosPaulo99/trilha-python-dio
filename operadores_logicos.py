saldo = 1000
saque = 150
limite = 200
conta_especial = True

# AND = PARA SER TRUE TUDO TEM QUE SER TRUE
# OR = PARA SER TRUE APENAS UM TEM QUE SER TRUE


# print(True and True)
# print(True and False)
# print(False and True)
# print(True or True)
# print(True or False)
# print(False or True)


saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

conta_normal_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo = conta_especial and saldo >= saque

exp_3 = conta_normal_saldo_suficiente or conta_especial_com_saldo
print(exp_3)
