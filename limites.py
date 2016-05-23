
from utils import * 

def limiteSuperiorPositivo(polinomio): # funcionando
    n = len(polinomio)-1
    temRaizPositiva = False
    temK = False
    temB = False
    for i in range(n+1):
        if(polinomio[i]<0):
            temRaizPositiva = True
            if(i!=0 and not temK):
                k = n-i
                temK = True
            if(not temB):
                b = -1*polinomio[i]
                temB = True
            else:
                if(b<-1*polinomio[i]):
                    b = -1*polinomio[i]
    if(not temK):
        return 0;
    else:
        #print('b={}; an={}; n={}; k={}'.format(b, polinomio[0], n, k))
        return 1+(b/polinomio[0])**(n-k)
    
#==============================================================
def limiteInferiorPositivo(polinomio):
    p1 = polinomio
    for i in range(len(p1)):
        p1[i] = polinomio[len(p1)-1-i]
    print("polinomio{}\n p1{}".format(polinomio, p1))
    temRaizPositiva = False
    temK = False
    for i in range((len(p1)-1), 0):
        if(p1[i]<0):
            temRaizPositiva = True
            if(not temK):
                k = i
            if(b<-1*p1[i]):
                b = -1*p1[i]
    if(not temK):
        return 0;
    else:
        return 1+(1/(len(p1)-1-k))**(b/p1[0])

#==============================================================
def limiteSuperiorNegativo(polinomio):
    p1 = polinomio
    p1.reverse()
    for i in range(len(p1)):
        if(i%2==1):
            p1[i]=-1*p1[i]
    
    temRaizPositiva = False
    temK = False
    for i in range(len(p1)-1, 0):
        if(p1[i]<0):
            temRaizPositiva = True
            if(not temK):
                k = i
            if(b<-1*p1[i]):
                b = -1*p1[i]
    if(not temK):
        return 0;
    else:
        return 1+(1/(len(p1)-1-k))**(b/p1[0])

#==============================================================
def limiteInferiorNegativo(polinomio):
    p1 = polinomio
    for i in range(len(p1), 0):
        if((len(p1)-i)%2==1):
            p1[i] = -1*p1[i]
    
    temRaizPositiva = False
    temK = False
    for i in range(len(p1)-1, 0):
        if(p1[i]<0):
            temRaizPositiva = True
            if(not temK):
                k = i
            if(b<-1*p1[i]):
                b = -1*p1[i]
    if(not temK):
        return 0;
    else:
        return 1+(1/(len(p1)-1-k))**(b/p1[0])


#==============================================================
#====================       ISOLAMENTO   ======================
#============================================================== 
def limites(f):
    if( f(0, False, True)==[0] ):
        print('A função não é um polinomio.')
        return [0,0,0,0]
    limitesList = [0, 0, 0, 0]
    limitesList[0] = limiteSuperiorPositivo(f(0, False, True))
    limitesList[1] = limiteInferiorPositivo(f(0, False, True))
    limitesList[2] = limiteSuperiorNegativo(f(0, False, True))
    limitesList[3] = limiteInferiorNegativo(f(0, False, True))
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
        print('Nenhuma intervalo contendo raiz encontrado.')
        print('')
        return
    if (f(i_p)*f(s_p)<=0):
        print('')
        return [i_p,s_p]
    else:
        print('')
        return [i_n,s_n]






