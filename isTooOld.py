def isTooOld(child_url_string = ''):

    import time
    import requests
    from bs4 import BeautifulSoup

    if child_url_string != '' and type(child_url_string) is list:
        child_url_string = child_url_string[0]

    if (child_url_string == ''):
        MainDogURL = input("Enter Dog's PDB Website URL: ")
        r = requests.get(MainDogURL)
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        #print(soup)
        time.sleep(.5)

        for d in soup.findAll('div', attrs={'class': 'box', 'id': 'dogherounit'}):
            #print(d.h4)
            reg_num = d.h4
            if reg_num == None:
                stringy = '2000'
            else:
                stringy = reg_num.string
            yearBorn = stringy[-4:]

        if int(yearBorn) < 1970:
            return True
        else:
            return False

    else:
        MainDogURL = child_url_string
        r = requests.get(MainDogURL)
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        # print(soup)
        time.sleep(.5)
        for d in soup.findAll('div', attrs={'class': 'box', 'id': 'dogherounit'}):
            #print(d.h4)
            reg_num = d.h4

            if reg_num == None:
                stringy = '2000'
            else:
                stringy = reg_num.string

            yearBorn = stringy[-4:]

        if int(yearBorn) < 1970:
            return True
        else:
            return False


#print(isTooOld("http://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=691-gockel-von-bern"))
#print(isTooOld())