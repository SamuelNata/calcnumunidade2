#noLinearAlgorithm
from noLinearUtils import *
from broyden import *

"""SOLUCOES

F1 com F2 = [-0.70710678118, 0.70710678118] e [0.70710678118, -0.70710678118]
F1 com F3 = [-1,0] e [1,0]
F1 com F3 com F4 = [-1,0] e [1,0]



"""

def F(x): #R^n->R^n
	m = np.asmatrix([F_1(x), F_3(x), F_4(x)]).T;
	return m

chute = np.mat([10,10]).T

broyden(F, chute, 0.000001)