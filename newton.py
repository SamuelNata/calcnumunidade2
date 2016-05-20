#testado e funcionando

from __future__ import division
import time
from utils import *
from limites import *

f = f1 # f1 ta definido em utils

def newton( xChute, erro):
	f(0, True)
	print('')

	if(xChute == None or erro == None):
		print('Please, insert valid entries!')
		return None
	else:
		print ("Search begining in {}".format(xChute))
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = xChute
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} is not a valid value, insert a number between 0 and 1'.format(erro))
			return None
		while(abs(f(xRaiz))>=erro):
			if(f_(f, xRaiz)==0):
				print('There\'s a null derivative in the interval, try other method')
			xRaiz -= f(xRaiz)/f_(f, xRaiz)
			print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xRaiz, erroAtual))
			print('')
			numDeIteracoes = numDeIteracoes + 1
			#time.sleep(1)
		f(0, True)
		print('The algorithm found the approximation {0:.7f} with {1:d} iterations!'.format(xRaiz, numDeIteracoes))
		print('')
	return

limite = trocaDeSinal(f)
#print('limites: [{},{}]'.format(limite[0], limite[1]))
newton(limite[0], 0.000001)
