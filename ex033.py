n1 = float(input('Diga o primeiro número!'))
n2 = float(input('Diga o segundo número!'))
n3 = float(input('Diga o terceiro número'))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O número menor é {}'.format(menor))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O valor maior é %f' % (maior))