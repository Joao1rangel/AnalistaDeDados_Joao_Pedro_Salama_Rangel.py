nome = input("digite seu nome: ")
valor_hora_trabalhada = float(input(f"Informe quanto ganha por hora {nome}: "))
horas_trabalhada = int(input("digite quantas horas trabalha no mes: "))

salario_bruto = valor_hora_trabalhada * horas_trabalhada
imposto_renda = (salario_bruto/100) * 11
inss = (salario_bruto/100) * 8
sindicato = (salario_bruto/100) * 5
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f"o salário bruto de {nome} foi {salario_bruto}")
print('----------------------------------------------')
print(f"O valor pago de Imposto de renda foi {imposto_renda}")
print('----------------------------------------------')
print(f"O valor pago de INSS foi de {inss}")
print('----------------------------------------------')
print(f"O valor pago ao Sindicado foi de : {sindicato}")
print('----------------------------------------------')
print(f"o salário liquido de {nome} foi {salario_liquido}")