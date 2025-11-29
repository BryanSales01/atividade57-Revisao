# Leia idades de várias pessoas até que o usuário digite -1.
# Calcule a média das idades somente dos maiores de 18 anos.
# Se não houver maiores de idade, exiba mensagem apropriada.

idades = []
idade = int(input("Digite a idade que você deseja tirar a média(Digite -1 para parar: ): "))

while idades != -1:
    idade = int(input("Digite a idade que você deseja tirar a média(Digite -1 para parar: ): "))
    if idade >= 18:
        idades.append(idade)

    elif idade == -1:
        break

    else:
        print("Nenhum maior de idade identificado")
        continue

soma = sum(idades)
media = soma / len(idades)

print(media)
