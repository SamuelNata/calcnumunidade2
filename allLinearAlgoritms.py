#allLinearAlgoritms
from limites import *
from utils import *
from pontoFixo import *
from bissecao import *
from newton import *
from condaSimples import *

show = False

f = f2
g = g1c

intervalo1 = trocaDeSinal(f, True)
intervalo2 = limites(f)

print('Troca de sinal encontrou {}'.format(intervalo1))
print('Limites encontrou {}'.format(intervalo2))



bissect(intervalo1[0], intervalo1[1], 0.00001)
cordaSimples(intervalo1[0], intervalo1[1], 0.00001)
pontoFixo(intervalo1[0], 0.00001)
newton(intervalo1[0], 0.00001)

