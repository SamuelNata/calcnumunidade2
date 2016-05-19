from __future__ import division
from utils import *
import time

#from limites import *


def bissect(xBaixo, xAlto, erro):
	print ("Searching a root in the interval [{0}, {1}]".format(xBaixo, xAlto))
	numDeIteracoes = 0
	xRaizAntigo = 0
	xRaiz = 0
	erroAtual = 1
	if(erro < 0 or erro > 1):
		print('{} is not a valid value, insert a number between 0 and 1'.format(erro))
		return None
	while(erro <= erroAtual):
		xRaizAntigo = xRaiz
		xRaiz = (xAlto + xBaixo)/2
		numDeIteracoes = numDeIteracoes + 1
		trocaSinal = f(xBaixo) * f(xRaiz)
		if(xRaiz != 0):
			erroAtual = abs((xRaiz - xRaizAntigo) / xRaiz)
		print('f({0:.5f}) * f({1:.5f}) = {2:.7f}'.format(xBaixo, xRaiz, trocaSinal))
		if(trocaSinal < 0):
			xAlto = xRaiz
			print('Changing the upper limit')
		elif(trocaSinal > 0):
			xBaixo = xRaiz
			print('Changing the lower limit')
		else:
			print('{} is a root!'.format(xRaiz))
			return xRaiz
		print('The approximation is {0:.7f} with an error of {1:.2f}%'.format(xRaiz, erroAtual*100))
		print ' '
		time.sleep(1)
	print('The algorithm found the approximation {0:.7f} with {1:d} iterations!'.format(xRaiz, numDeIteracoes))
	print ' '

bissect(-20, -1, 0.00001)