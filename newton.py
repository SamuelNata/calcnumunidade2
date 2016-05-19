from __future__ import division
import time
from utils import f
from utils import f_
from limites import *

def newton( xBaixo, xAlto, erro):
	if(xBaixo == None or xAlto == None or erro == None):
		print('os argumentos não devem ser vazios!')
		return None
	else:
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = (xAlto+xBaixo)/2
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} não é um valor válido, insira um valor entre 0 e 1!'.format(erro))
			return None
		while(abs(f(xRaiz))>=erro):
			if(f_(xRaiz)==0):
				print('existe derivada nula no intervalo, use outro metodo')
			xRaiz -= f(xRaiz)/f_(xRaiz)
			print('a raiz atual é {}.'.format(xRaiz))
			numDeIteracoes = numDeIteracoes + 1
			time.sleep(1)
		print('A raiz é {0:.7f} com erro de {1:.7f}%'.format(xRaiz, f(xRaiz)))
		print('A aproximação precisou de {} iterações!'.format(numDeIteracoes))
		return xRaiz


#poli = [1, 3, -10]
limite = a()
print(newton(limite[0], limite[1], 0.001))
