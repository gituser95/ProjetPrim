
#ci-dessous est notre classe main() !!!!
import pub
import Program
from BasicFunctions import *
import xlrd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import time

# ouverture du fichier Excel ::::
wb = xlrd.open_workbook('p_prim.xlsx')
# feuilles dans le classeur
sheet_names =wb.sheet_names()
# # # # # #
#ici on va recuperer la tranche horaire pour construire la liste des durées de pubs par heure: (doit etre <12min)
xl_sheet = wb.sheet_by_index(0)
timeSlot = xl_sheet.cell(6,3).value.split('-')
PubsDurationPerHour=[]
startHour=(int)(timeSlot[0].split(':')[0])
EndHour=(int)(timeSlot[1].split(':')[0])
for hour in range(startHour,EndHour+1):
    hourInfo=[hour,0]
    PubsDurationPerHour.append(hourInfo)
tm_time, tm_frda, Pubsduration, Pubsname, Programsname, Programsduration, MaxNumOfPubs, ProgramGivenIndex=Sheet_reading(wb,0)
#ici on va recuperer la tranche horaire pour construire la liste des durées de pubs par heure: (doit etre <12min)
xl_sheet = wb.sheet_by_index(0)
Pubs=[]
Programs=[]
numPubs=len(Pubsduration)#reccupèrer le nombre des pubs
numEmission=len(Programsduration)
########################################
#la boucle while ci-dessous sert à appeler le constructeur pour définir les pubs et puis l'ajouter l'une après l'autre à la liste Pubs
i=0
while i<numPubs:
    pub0=pub.pub(Pubsduration[i],Pubsname[i])
    Pubs.append(pub0)
    i=i+1

j=0
while j<numEmission:
    program0=Program.program(Programsduration[j],Programsname[j],MaxNumOfPubs[j], ProgramGivenIndex[j])
    Programs.append(program0)
    j=j+1

Summs=[]
print(Programs)
#un tableau qui rensigne si on peux utiliser l'indice associé pour placer une pub ou non (False = on peut pas ; True = on peut)
tabIsPlaceVaccant=[True]*len(tm_frda)
print(len(tabIsPlaceVaccant))
dureeInterPubs=900
pubsInfoList,pubsSum=LocalizePubs(tm_time,tm_frda,Pubs,tabIsPlaceVaccant,dureeInterPubs)
print("La somme cumulée des audiences des pubs est :"+str(pubsSum))
#juste pour regler le code
# Tm_frdaGraph(tm_time,tm_frda,pubsInfoList)


