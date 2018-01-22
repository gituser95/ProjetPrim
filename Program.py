import datetime
import time

class program():

    """
    Classe qui représente une emission TV
    Attributs: - duree (en secondes /& heures)
               - titre
               -Nombre des pubs maximale
               -temps du debut
               -Nombre des pubs
               -Une liste des pubs
               -indice precedent
               - ...
    """

    def __init__(self, duree, titre,numPubsMax0,givenIndex):
        # le constructeur de la classe pub
        #######
        self.duree = duree #la durée de l'emission en secondes
        self.dureeInHH = str(datetime.timedelta(seconds=duree))#la durée de l'emission en format HH:MM:SS
        self.title = titre #le nom de l'emission
        self.numPubsMax=numPubsMax0
        self.numPubs=0 #nombre de pubs intra-emission(par defaut =0 avant traitement)
        self.timeToBegin=None #le temps de debut de l'émission
        self.givenIndex=givenIndex#l'index de l'emission donné dans le fichier excel
        self.PubsList= [] #Une liste qui contient les noms des pubs à mettre au milieu de l'emission
        self.InterSpace='/n'
    def __repr__(self):
        """Afficher une pub"""
        return ("{} - durée {}s - numMax {} - givenIndex {}".format(self.title, self.duree, self.numPubsMax, self.givenIndex))

    def get_numPubsMax(self):
        #obtenir le nombre des pubs intra l'emission
        return self.numPubsMax

    def get_numPubs(self):
        #obtenir le nombre des pubs intra l'emission
        return self.numPubs

    def get_duration(self):
        #obtenir la duree en secondes de la pub
        return self.duree

    def get_durationInHH(self):
        # obtenir la duree en format HH:MM:SS de la pub
        return self.dureeInHH

    def get_index(self):
        #obtenir l'indice de début de la pub placée % au differents tableaux
        return self.givenIndex

    def set_index(self,indice):
        # donner l'indice de début de la pub placée % au differents tableaux
        self.givenIndex=indice

    def get_timeToBegin(self):
        #obtenir le temps du debut de la pub proposé par l'algorithme
        return self.timeToBegin

    def set_timeToBegin(self,time):
        #donner le temps du debut de la pub proposé par l'algorithme
        if(time==None):
            self.timeToBegin=None
        else:
            self.timeToBegin=str(datetime.timedelta(seconds=time))