nome = 'Ana Virginia'
altura = 1.50
peso = 59
imc =  peso / (altura * altura)
print(imc)

# f-strings => formatação
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
# print(nome, 'tem', altura, 'de altura,',)
# print('pesa', peso, 'quilos e seu imc é',)
# print(imc)

# Ana Virginia tem 1.50 de altura,
# pesa 59 quilos e seu imc é