#noLinearAlgorithm
from noLinearUtils import *
from broyden import *

"""SOLUCOES
F1 com F2 = [-0.70710678118, 0.70710678118] e [0.70710678118, -0.70710678118]
F1 com F3 = [-1,0] e [1,0]
F1 com F4 = [-1,0] e [1,0]
F5 com F4 = toda a tera y=0
F2 com F4 = [0,0]
"""

def F(x, size = False): #R^n->R^n
	funcoes = [F_2(x), F_4(x)]
	if(size):
		return len(funcoes)
	m = np.asmatrix(funcoes).T;
	return m

chute = np.mat([100,100]).T

broyden(F, chute, 0.000001)