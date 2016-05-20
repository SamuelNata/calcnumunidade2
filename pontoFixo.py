import time
from utils import *
from limites import *

f = f3 # fi ta definido em utils (para rodar outra função basta alterar o i)
g = g3c # giL ta definido em utils (para rodar outra função basta alterar o i)
		# L='c' -> gic (gi que converge)
		# L='d' -> gid (gi que diverge)

def pontoFixo(xInicial, erroEsperado):
	f(0, True)
	g(0, True)
	print ("Iniciando busca em x = {0}".format(xInicial))
	print('')

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
			if(abs(g_(g, xAtual)) >= 1):
				#print "g_(atual) = ", g_(xAtual)
				print('The function g(x) is not converging to a root!')
				return -1
			print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xAtual, erroAtual))
			print(' ')
		f(0, True)
		print('The algorithm found the approximation {0:.7f} with {1:d} iterations!'.format(xAtual, numeroDeIteracoes))
		print(' ')


pontoFixo(0, 0.00000000001)