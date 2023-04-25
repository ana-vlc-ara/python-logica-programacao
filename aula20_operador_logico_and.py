# Operador lógico
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considereado falso, a expressão inteira será 
# avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0 0 '' False
# Também existe o tipo de None que é usado para representar um não valor 

#entrada = input('[E]entrar [S]air:')
#senha_digitada = input('senha:')

#senha_permitida = '123456'
# if True:
#...
#if entrada == 'E' and senha_digitada == senha_permitida:
  #  print('Entrar')
#else:
  #  print('Sair')

# Avaliação de curto circuito
#print(True and False and True)
#print(True and 0 and True)

if 1 and 1:
    print(True and 1 and False)