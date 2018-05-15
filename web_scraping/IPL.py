import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.cricbuzz.com/live-cricket-scorecard/20064/srh-vs-rr-4th-match-indian-premier-league-2018")
soup = BeautifulSoup(r.content,"html.parser")

## Getting into the 1st table
bat1 = soup.find("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr") ## Not  a list but an Object
##--------------------------------------------------------------------------------------------------------
## geting the player name
name = bat1.find_all("a",class_="cb-text-link") #A list
player_name = []
for i in name:
    player_name.append(i.text) # Getting the exact value from the list

##------------------------------------------------
## Getting the score
score = bat1.find_all("div", class_="cb-col cb-col-8 text-right text-bold")
s = []
for i in score:
    s.append(i.text)
##--------------------------------------------------
