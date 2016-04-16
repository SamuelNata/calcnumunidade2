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
			erroAtual = abs((xRaiz - xRaizAntigo) / xRaiz)
			print('O resultado de f({0:.7f}) * f({1:.7f}) é {2:.7f}'.format(xBaixo, xRaiz, trocaSinal))
			if(trocaSinal < 0):
				xAlto = xRaiz
				print('Trocando o limite superior')
			elif(trocaSinal > 0):
				xBaixo = xRaiz
				print('Trocando o limite inferior')
			else:
				print('{} é raiz do polinomio!'.format(xRaiz))
				return xRaiz
			print('A raiz é {0:.7f} com erro de {1:.7f}%'.format(xRaiz, erroAtual*100))
			print()
			xRaizAntigo = xRaiz
			numDeIteracoes = numDeIteracoes + 1
			time.sleep(1)
		print('A aproximação precisou de {} iterações!'.format(numDeIteracoes))
		return xRaiz


poli = [1, 3, -10]

bissect(poli, -20, -1, 0.00001)