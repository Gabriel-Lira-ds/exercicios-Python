maior = 0
menor = 0
for p in range(1,6):
	peso = float(input('Qual o peso da {}° pessoa: '.format(p)))
	if p == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))

# Outra opção

'''pesos = []
for p in range(1, 6):
	peso = float(input('Qual o pesso da {}° pessoa: '.format(p)))
	pesos.append(peso)
print('O maior peso é {}Kg'.format(max(pesos)))
print('O menor peso é {}Kg'.format(min(pesos)))'''