# if / elif       / else
# se / se não se  / se não
# Não se pode ter elif ou else sozinhos, eles dependem do if
# else é a ultima coisa a ser execultada
# A partir do if, não se pode ter outro if, so se tem um if no bloco.
# Para se ter outras condições se utiliza o elif
# obs: quando não se quer escrever codigo, pode se utilizar o ... (elipce)
# ou o pass (que significa passa depois eu escrevo )
# A partir do momento que se encontra uma opção verdadeira, ele não checa as demais.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
        print('Outro if')

print('Fora do if')
