"""
import random

cpf_aleatorio = ''
for i in range (11):
    cpf_aleatorio += str(random.randint(0,9))

print (cpf_aleatorio)



tupla = ''
print(len(tupla))



def soma(numero1,numero2):
    soma_total = numero1 + numero2
    return soma_total

def execute(funcao,*args):
    return funcao(*args)

x = execute(soma, 2,6)
print(x)
"""

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },

]

novos_produtos =[

    {**produto, 'preço' : produto['preço'] * 1.30}
    if produto['preço'] > 15 else {**produto} 
    for produto in produtos 
]

print(*novos_produtos, sep='\n') #Tem que desempacotar
print()