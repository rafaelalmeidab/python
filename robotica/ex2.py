import math


def ret (w, l=None):
    if l is None or l == '':
        print(w*w)
    else:
        print(w*l)

ret(4, 5)
ret(2, '')
ret(5)

#Calcule a raiz quadrada
print()

for i in range(1,10):
    #print(i + " - " + math.sqrt(i)) - nao funciona, somente com tipos iguais
    print(i , " - " , math.sqrt(i))

   

