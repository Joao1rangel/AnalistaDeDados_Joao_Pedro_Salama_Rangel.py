
maior_idade = 0
mulheres_18_35 = 0
olhos_verdes_cabelos_louros = 0
n = 1

quantidade_habitantes = int(input("Informe a quantidade de habitantes a serem analisados: "))

for i in range(quantidade_habitantes):
    print(f"Habitante {n}:")
    n += 1
    
    
    
    sexo = input("Sexo (M/F): ").upper()
    cor_olhos = input("Cor dos olhos (azul, verde, castanho): ").upper()
    cor_cabelos = input("Cor dos cabelos (loiro, castanho, preto, ruivo): ").upper()
    idade = int(input("Idade: "))
    
    
    if idade > maior_idade:
        maior_idade = idade

    
    if sexo == 'F' and 18 <= idade <= 35:
        mulheres_18_35 += 1

    
    if cor_olhos == 'VERDE' and cor_cabelos == 'LOIRO':
        olhos_verdes_cabelos_louros += 1



print(f"Maior idade registrada: {maior_idade}")
print(f"Quantidade de mulheres entre 18 e 35 anos: {mulheres_18_35}")
print(f"Quantidade de pessoas com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")
