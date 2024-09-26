import json
import math
# Lendo um JSON
with open('faturamentos.json', 'r') as file:
    entrada = json.load(file)
faturamentos = entrada["faturamentos"]
maior = 0
menor = math.inf
soma = 0
cont = 0
for faturamento in faturamentos:
    if faturamento>0:
        if faturamento<menor:
            menor = faturamento
        if faturamento>maior:
            maior = faturamento
        soma+=faturamento
        cont+=1
media = soma/cont
contMedia = 0
for faturamento in faturamentos:
    if faturamento>media:
        contMedia+=1
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Houveram {contMedia} faturamentos acima da média mensal")