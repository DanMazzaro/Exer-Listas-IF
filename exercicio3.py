# Faça um programa que leia 15 números inteiros digitados pelo usuário e armazene-os em uma lista. Armazene os números pares na lista PAR e os números IMPARES na lista IMPAR. No final mostre as três listas.

nT = []
nI = []
nP = []

for i in range(15):
    usu = int(input('digite 15 numeros: '))
    nT.append(usu)
    if usu % 2 ==0:
        nP.append(usu)
    elif usu % 2 >= 1:
        nI.append(usu)

print(f'os 15 numeros são: {nT}')
print(f'os impares são: {nI}')
print(f'os pares são: {nP}')
