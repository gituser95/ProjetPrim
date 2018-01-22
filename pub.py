import datetime
import time

class pub():

    """
    Classe qui représente une pub
    une pub = une publicité
    Attributs: - duree (en secondes /& heures)
               - titre
               -isLocated = T/F*
               -indice
               -temps du debut
               -
               - ...
    """

    def __init__(self, duree, titre):
        # le constructeur de la classe pub
        #######
        self.duration = duree #la durée de la pub en secondes
        self.durationInHH = str(datetime.timedelta(seconds=duree))#la durée de la pub en format HH:MM:SS
        self.title = titre #le nom de la pub
        self.isLocated= False #une pub n'est pas placée, au début, parmi les émissions (par défaut)
        self.index=None #l'indice de debut de la pub si elle est placée( à partir dequel on va placer la pub) dans le tableau des émissions
        self.timeToBegin=None #le temps de debut de l'émission de la pub si elle est déjà placée

    def __repr__(self):
        """Afficher une pub"""
        return ("{} - durée {}s".format(self.title, self.duree))

    def get_isLocated(self):
        ###Verifier si la pub est déjà placée ou non
        return self.isLocated

    def set_isLocated(self,variable):
        #placer la pub
       self.isLocated = variable

    def get_duration(self):
        #obtenir la duree en secondes de la pub
        return self.duration

    def get_durationInHH(self):
        # obtenir la duree en format HH:MM:SS de la pub
        return self.durationInHH

    def get_index(self):
        #obtenir l'indice de début de la pub placée % au differents tableaux
        return self.index

    def set_index(self,indice):
        # donner l'indice de début de la pub placée % au differents tableaux
        self.index=indice

    def get_timeToBegin(self):
        #obtenir le temps du debut de la pub proposé par l'algorithme
        return self.timeToBegin

    def set_timeToBegin(self,time):
        #donner le temps du debut de la pub proposé par l'algorithme
        if(time==None):
            self.timeToBegin=None
        else:
            self.timeToBegin=str(datetime.timedelta(seconds=time))