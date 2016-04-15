import time
from utils import fNoPonto

def cordaSimples(poli, xBaixo, xAlto, erro):

	if(poli == None or xBaixo == None or xAlto == None or erro == None):
		print('os argumentos não devem ser vazios!')
		return None
	else:
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = 0
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} não éum valor válido, insira um valor entre 0 e 1!'.format(erro))
			return None
		while(erro < erroAtual):
			xRaiz = xAlto - ((fNoPonto(poli, xAlto) * (xBaixo - xAlto)) / \
					(fNoPonto(poli, xBaixo) - fNoPonto(poli, xAlto)))
			trocaSinal = fNoPonto(poli, xBaixo) * fNoPonto(poli, xRaiz)
			print('O resultado de f({}) * f({}) é {}'.format(xBaixo, xRaiz, trocaSinal))
			if(trocaSinal < 0):
				xAlto = xRaiz
			elif(trocaSinal > 0):
				xBaixo = xRaiz
			else:
				print('{} é raiz do polinomio!'.format(xRaiz))
				return xRaiz
			erroAtual = abs((xRaiz - xRaizAntigo) / xRaiz)
			print('O erro é {}-{}/{} = {}%'.format(xRaiz, xRaizAntigo, xRaiz, erroAtual*100))
			xRaizAntigo = xRaiz
			print()
			numDeIteracoes = numDeIteracoes + 1
			time.sleep(1)
		print('A aproximação precisou de {} iterações!'.format(numDeIteracoes))
		return xRaiz


poli = [1, -2, -5, -6]

print(cordaSimples(poli, 0, 4, 0.001))