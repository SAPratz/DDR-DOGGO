from isDDR import *
from findParents import *
from isTooOld import *

def findDDR(dogName = '', generationCount=0):
    print(dogName)
    if dogName != '' and type(dogName) is list:
        dogName = dogName[0]

    if dogName == '':
        dogName = input("Enter Dog's PDB Website URL: ")

    if isDDR(dogName):
        print('-'*generationCount, 'Found a DDR dog line in Generation ', generationCount, '. Dog name: ', dogName)
        return 1/(2**(generationCount))

    if isTooOld(dogName):
        print('Exhausted a line, no DDR dog found in ', generationCount, " generations")
        #print(dogName)
        return 0

    else:
        [fatherDog, motherDog] = findParents(dogName)
        if isDDR(fatherDog):
            print('-'*generationCount, 'Found a DDR dog line in Generation ', generationCount+1, '. Dog name: ', fatherDog)
            #print(fatherDog)
            DDRpercentDad = 1/(2**(generationCount))*.5
        else:
            DDRpercentDad = findDDR(fatherDog,generationCount+1)
        if isDDR(motherDog):
            print('-'*generationCount, 'Found a DDR dog line in Generation ', generationCount+1, '. Dog name: ', motherDog)
            #print(motherDog)
            DDRpercentMom = 1/(2**(generationCount))*.5
        else:
            DDRpercentMom = findDDR(motherDog,generationCount+1)

    return DDRpercentDad + DDRpercentMom