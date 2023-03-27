# if / elif      / else
# se / se não se / se não
def calcular(*args):    
    # r = 1 + 4 + 5 = 10
    r = sum(args)    
    
    # r = 10
    for i in args:
        # 1 vez -> r = r(10) + 1 -> 11
        # 2 vez -> r = r(11) + 4 -> 15
        # 3 vez -> r = r(15) + 5 -> 20        
        r += i
    
    return r    

print(calcular(1, 4, 5))