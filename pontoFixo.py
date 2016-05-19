import time
from utils import *
from limites import *

def pontoFixo(xInicial, erroEsperado):
	xAtual = xInicial
	erroAtual = 1
	numeroDeIteracoes = 0
	# Verifica se o erro esperado eh valido
	if(erroEsperado < 0 or erroEsperado > 1):
		print('{} is not a valid value, insert a number between 0 and 1'.format(erroEsperado))
		return None
	else:
		while(erroAtual > erroEsperado):
			# Atualiza a aproximacao
			xAntigo = xAtual
			xAtual = g(xAntigo)
			# Atualiza o erro absoluto percentual
			erroAtual = abs(xAtual - xAntigo)
			numeroDeIteracoes = numeroDeIteracoes + 1
			# Verifica a convergencia
			if(abs(g_(xAtual)) >= 1):
				#print "g_(atual) = ", g_(xAtual)
				print('The function g(x) is not converging to a root!')
				return -1
			print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xAtual, erroAtual))
			print ' '
		print('The algorithm found the approximation {0:.7f} with {1:d} iterations!'.format(xAtual, numeroDeIteracoes))
		print ' '
pontoFixo(0, 0.00000000001)