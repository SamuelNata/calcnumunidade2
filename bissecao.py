#Funcionando :D
from __future__ import division
from utils import *
from limites import *
import time

#f=f1 # fi ta definido em utils

def bissect(f, xBaixo, xAlto, erro, show = False):
	print('(=== BISSEÇÃO ===)')
	f(0, True)
	print ("Buscando no intervalo [{0}, {1}]".format(xBaixo, xAlto))
	if( show ):
		print('')

	numDeIteracoes = 0
	xRaizAntigo = 0
	xRaiz = 0
	erroAtual = 1
	if(erro < 0 or erro > 1):
		print('{} invalido, insira um erro não negativo menor que 1.'.format(erro))
		return None
	if( show ):
		print('iteração | limiteAnterior	| limiteAtual		| erro')
	while(erro <= erroAtual):
		xRaizAntigo = xRaiz
		xRaiz = (xAlto + xBaixo)/2
		numDeIteracoes = numDeIteracoes + 1
		trocaSinal = f(xBaixo) * f(xRaiz)
		erroAtual = abs(xRaiz - xRaizAntigo)
		if( show ):
			print('{0:d} 	| [{1:.5f}, {2:.5f}]	| '.format(numDeIteracoes, xBaixo, xAlto,), end='' )
		#print('f({0:.5f}) * f({1:.5f}) = {2:.7f}'.format(xBaixo, xRaiz, trocaSinal))
		if(trocaSinal < 0):
			xAlto = xRaiz
			#print('Changing the upper limit')
		elif(trocaSinal > 0):
			xBaixo = xRaiz
			#print('Changing the lower limit')
		#else:
			#print('{} is a root!'.format(xRaiz))
			#return xRaiz

		if( show ):
			print('[{0:5f}, {1:.5f}]	| {2:.10f}'.format(xBaixo, xAlto, erroAtual))
		#print('A aproximação é {0:.7f} com erro {1:.2f}%'.format(xRaiz, erroAtual*100))
		#print(' ')
	if( show ):
		f(0, True)
	print('O algoritmo da bisseção encontro aproximação {0:.7f} com {1:d} iterações!'.format(xRaiz, numDeIteracoes))
	print(' ')