from random import randint, choice
from string import ascii_lowercase
from time import sleep
from webbrowser import open

urlCharacters = list()
letters = ascii_lowercase
goback = True
while goback is True:
    quanturl = (input('How many links do you wants?'))
    if quanturl.isnumeric():
        break
    else:
        print('\033[31mPlease, only type in numbers.\033[m')
        goback = True
for c in range(0, int(quanturl)):
    for cont in range(0, 5):
        chosenLetter = choice(letters)
        urlCharacters.append(chosenLetter)
    urlCharacters = ''.join(urlCharacters)
    fullUrl = 'https://prnt.sc/' + urlCharacters + str(randint(0, 9))
    print(fullUrl)
    open(fullUrl)
    sleep(0.1)
    urlCharacters = list()