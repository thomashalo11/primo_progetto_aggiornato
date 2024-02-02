import random

primoNumero = random.randint(0, 5)
secondoNumero = random.randint(0, 5)
scelte = ['+', '-', '*', '/']
operazione = random.choice(scelte)

print(primoNumero)
print(secondoNumero)
print(operazione)



"""
print(f"\nPrimo numero:{primoNumero},
      \n Secondo numero: {secondoNumero},
      \n Operazione: {operazione}")
"""