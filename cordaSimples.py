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
			print('O resultado de f({0:.5f}) * f({0:.5f}) é {0:.5f}'.format(xBaixo, xRaiz, trocaSinal))
			if(trocaSinal < 0):
				xAlto = xRaiz
			elif(trocaSinal > 0):
				xBaixo = xRaiz
			else:
				print('{0:.5f} é raiz do polinomio!'.format(xRaiz))
				return xRaiz
			erroAtual = abs((xRaiz - xRaizAntigo) / xRaiz)
			print('O erro é {0:.5f}%'.format(erroAtual*100))
			print()
			xRaizAntigo = xRaiz			
			numDeIteracoes = numDeIteracoes + 1
			time.sleep(1)
		print('A aproximação precisou de {} iterações!'.format(numDeIteracoes))
		return xRaiz


poli = [1, 4, -9]

print(cordaSimples(poli, -20, -1, 0.001))