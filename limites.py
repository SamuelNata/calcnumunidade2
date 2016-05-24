from utils import * 

def LP(polinomio):
    temK = False
    temRaizPositiva = False
    n = len(polinomio)-1
    b = abs(polinomio[0])
    for i in range(n+1):
        if(polinomio[i]<0):
            temRaizPositiva = True
            if( i!=0 and not temK):
                k = n-i
                temK = True
            if(b<-polinomio[i]):
                b = -polinomio[i]
    if(not temK):
        return 0;
    else:
        #print('b={}; an={}; n={}; k={}'.format(b, polinomio[0], n, k))
        return 1+(b/polinomio[0])**(1/(n-k))

#==============================================================
def limiteSuperiorPositivo(polinomio): # funcionando
    #print('LSP: {}'.format(polinomio))
    return LP(polinomio)

#==============================================================
def limiteInferiorPositivo(polinomio): # funcionando
    p1 = polinomio*1
    p1.reverse()
    #print('LIP: {}'.format(p1))
    return LP(p1)

#==============================================================
def limiteSuperiorNegativo(polinomio): # funcionando
    p1 = polinomio*1
    p1.reverse()
    for i in range(1,len(p1)+1):
        p1[-i] = p1[-i]*(-1)**(i+1)
    #print('LSN: {}'.format(p1))
    return LP(p1)

#==============================================================
def limiteInferiorNegativo(polinomio): # funcionando
    p1 = polinomio*1
    for i in range(1,len(p1)+1):
        p1[-i] = p1[-i]*(-1)**(i+1)
    #print('LIN: {}'.format(p1))
    return LP(p1)

#============================================================== 
def limites(f):
    if( f(0, False, True)==[0] ):
        print('A função não é um polinomio.')
        return [0,0,0,0]
    limitesList = [0, 0, 0, 0]
    limitesList[0] = limiteSuperiorPositivo(f(0, False, True))
    limitesList[1] = limiteInferiorPositivo(f(0, False, True))
    limitesList[2] = -limiteSuperiorNegativo(f(0, False, True))
    limitesList[3] = -limiteInferiorNegativo(f(0, False, True))
    return limitesList

#============================================================== 
def trocaDeSinal(f, show = False): # funcionando perfeitamente*
    if(show):
        f(0,True)
    passo = 1
    i_p = 0
    s_p = 1.5
    i_n = -1.5
    s_n = 0
    while( f(i_p)*f(s_p)>0 and f(i_n)*f(s_n)>0 ) and s_p<1000 and i_n>-1000:
        s_p = s_p + passo
        i_p = i_p + passo
        s_n = s_n - passo
        i_n = i_n - passo

    if(s_p==1000 or i_n==-1000):
        print('TrocaDeSinal(): Nenhuma intervalo contendo raiz encontrado.')
        print('')
        return
    if (f(i_p)*f(s_p)<=0):
        return [i_p,s_p]
    else:
        return [i_n,s_n]






