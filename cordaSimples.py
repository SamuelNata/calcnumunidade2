from __future__ import division
import time
from utils import f
#from limites import *

def cordaSimples( xBaixo, xAlto, erro):

	if(xBaixo == None or xAlto == None or erro == None):
		print('Please, insert valid entries!')
		return None
	else:
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = 0
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} is not a valid value, insert a number between 0 and 1'.format(erro))
			return None
		print ("Searching a root in the interval [{0}, {1}]".format(xBaixo, xAlto))
		while(erro < erroAtual):
			xRaizAntigo = xRaiz			
			numDeIteracoes = numDeIteracoes + 1
			xRaiz = xAlto - ((f(xAlto) * (xBaixo - xAlto)) / (f(xBaixo) - f(xAlto)))
			trocaSinal = f(xBaixo) * f(xRaiz)
			if(xRaiz != 0):
				erroAtual = abs(xRaiz - xRaizAntigo)
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
			print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xRaiz, erroAtual))
			print ' '
			#time.sleep(1)
		print('The algorithm found the approximation {0:.7f} with {1:d} iterations!'.format(xRaiz, numDeIteracoes))
		print ' '

cordaSimples(-400, 0, 0.00001)