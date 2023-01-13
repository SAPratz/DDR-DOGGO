#this function identifies the parents of a dog in PDB, and returns the URL of the mother and father in PDB to be handled for other functions. If there are no parents found, the returned URL will be Horand von Schwaben, which will exceed any isTooOld.py criteria, and will terminate searching that line at the missing parent in PDB.

def findParents(child_url_string = ''):

    import requests
    from bs4 import BeautifulSoup


    if (child_url_string == ''):
        MainDogURL = input("Enter Dog's PDB Website URL: ")
        r = requests.get(MainDogURL)
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        #print(soup)

        mom_dad = []
        r = 0
        for d in soup.findAll('td', attrs={'rowspan':'4'}):
            #print(d)
            if (r == 0):
                fatherURL = d.a
            if (r == 1):
                motherURL = d.a
            r = r+1


        if fatherURL == None:
            fatherLink = 'http://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=462004-horand-von-schwaben'
        else:
            fatherPath = fatherURL.get('href')
            fatherLink = ["http://www.pedigreedatabase.com" + fatherPath]
        if motherURL == None:
            motherLink = 'http://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=462004-horand-von-schwaben'
        else:
            motherPath = motherURL.get('href')
            motherLink = ["http://www.pedigreedatabase.com" + motherPath]

        return [fatherLink, motherLink]

    else:
        MainDogURL = child_url_string
        r = requests.get(MainDogURL)
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        # print(soup)

        mom_dad = []
        r = 0
        for d in soup.findAll('td', attrs={'rowspan': '4'}):
            # print(d)
            if (r == 0):
                fatherURL = d.a
            if (r == 1):
                motherURL = d.a
            r = r + 1

        # print(fatherURL)
        # print(motherURL)

        if fatherURL == None:
            fatherLink = 'http://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=462004-horand-von-schwaben'
        else:
            fatherPath = fatherURL.get('href')
            fatherLink = ["http://www.pedigreedatabase.com" + fatherPath]
        if motherURL == None:
            motherLink = 'http://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=462004-horand-von-schwaben'
        else:
            motherPath = motherURL.get('href')
            motherLink = ["http://www.pedigreedatabase.com" + motherPath]

        return [fatherLink, motherLink]

#print(findParents())
