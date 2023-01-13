#this function will take a dog's URL and determine if the registration number of the dog is a DDR registration number. If there is no registration number listed, the program will set the value to 'RANDOM_PLACEHOLDER' and will not count that dog DDR until a DDR registration number is listed on a parent in PDB.

def isDDR(child_url_string = ''):

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

        for d in soup.findAll('div', attrs={'class':'box','id':'dogherounit'}):
            #print(d.i)
            reg_num = d.i
            if reg_num == None:
                stringy = 'RANDOM_PLACEHOLDER'
            else:
                stringy = reg_num.string

        if (stringy.find('DDR') == 0):
            return True
        else:
            return False

    else:
        MainDogURL = child_url_string
        r = requests.get(MainDogURL)
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        # print(soup)

        for d in soup.findAll('div', attrs={'class': 'box', 'id': 'dogherounit'}):
            #print(d.i)
            reg_num = d.i
            if reg_num == None:
                stringy = 'RANDOM_PLACEHOLDER'
            else:
                stringy = reg_num.string

        if (stringy.find('DDR') == 0):
            return True
        else:
            return False


#print(isDDR("http://www.pedigreedatabase.com/german_shepherd_dog/dog.html?id=120158-draga-aus-der-brigittenklause"))
#print(isDDR())
