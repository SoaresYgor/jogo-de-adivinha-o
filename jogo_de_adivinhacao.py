from random import randint

print('**************************************')
print('Seja bem vindo ao jogo de adivinhação!')
print('**************************************')

# o \n é um caracter de escape, utilizado para quebra de linha
print('\n')

numero_secreto = randint(1, 10)
numero_escolhido = 0

while numero_secreto != numero_secreto:
    numero_escolhido = int(input('Escolha um número de 1 a 10: '))

if numero_escolhido != numero_secreto:
    print('\n')
    print('Escolha errada!')
    print('Tente novamente!')
    print('\n')


print(f'Parabéns! Você descobriu que o número secreto era o {numero_secreto}!')
print('\n')
