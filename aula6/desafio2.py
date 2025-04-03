import math
area_terreno = float(input("informe o tamanho da area do terreno: "))

cobertura_por_litro = 3 
lata_litros = 18
preco = 130

tinta_necessaria = area_terreno / cobertura_por_litro
latas_necessarias = math.ceil(tinta_necessaria / lata_litros)

custo_total = latas_necessarias * preco

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias} lata(s)")
print(f"Custo total: {custo_total:.2f} Reais")