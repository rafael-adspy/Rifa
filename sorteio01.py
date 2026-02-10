import random
print(' Rifa do bem!')
print(' Os candidados restante sao, Jose, Roberto, Julia, Edgar, Aline, Mario, Ester, Maria, Bruno e Ana.\nBoa Sorte a todos!')
n1 = str('Jose')
n2 = str('Roberto')
n3 = str('Julia')
n4 = str('Edgar')
n5 = str('Aline')
n6 = str('Mario')
n7 = str('Ester')
n8 = str('Maria')
n9 = str('Bruno')
n10 = str('Ana')
lista = [ n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 ]
ganhador = random.choice(lista)
print(' O ganhador do premio é: {}'.format(ganhador))


