lista_temperaturas = []

quantidade_temperaturas = int(input("Quantas temperaturas deseja informar? "))
n = 17
for i in range(quantidade_temperaturas):
    temperatura = float(input(f"Informe a temperatura {n} em Celcius: "))
    n += 1
    lista_temperaturas.append(temperatura)

# Cálculos
menor = min(lista_temperaturas)
maior = max(lista_temperaturas)
media = sum(lista_temperaturas) / len(lista_temperaturas)

# Exibição dos resultados
print(f"\nMenor temperatura: {menor}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Média das temperaturas: {media:.1f}°C")
