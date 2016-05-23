#falta só encontrar as g1 (g1d) que divirja e g3 (g3c) que convirja
import time
from utils import *
from limites import *

#f = f3 # fi ta definido em utils (para rodar outra função basta alterar o i)
#g = g3c # giL ta definido em utils (para rodar outra função basta alterar o i)
		# L='c' -> gic (gi que converge)
		# L='d' -> gid (gi que diverge)

def pontoFixo(xInicial, erroEsperado, show = False):
	f(0, True)
	g(0, True)
	print ("Iniciando busca em x = {0}".format(xInicial))
	if(show):
		print('')

	xAtual = xInicial
	erroAtual = 1
	numeroDeIteracoes = 0
	# Verifica se o erro esperado eh valido
	if(erroEsperado < 0 or erroEsperado > 1):
		print('{} is not a valid value, insert a number between 0 and 1'.format(erroEsperado))
		return None
	else:
		if(show):
			print('iretação	| Aproximação		| erro')
		while(erroAtual > erroEsperado):
			# Atualiza a aproximacao
			xAntigo = xAtual
			xAtual = g(xAntigo)
			# Atualiza o erro absoluto percentual
			erroAtual = abs(xAtual - xAntigo)
			numeroDeIteracoes = numeroDeIteracoes + 1
			# Verifica a convergencia
			if(abs(g_(g, xAtual)) >= 1):
				print('g(x) não converge!')
				return -1
			if(show):
				print('{0:.0f}		| {1:.10f}		| {2:.6f}'.format(numeroDeIteracoes, xAtual, erroAtual))
			#print('The approximation is {0:.7f} with an error of {1:.10f}'.format(xAtual, erroAtual))
		if(show):
			f(0, True)
			g(0, True)
		print('Algoritmo obteve aproximação x={0:.7f} com {1:d} iterações!'.format(xAtual, numeroDeIteracoes))
		print(' ')