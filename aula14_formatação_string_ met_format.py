# Função format, tudo em python é um objeto
a = 'AAAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'  #está pegando por indices, não depende
# da ordem

# parametro nomeando é quando damos nomes as coisas
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
print('"Já sei"')