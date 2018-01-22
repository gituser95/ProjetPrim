import xlrd
import pub
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import time




#####    #######   ######   ######    #####    #######   ######   ######     #####    #######   ######   ######

def timeTicks(x, pos):
    d = datetime.timedelta(seconds=x)

    return str(d)[:5]



def Sheet_reading(wb,a):
    #La fonction responsable de la lecture de la feuille donnée comme argument
    #elle est responsable de reccupèrer les differents données nécessaires pour notre algorithme et les mettre dans des listes
    xl_sheet = wb.sheet_by_index(a)
    print ('Sheet name: %s' % xl_sheet.name)
    #Déclarations :
    #############
    #Les colonnes qui nous servirent par la suite
    colonne1 =  xl_sheet.col_values(1) #colonne du temps minute par minute % TM-frda-50
    colonne5 = xl_sheet.col_values(5) # colonne des valeurs de taux moyen FRDA-50
    colonne7 = xl_sheet.col_values(7)#colonne du temps minute par minute % Les emissions
    colonne9 = xl_sheet.col_values(9)#colones qui contient les noms des emissions
    colonne8 = xl_sheet.col_values(8)
    colonne14= xl_sheet.col_values(14)  # colones qui contient le nombre des pubs maximal par emission


    # Des variables utiles pour le traitement suivant
    i = colonne1.index('Minute') + 1# L'indice de la ligne avec laquelle on commence à retrouver les valeurs de differents tableaux
    h = colonne1.index('Minute')+1
    fin=colonne7[h:].index('')+h-1
    pub = 'Pub'
    col1size=len(colonne1)#La taille de la premiere colonne (celle du temps correspondant aux valeurs de Tm-frda-50)
    col2size = len(colonne7)  # La taille de la 7ème colonne (celle du l'heure de debut des emissions)
    tm_time=[]#la liste qui contient les valeurs temporelles transformées en secondes
    tm_frda=[]#la liste qui contient les valeurs tm-frda transformées en secondes
    Pubsname=[]#une liste où on va enregistrer les noms des pubs successivement
    Pubsduration = []#une liste où on va enregistrer les durées des pubs successivement
    Programsname = []  # une liste où on va enregistrer les noms des emissions successivement
    Programsduration = []  # une liste où on va enregistrer les durées des emissions successivement
    MaxNumOfPubs=[] # une liste qui contient le nombre maximale des pubs par emission
    ProgramGivenIndex=[]

    ##############    ##############     ##############      ##############

    # Ci-dessous, on va créer deux listes à partir du 1èr tableau : la premiere sert à conserver le temps en secondes et la deuxième
    #pour conserver les valeur de tm-frda

    while i < col1size:
         strp = colonne1[i].split(':')
         time=int(strp[0])*3600+int(strp[1])*60
         j=0
         while j<60:
            tm_time.append(time+j)
            tm_frda.append(colonne5[i])
            j=j+1
         i=i+1
    # ici on va creer deux listes à partir du 2ème tableau dans le fichier excel: deux listes pour conserver respectivement la
    #duree en  sec des emissions et des pubs, et deux listes pour conserver les noms des emissions et pubs
    """traitement appliquer sur la 9ème colonne pour reccuperer la durée en secondes ainsi que les noms des pubs"""
    ProgramDivision=[]

    while(h<fin):
        a = colonne7[h].split(':')
        b = colonne7[h + 1].split(':')
        min = int(b[1]) - int(a[1])
        sec = int(b[2]) - int(a[2])

        if(pub in colonne9[h]):
          Pubsduration.append( min * 60 + sec)
          Pubsname.append(colonne9[h])
        elif '.' in colonne9[h]:
           ProgramDivision.append(colonne9[h])
        else :
           Programsname.append(colonne9[h])
           MaxNumOfPubs.append(colonne14[h])
           onset = int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])
    #ici il s'agit de donner l'indice de debut
           if onset < 70200:
               ProgramGivenIndex.append(70200)
               Programsduration.append(abs(min) * 60 + sec - 70200 + onset)

           else:
               ProgramGivenIndex.append(onset)
     # D'abord si il n'y a pas division de l'emission
               if ((int)(colonne14[h])==0):
                 # D'abord si il n'y a pas division de l'emission
                  Programsduration.append(min * 60 + sec)
               else:
               # Si il y a une division intra-emission
                   duree=0
                   name=colonne9[h].split('|')[0]
                   print(name)
                   it=h+1

                   while('.' in colonne9[it]):
                     if(name in colonne9[it]):
                        a = colonne7[it].split(':')
                        print(a)
                        b = colonne7[it+ 1].split(':')
                        print(b)
                        min2 = int(b[1]) - int(a[1])
                        sec2= int(b[2]) - int(a[2])
                        duree=duree+min2 * 60 + sec2
                        it=it+1
                        print(it)
                   print('lol')
                   print(duree)
                   Programsduration.append(duree)
                   ProgramGivenIndex.append(onset)
        h=h+1
 #retourner la liste des valeurs temporelles, la liste des taux moyens frda, une liste des durées des pubs, une liste des noms des pubs
    return tm_time,tm_frda,Pubsduration,Pubsname,Programsname,Programsduration,MaxNumOfPubs,ProgramGivenIndex


#####    #######   ######   ######    #####    #######   ######   ######     #####    #######   ######   ######


def Tm_frdaGraph(tm_time0,tm_frda0,pubsInfoList):
    #la fonction responsable de dessiner les differentes courbes
    v = np.array(tm_time0)
    fv = np.array(tm_frda0)
    xduree=[]
    yindice=[]
    # une liste des couleurs à utiliser par la suite :
    color=['m','b','xkcd:ice','c','xkcd:gold','k','r','xkcd:neon pink','y','g','xkcd:bright orange']

    for i in range(len(pubsInfoList)):
        if (pubsInfoList[i][2] == None):
            print("La pub " + pubsInfoList[i][0] + " n'étais pas placée")
        else:
         xduree.append(pubsInfoList[i][1])
         yindice.append(pubsInfoList[i][2])
    k=0
    plt.figure()
    fctPubtemp = [0] * len(v)
    #parcourrir tous les pubs
    while k < len(yindice):
       plt.bar(x=[70200+yindice[k]], width=xduree[k], height=10,align='edge', color=color[k])
       k=k+1

    plt.plot(v, fv, 'r', label='tm_fdra % temps en sec')
    ax=plt.gca()
    formatter = matplotlib.ticker.FuncFormatter(timeTicks)
    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1800))
    plt.xticks(rotation=90)
    #p2=plt.plot(duree0,indice0)
    plt.show()
    plt.savefig('toto.png')

    #####    #######   ######   ######    #####    #######   ######   ######     #####    #######   ######   ######


    #####    #######   ######   ######    #####    #######   ######   ######     #####    #######   ######   ######


def MaxSum(tm,duration,title,tabIsPlaceVaccant):

    """La fonction MaxSum est responsable de trouver l'endroit optimal pour placer une pub dont la durée est donnée ; tq elle (la pub)
    correspond à la somme maximale des tm_frda disponile en consultant la liste  tabPlaceUsed. Elle prend, donc, comme arguments:
      - tm : La liste des taux moyens de frda
      - duration : la durée de la pub q'on veut placer
      -title : nom de la pub qu'on cherche à placer
      - tabIsPlaceVaccant : la liste qui verifier la disponibilité de l'indice cherché pour placer la pub

    Cette fonction sert à :
             * Trouver l'endroit optimal pour placer la pub en verifiant sa disponibilité avec tabPlaceUsed
             * Signaler si une pub n'est pas placée

    """
    beginningIndex=0
    Sums=[]
    listfinal=[]
    zero=0
    s=0 #compteur de la boucle while ;
 ###Traitement principale !!
    while s<(len(tm)-duration):
        # note : on doit etre capable de placer une pub à la fin
      sum = 0
      condition=True
     #Voir si c'est possible de placer la pub dans l'indice s ou non ; condition = True : on peux sinon on ne peut pas
      if (tabIsPlaceVaccant[s]==True):
          if False in tabIsPlaceVaccant[s:s+duration-1] : condition=False
      else :   # si la case est déjà pris par un traitement ultérieur (non disponible)
          condition= False
          # si on peut placer la pub à partir de l'indice s on calcule la somme des valeurs tm_frda correspondantes
      if(condition==True):
          for i in range(duration):
              sum = sum + tm[s + i]
          Sums.append(sum)
      else:
          Sums.append(0)
      s=s+1
###Organiser le resultat du traitement :
    if (max(Sums)==0):
        #print("La pub"+ title+" n'est pas placée")
        beginningIndex=None
        maxSum=None

    else:
      beginningIndex=Sums.index(max(Sums)) #l'indice où on doit placer la pub ; correspond à l'indice ou on peut obtient une somme maximale des tm_frda
      Sums.sort(reverse=True)
      maxSum = Sums[0]

    #On retourne l'indice (%tm-frda) à partir dequel on doit placer notre pub et la somme associée
    return beginningIndex,maxSum


#####    #######   ######   ######    #####    #######   ######   ######     #####    #######   ######   ######


def LocalizePubs(tm_time,tm_fedra,Pubs,tabIsVaccant,dureeInterPubs):

    """
    La classe LocalizePubs esr reponsable de mettre les pubs dans les bonnes places ; <en commencant par la pub la plus longue>
    Elle associe comme argument: La liste des valeurs temporelles,la liste des taux de frda, la liste qui rensigne si une case
    est utilisable pour placer la pub ou non
    La fonction LocalizePubs est responsable de placer les pubs en appelant la fonction MaxSum pour chaqu'une d'elles

       Cette fonction sert à :
                * Placer la pub ; En en faisant le traitement sur tabPlaceUsed pour qu'on definit la cases ou en va placer la pub
            et les 20 minutes d’avant et d’après comme non utilisable
                * Retourner une liste avec les données/infos des pubs (placées ou non)
"""
    somme=0
    tab=list(tm_fedra) #on fait une copie de la liste tm_frda pour que cette derniere ne change pas lors de traitement ci-dessous
    pubPlacementInfos=[] #une liste des info de placement correspondante à la pub designée
    pubsInfoList = []
    pubsSum=0
    #On va effectuer le traitement pour chaque pub de la liste donnée
    for i in range(len(Pubs)):
        duration0=Pubs[i].duration
        #recuperer la position et la somme maximale de la pub si elle existe
        pubBeginningIndex, maxSum=MaxSum(tab,duration0,Pubs[i].title,tabIsVaccant)
        #preparer une liste qui contient les infos importante sur le positionnement de notre pub
        pubPlacementInfos.append(Pubs[i].title)
        pubPlacementInfos.append(Pubs[i].duration)
        pubPlacementInfos.append(pubBeginningIndex)
        pubPlacementInfos.append(maxSum)
        #Ajouter la liste des info de la pub correspondante à 'i' à la liste des infos de toutes les pubs
        pubsInfoList.append(pubPlacementInfos)
        Pubs[i].set_isLocated(True)
        Pubs[i].set_index(pubBeginningIndex)
        if(pubBeginningIndex==None):
            Pubs[i].set_timeToBegin(None)
        else:
           Pubs[i].set_timeToBegin(tm_time[pubBeginningIndex])
           pubsSum = pubsSum + maxSum
        pubPlacementInfos = []
        #if maxSum == None : print(Pubs[i].title+'has no place')
        if (pubBeginningIndex != None):
            for h in range(duration0):
                tab[h + int(pubBeginningIndex)] = 0
                tabIsVaccant[h + int(pubBeginningIndex)] = False
            #Pour la partie gauche
            if (pubBeginningIndex>(dureeInterPubs)):
                for h in range(dureeInterPubs):
                    #la partie gauche
                    tabIsVaccant[int(pubBeginningIndex)-h] = False
            else:
                for h in range(pubBeginningIndex):
                    tabIsVaccant[h] = False
            #la partie droite
            if (pubBeginningIndex+duration0<len(tab)-dureeInterPubs):
                for h in range(dureeInterPubs):
                    tabIsVaccant[int(pubBeginningIndex) + h + duration0] = False
            else:
                for h in range(len(tab)-pubBeginningIndex-duration0):
                   tabIsVaccant[pubBeginningIndex+duration0+h] = False

#La fonction va retourner : l
    return pubsInfoList,pubsSum




#####    #######   ######   ######    #####    #######   ######   ######     #####    #######   ######   ######
