from utils import * 


def limiteSuperiorPositivo(polinomio):
    temRaizPositiva = False
    temK = False
    for i in range(len(polinomio), 0):
        if(polinomio[i]<0):
            temRaizPositiva = True
            if(not temK):
                k = i
            if(b<-1*polinomio[i]):
                b = -1*polinomio[i]
    if(not temK):
        return 0;
    else:
        return 1+(1/(len(polinomio)-1-k))**(b/polinomio[0])
    
#==============================================================
def limiteInferiorPositivo(polinomio):
    p1 = polinomio
    for i in range(len(p1)):
        p1[i] = p1[len(p1)-1-i]
    
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
#============================================================== 
#============================================================== 
def limites(polinomio):
    limitesList = [0, 0, 0, 0]
    limitesList[0] = limiteSuperiorPositivo(polinomio)
    limitesList[1] = limiteInferiorPositivo(polinomio)
    limitesList[2] = limiteSuperiorNegativo(polinomio)
    limitesList[3] = limiteInferiorNegativo(polinomio)
    return limitesList

#============================================================== 
def trocaDeSinal(f): # funcionando perfeitamente*
    #f(0,True)
    passo = 1
    i_p = 0
    s_p = 1.5
    i_n = -1.5
    s_n = 0
    while( f(i_p)*f(s_p)>0 and f(i_n)*f(s_n)>0 ):
        #print('f({})*f({})>0 and f({})*f({})>0'.format(i_p, s_p, i_n, s_n))
        #print('{}*{}>0 and {}*{}>0'.format(f(i_p),f(s_p),f(i_n),f(s_n)) )
        #print("{}>0 and {}>0".format(f(i_p)*f(s_p),f(i_n)*f(s_n)))
        #print('{} and {}'.format(f(i_p)*f(s_p)>0,f(i_n)*f(s_n)>0 ))
        #print('')
        s_p = s_p + passo
        i_p = i_p + passo
        s_n = s_n - passo
        i_n = i_n - passo
    #print('f(i_p)*f(s_p)>0 and f(i_n)*f(s_n)>0')
    #print('{}*{}>0 and {}*{}>0'.format(f(i_p),f(s_p),f(i_n),f(s_n)) )
    #print("{}>0 and {}>0".format(f(i_p)*f(s_p),f(i_n)*f(s_n)))
    #print('{} and {}'.format(f(i_p)*f(s_p)>0,f(i_n)*f(s_n)>0 ))
    #print('')
    if (f(i_p)*f(s_p)<=0):
        return [i_p,s_p]
    else:
        return [i_n,s_n]






