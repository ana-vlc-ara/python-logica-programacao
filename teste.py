#media_final = 6

#if media_final >= 7:
#    print("aprovado")
#else:
#    print("reprovado")


media_final = 7
faltas = 5

if media_final >= 7 and faltas >= 5:
    print("aprovado")
else:
    print("reprovado")



variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')