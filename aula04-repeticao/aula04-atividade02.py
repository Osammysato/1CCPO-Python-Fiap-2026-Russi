# Atividade 2: Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.
def verificar_notas(nota):
    while nota < 0 or  nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota

notaA = float(input("Digite a primeira nota: "))
notaA = verificar_notas(notaA)

notaB = float(input("Digite a segunda nota: "))
notaB = verificar_notas(notaB)

media = (notaA + notaB) / 2
print(media)