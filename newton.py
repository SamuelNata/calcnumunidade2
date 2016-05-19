from __future__ import division
import time
from utils import f
from utils import f_
from limites import *

def newton( xBaixo, xAlto, erro):
	if(xBaixo == None or xAlto == None or erro == None):
		print('Please, insert valid entries!')
		return None
	else:
		print ("Searching a root in the interval [{0}, {1}]".format(xBaixo, xAlto))
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = (xAlto+xBaixo)/2
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} is not a valid value, insert a number between 0 and 1'.format(erro))
			return None
		while(abs(f(xRaiz))>=erro):
			if(f_(xRaiz)==0):
				print('There\'s a null derivative in the interval, try other method')
			xRaiz -= f(xRaiz)/f_(xRaiz)
			print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xRaiz, erroAtual))
			print ' '
			numDeIteracoes = numDeIteracoes + 1
			#time.sleep(1)
		print('The algorithm found the approximation {0:.7f} with {1:d} iterations!'.format(xAtual, numeroDeIteracoes))
		print ' '

limite = a()
print(newton(limite[0], limite[1], 0.001))
