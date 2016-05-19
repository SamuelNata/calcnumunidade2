import time
from utils import *
from limites import *


def bissect(xBaixo, xAlto, erro):
	print "buscando no intervalo {} {}".format(xBaixo, xAlto)
	numDeIteracoes = 0
	xRaizAntigo = 0
	xRaiz = 0
	erroAtual = 1
	if(erro < 0 or erro > 1):
		print('{} não é um valor válido, insira um valor entre 0 e 1!'.format(erro))
		return None
	while(erro <= erroAtual):
		xRaiz = (xAlto + xBaixo)/2
		trocaSinal = f(xBaixo) * f(xRaiz)
		erroAtual = abs((xRaiz - xRaizAntigo))
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
	print ('A solucao foi ',xRaiz)
	return xRaiz

limite = a()
bissect(limite[0], limite[1], 0.00001)