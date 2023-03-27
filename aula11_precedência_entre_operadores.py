# 1. (n + n) => primeiro a ser executado é parenteses
# de dentro pra fora.

# 2. ** => Segunda mais forte é expodenciação ou potenciação

# 3. * / // % => Terceira, quarta.. multiplicação,divisão,divisão inteira e modulo.

# 4. + - => Adição e subtração

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)