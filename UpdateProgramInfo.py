from bs4 import BeautifulSoup
import requests
import sys
import json

def updateProgram():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    programsList = []

    #open btv web page html
    r=requests.get("https://www.btv.bg/programata/")
    r.encoding = r.apparent_encoding

    #parse the html
    soup = BeautifulSoup(r.text, features="html5lib")

    #go thorugh each btv media group chanel but we are interested only in the first one
    for each_div in soup.findAll('div', {'class': 'channel-schedule-wrapper'}):
        #each program is stored in a list, therefore iterate thorugh li-s
        for eachLi in each_div.findAll('li'):
            #get the name
            name = (eachLi.findNext('span', {'class': 'title'})).text.strip()
            #get the time
            startTime = eachLi.findNext('span', {'class': 'time'}).text.strip()
            print name
            prog = {}
            prog["name"] = name
            prog["start_time"] = startTime
            programsList.append(prog)
        break

    print programsList

    #post the collected info to the server
    r = requests.post('http://46.101.233.213/programs/2', json=programsList)
    print r.status_code #expecting 200
