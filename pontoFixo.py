import time
from utils import *

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
			if(abs(g_(xAtual)) >= 1):
				print("A sequência diverge...")
				return -1
			# Atualiza a aproximação
			xAntigo = xAtual
			xAtual = g(xAtual)
			# Atualiza o erro absoluto percentual
			if(xAtual != 0):
				erroAtual = abs((xAtual - xAntigo)/xAtual) * 100
			numeroDeIteracoes = numeroDeIteracoes + 1
			print("A raiz da iteração é {0:.7f}".format(xAtual))
		return xAtual
	return -1


pontoFixo(0, 0.1)