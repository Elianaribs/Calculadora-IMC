"""calculo_imc Eliana Ribeiro da Silva
"""

"""
Declaração de funções
"""


def calculo_base():
    return peso / (altura * 2)


nome = str(input("Qual seu nome"))
peso = float(input("Digite o seu peso em kg:"))
altura = float(input("Digite sua altura em metros:"))

imc = calculo_base()

print(f"O seu imc é:", imc)

if imc < 18.00:
    print(f'{nome},você está abaixo do peso')
elif imc <= 25:
    print(f'{nome},você está no peso ideal')
elif 25.1 <= imc <= 40:
    print(f'{nome},você está com sobrepeso')
else:
    print(f'{nome},você está com obesidade')
