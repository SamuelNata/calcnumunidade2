#allLinearAlgoritms
from limites import *
from utils import *

f = f3
g = g2c

from pontoFixo import *
from bissecao import *
from newton import *
from cordaSimples import *

show = False

intervalo1 = trocaDeSinal(f, True)
intervalo2 = limites(f)

print('Troca de sinal encontrou {}'.format(intervalo1) )
print('Limites encontrou {}'.format(intervalo2) )
print('')


bissect(f, intervalo1[0], intervalo1[1], 0.00001, show)
cordaSimples(f, intervalo1[0], intervalo1[1], 0.00001, show)
pontoFixo(f, g, intervalo1[0], 0.00001, show)
newton(f, intervalo1[0], 0.00001, show)
