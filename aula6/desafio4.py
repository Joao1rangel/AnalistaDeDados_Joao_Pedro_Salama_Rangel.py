lista_num = []
n = 1
for i in range(10):
    lista_num.append(int(input(f"informe o {n}ro numero:")))
    n += 1

soma = sum(lista_num)
maior = max(lista_num)
menor = min(lista_num)
media = sum(lista_num) / len(lista_num) 

print(f"a lista de numero é {lista_num}")
print(f"O maior número dessa lista é o {maior} e o menor é o {menor}")
print(f"A soma dos numeros dessa lista é {soma} e a média entre esse números é de {media:.1f}")
