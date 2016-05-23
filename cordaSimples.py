#funcionando! :D deixei alguns prints anteriores comentados
from __future__ import division
import time
from utils import *
from limites import *

#f=f3 # f1 ta definido em utils

def cordaSimples( xBaixo, xAlto, erro, show = False):
	f(0, True)
	print ("Busca no intervalo [{0}, {1}]".format(xBaixo, xAlto))
	if(show):
		print('')

	if( f(xBaixo)>0 or f(xAlto)<0 ): #concertando limites
		aux = xAlto
		xAlto = xBaixo
		xBaixo = aux

	if(xBaixo == None or xAlto == None or erro == None):
		print('Algo errado com o intervalo ou o erro!')
		return None
	else:
		numDeIteracoes = 0
		xRaizAntigo = xAlto
		xRaiz = 0
		erroAtual = 1
		if(erro < 0 or erro > 1):
			print('{} é um erro invalido, tente um erro não negativo e menor que 1'.format(erro))
			return None
		if(show):
			print('iteração | limiteAnterior	| limiteAtual		| erro')
		while(erro < erroAtual):
			xRaizAntigo = xRaiz			
			numDeIteracoes = numDeIteracoes + 1
			xRaiz = xAlto - ( f(xAlto) * (xBaixo-xAlto) / (f(xBaixo)-f(xAlto)) )
			#print('f({0:.5f}) * f({1:.5f}) = {2:.7f}'.format(xBaixo, xRaiz, trocaSinal))
			if(show):
				print('{0:d} 	| [{1:.5f}, {2:.5f}]	| '.format(numDeIteracoes, xBaixo, xAlto,), end='' )
			if( f(xRaiz) > 0 ):
				xAlto = xRaiz
				#print('Alterando limite superior para {}'.format(xRaiz))
			elif( f(xRaiz) < 0 ):
				xBaixo = xRaiz
				#print('Alterando limite inferior para {}'.format(xRaiz))
			if(show):
				print('[{0:5f}, {1:.5f}]	| {2:.10f}'.format(xBaixo, xAlto, erroAtual))
			if( f(xRaiz) == 0 ):
				erroAtual = abs(xRaiz - xRaizAntigo)
				break
			erroAtual = abs(xRaiz - xRaizAntigo)
			#print('A aproximação é {0:.7f} com erro {1:.10f}'.format(xRaiz, erroAtual))
		if(show):
			f(0, True)
		print('O algoritmo encontrou aproximação {0:.7f} com  {1:d} iterações!'.format(xRaiz, numDeIteracoes))
		print(' ')
