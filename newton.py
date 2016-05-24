#testado e funcionando

from __future__ import division
import time
from utils import *
from limites import *

#f = f1 # f1 ta definido em utils

def newton(f, xChute, erro, show = False):
	print('(=== NEWTON ===)')
	f(0, True)
	if(show):
		print('')

	if(xChute == None or erro == None):
		print('Por favor, insira entradas válidas!')
		return None
	else:
		print ("Busca começa em {}".format(xChute))
		numDeIteracoes = 0
		xRaizAntigo = 0
		xRaiz = xChute
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} não é válido, insira um erro não negativo menor que 1'.format(erro))
			return None
		if(show):
			print('iretação	| Aproximação		| erro')
		while(abs(f(xRaiz))>=erro):
			if(f_(f, xRaiz)==0):
				print('A derivada no intervalo é nula, tente outro metodo.')
			xRaiz -= f(xRaiz)/f_(f, xRaiz)
			if(show):
				#print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xRaiz, erroAtual))
				print('{0:.0f}		| {1:.10f}		| {2:.6f}'.format(numeroDeIteracoes, xAtual, erroAtual))
				print('')
			numDeIteracoes = numDeIteracoes + 1
			#time.sleep(1)
		if(show):
			f(0, True)
		print('O algoritmo de Newton encontrou a aproximação {0:.7f} com {1:d} iterações!'.format(xRaiz, numDeIteracoes))
		print('')
	return
