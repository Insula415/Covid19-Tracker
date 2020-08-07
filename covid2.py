import bs4
import requests
from bs4 import BeautifulSoup

a=requests.get('https://www.worldometers.info/coronavirus/')
soup=bs4.BeautifulSoup(a.text,features="html.parser")

b=requests.get('https://www.worldometers.info/coronavirus/coronavirus-death-toll/')
bsoup=bs4.BeautifulSoup(b.text,features="html.parser")

updated = soup.find('div',{'style':'font-size:13px; color:#999; margin-top:5px; text-align:center'}).text

current = soup.find('div',{'content-inner'}).find('span').text

deaths = bsoup.find('div',{'class':'maincounter-number'}).find('span').text

print("Covid19 cases: "+current)
print("Covid19 deaths: "+deaths)
print(updated)
