import time
from utils import fNoPonto

def bissect(poli, xBaixo, xAlto, erro):

	if(poli == None or xBaixo == None):
		print('A lista do polinômio está vazia!')
		return None
	else:
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = 0
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} não é um valor válido, insira um valor entre 0 e 1!'.format(erro))
			return None
		while(erro < erroAtual):
			xRaiz = (xAlto + xBaixo)/2
			trocaSinal = fNoPonto(poli, xBaixo) * fNoPonto(poli, xRaiz)
			print('O resultado de f({0:.5f}) * f({1:.5f}) é {2:.5f}'.format(xBaixo, xRaiz, trocaSinal))
			if(trocaSinal < 0):
				xAlto = xRaiz
			elif(trocaSinal > 0):
				xBaixo = xRaiz
			else:
				print('{} é raiz do polinomio!'.format(xRaiz))
				return xRaiz
			erroAtual = abs((xRaiz - xRaizAntigo) / xRaiz)
			print('A raiz é {0:.5f} com erro de {1:.5f}%'.format(xRaiz, erroAtual*100))
			xRaizAntigo = xRaiz
			print()
			numDeIteracoes = numDeIteracoes + 1
			time.sleep(1)
		print('A aproximação precisou de {} iterações!'.format(numDeIteracoes))
		return xRaiz


poli = [1, 4, -9]

bissect(poli, -20, -1, 0.00001)