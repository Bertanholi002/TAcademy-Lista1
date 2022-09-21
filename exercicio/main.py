# pegar quanto ganha por hora e o numero de horas trabalhadas
# calcule e mostre o total do salario com descontos de 11 imposto de renda 8 para inss e 5 para sindicato
# mostre o salario bruto e o salario liquido 

valor_recebido_hora = int(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalha por mês? "))

salario_bruto = valor_recebido_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
desconto_total = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - desconto_total  

print(f"O salario bruto é de {salario_bruto}, o liquido é de {salario_liquido}. Para demonstração, os descontos são {imposto_renda}{inss}{sindicato}")