
def condition3Satisfaction(tabEmission,pubTimeToBegin,pubDuree):


   return
def MaxSumIntraEmission(tabEmission,duration,title,tabIsPlaceVaccant):
    #avec tabEmission= tm_fdra[Program.index:Pub.index+duree]

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
    while s<(len(tabEmission)-duration):
        # note : on doit etre capable de placer une pub à la fin
      sum = 0
      condition=True
     #Voir si c'est possible de placer la pub dans l'indice s ou non ; condition = True : on peux sinon on ne peut pas
      if (tabIsPlaceVaccant[s]==True)&&(PubsDurationPerHour):
          if False in tabIsPlaceVaccant[s:s+duration-1] : condition=False
      else :   # si la case est déjà pris par un traitement ultérieur (non disponible)
          condition= False
          # si on peut placer la pub à partir de l'indice s on calcule la somme des valeurs tm_frda correspondantes
      if(condition==True):
          for i in range(duration):
              sum = sum + tabEmission[s + i]
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


#####    #######   ######   ##