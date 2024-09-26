faturamentos = [{"Estado":"SP","Quantia": 67836.43},{"Estado":"RJ","Quantia": 36678.66},{"Estado":"MG","Quantia": 29229.88},{"Estado":"ES","Quantia": 27165.48},{"Estado": "Outros", "Quantia":19849.53}]
soma=0
for faturamento in faturamentos:
    soma+=faturamento["Quantia"]
for faturamento in faturamentos:
    estado = faturamento["Estado"]
    quantia = faturamento["Quantia"]
    print(f"{estado}:{quantia*100/soma:.2f}%")