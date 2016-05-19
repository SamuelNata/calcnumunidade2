import time
from utils import *
from limites import *

def pontoFixo(xInicial, erroEsperado):
	xAtual = xInicial
	erroAtual = 1
	numeroDeIteracoes = 0
	# Verifica se o erro esperado é válido
	if(erroEsperado < 0 or erroEsperado > 1):
		print("O erro deve ser um valor entre zero e um!")
	else:
		while(erroAtual > erroEsperado):
			# Verifica a convergência
			if(abs(g_(xAtual)) > 1):
				#print "g_(atual) = ", g_(xAtual)
				print("A função diverge...")
				return -1
			# Atualiza a aproximação
			xAntigo = xAtual
			xAtual = g(xAntigo)
			# Atualiza o erro absoluto percentual
			erroAtual = abs(xAtual - xAntigo)
			numeroDeIteracoes = numeroDeIteracoes + 1
			print("A raiz da iteração é {0:.7f} com erro {0:.7f}".format(xAtual,erroAtual))
		print("Precisou de {} iterações".format(numeroDeIteracoes))
		return xAtual
	return -1


limite = a()
pontoFixo(0, 0.1)