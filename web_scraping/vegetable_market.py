import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
r = requests.get("http://www.hopcoms.kar.nic.in/(S(vks0rmawn5a2uf55i2gpl3zo))/RateList.aspx")
soup = BeautifulSoup(r.content,"html.parser")

#get the table where the values are stored.
table = soup.find_all("table",cellspacing="0",rules="all",id="ctl00_LC_grid1")
#going to numbers
for veg_1 in table:
    veg_2 = soup.find_all("span")

#get the date
for i in veg_2:
    date = soup.find("span",id="ctl00_LC_DateText").text
date = date.strip("Last Updated Date: ")

veg = []
veg_num = []
veg_name = []
for i in veg_2:
    veg.append(i.text)







