# Faça um algoritmo que leia 30 valores do tipo inteiro digitados pelo usuário e armazene-os em
# uma lista. A seguir, o algoritmo deverá informar em forma de lista todos os números pares que
# existem na lista; o menor e o maior valor existente na lista; quantos dos valores da lista são
# maiores que a média desses valores.

lista_v = []
lista_p = []
lista_i = []
lista_me = []
lista_ma = []

for i in range(30):
    valores = int(input('digte um valor: '))
    lista_v.append(valores)

    if valores % 2 == 0:
        lista_p.append(valores)
    elif valores % 2 >= 1:
        lista_i.append(valores)




print(lista_v)
print(lista_p)
print(lista_i)
print(lista_ma)
