def limiteSuperiorPositivo(polinomio):
    temRaizPositiva = False
    temK = False
    for i in range(len(polinomio), 0):
        if(polinomio[i]<0):
            temRaizPositiva = True
            if(!temK):
                k = i
            if(b<-1*polinomio[i]):
                b = -1*polinomio[i]
    if(!temK):
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
    for i in range(len(p1)-1), 0):
        if(p1[i]<0):
            temRaizPositiva = True
            if(!temK):
                k = i
            if(b<-1*p1[i]):
                b = -1*p1[i]
    if !temK
        return 0;
    else
        return 1+(1/(len(p1)-1-k))**(b/p1[0])

#==============================================================
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
            if(!temK):
                k = i
            if(b<-1*p1[i]):
                b = -1*p1[i]
    if !temK
        return 0;
    else
        return 1+(1/(len(p1)-1-k))**(b/p1[0])

#==============================================================
def limiteInferiorNegativo(polinomio):
    p1 = polinomio
    for i in range(len(p1)), 0):
        if((len(p1)-i)%2==1):
            p1[i] = -1*p1[i]
    
    temRaizPositiva = False
    temK = False
    for i in range(len(p1)-1, 0):
        if(p1[i]<0):
            temRaizPositiva = True
            if(!temK):
                k = i
            if(b<-1*p1[i]):
                b = -1*p1[i]
    if !temK
        return 0;
    else
        return 1+(1/(len(p1)-1-k))**(b/p1[0])

#==============================================================
#============================================================== 
def limites(polinomio):
    limitesList = [0, 0, 0, 0]
    limitesList[0] = limiteSuperiorPositivo(polinomio)
    limitesList[1] = limiteInferiorPositivo(polinomio)
    limitesList[2] = limiteSuperiorNegativo(polinomio)
    limitesList[3] = limiteInferiorNegativo(polinomio)
    return limitesList












