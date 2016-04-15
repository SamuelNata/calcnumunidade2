
def fNoPonto(poli, ponto):
	
	soma = 0
	grau = len(poli)
	#print('Calculando f({})...'.format(ponto))
	for i in range(grau):
		soma = soma + poli[i] * (ponto**(grau-i-1))
	return soma