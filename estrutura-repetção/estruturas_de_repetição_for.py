# Pega o Texto e separa as vogais.
texto = input("Informe um texto:")
texto = ""
VOGAIS = "AEIOU"


# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha
    print("executa no final do laço")


# exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
