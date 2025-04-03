#Faça um programa que leia três notas de um aluno, armazene em uma lista e calcule a média dessas notas, imprima a média.

notas = []

for i in range(3):
    nota = float(input('digite a nota: '))
    notas.append(nota)

média = ((notas[0] + notas[1] + notas[2]) / 3)

print(f'a média é: {média}')