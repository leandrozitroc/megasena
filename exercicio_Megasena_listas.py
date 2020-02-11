from random import sample
from random import choice
from time import sleep
print('=-=' * 20)
print('MEGA SENA')
print('=-=' * 20)
total = 0
n = int(input('Quantos jogos deseja que eu gere , humano ? '))
print(f'Os jogos que voce pode ganhar na mega sena são :')
for c in range(n):
    lista = sorted(sample(range(1, 60), 6))
    print(f'Jogo: {c + 1}  ***{lista}***')
    sleep(1)
print('=-=' * 20)
print('=-=' * 20)

