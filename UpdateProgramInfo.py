from bs4 import BeautifulSoup
import requests
import sys

def updateProgram():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    programsList = []

    r=requests.get("https://www.btv.bg/programata/")
    r.encoding = r.apparent_encoding
   # print r.text
    soup = BeautifulSoup(r.text, features="html5lib")
    #programs = soup.find_all('div', {'class': 'channel-schedule-wrapper'})
    for each_div in soup.findAll('div', {'class': 'channel-schedule-wrapper'}):
        #print each_div
        for eachLi in each_div.findAll('li'):
            name = (eachLi.findNext('span', {'class': 'title'})).text.strip()
            startTime = eachLi.findNext('span', {'class': 'time'}).text.strip()
            print name
            programsList.append({"name": name, "start_time": startTime})
        break

    print programsList
