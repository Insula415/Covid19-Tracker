import bs4
import requests
from bs4 import BeautifulSoup

################################################################################
def USA():
    America = csoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}USA{+}--------{")
    print(America)

def SouthAmerica():
    print("Please note that these aren't all the countries in South America")
    Brazil = dsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Brazil{+}--------{")
    print(Brazil)
    Argentina = esoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Argentina{+}--------{")
    print(Argentina)
    Colombia = fsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Colombia{+}--------{")
    print(Colombia)
    Ecuador = gsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Ecuador{+}--------{")
    print(Ecuador)
    Chile = hsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Chile{+}--------{")
    print(Chile)
    Peru = isoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Peru{+}--------{")
    print(Peru)
    Bolivia = jsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Bolivia{+}--------{")
    print(Bolivia)
    Guyana = ksoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Guyana{+}--------{")
    print(Guyana)
    Uruguay  = lsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Uruguay {+}--------{")
    print(Uruguay )
    Suriname  = msoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Suriname{+}--------{")
    print(Suriname)
    Paraguay  = nsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Paraguay{+}--------{")
    print(Paraguay)
    Frenchguiana  = osoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}French Guiana{+}--------{")
    print(Frenchguiana)
    Falklandislands  = psoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Falkland Islands{+}--------{")
    print(Falklandislands)
    Trinidad  = qsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Trinidad and Tobago{+}--------{")
    print(Trinidad)

def Europe():
    print("Please note that these aren't all the countries in Europe")
    France  = rsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}France{+}--------{")
    print(France)
    UK  = ssoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}UK{+}--------{")
    print(UK)
    Netherlands  = tsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Netherlands{+}--------{")
    print(Netherlands)
    Greece  = usoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Greece{+}--------{")
    print(Greece)
    Switzerland  = vsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Switzerland{+}--------{")
    print(Switzerland)
    Poland  = wsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Poland{+}--------{")
    print(Poland)
    Spain  = xsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Spain{+}--------{")
    print(Spain)
    Norway  = ysoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Norway{+}--------{")
    print(Norway)
    Iceland  = zsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Iceland{+}--------{")
    print(Iceland)
    Germany  = onesoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Germany{+}--------{")
    print(Germany)
    Italy  = twosoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Italy{+}--------{")
    print(Italy)

def Africa():
    print("Please note that these aren't all the countries in Africa")
    Kenya  = threesoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Kenya{+}--------{")
    print(Kenya)
    Uganda  = foursoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Uganda{+}--------{")
    print(Uganda)
    SouthAfrica  = fivesoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}South Africa{+}--------{")
    print(SouthAfrica)
    Nigeria  = sixsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Nigeria{+}--------{")
    print(Nigeria)

def Australia():
    Australia  = sevensoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Australia{+}--------{")
    print(Australia)

def Asia():
    print("Please note that these aren't all the countries in Asia")
    Japan  = eightsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Japan{+}--------{")
    print(Japan)
    India  = ninesoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}India{+}--------{")
    print(India)
    Russia  = tensoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Russia{+}--------{")
    print(Russia)
    Iran  = elevensoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Iran{+}--------{")
    print(Iran)
    Hongkong  = twelvesoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Hong Kong{+}--------{")
    print(Hongkong)

def Canada():
    Canada  = finalsoup.find('h2',{'style':'border: 1px solid red;text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Canada{+}--------{")
    print(Canada)

def All():
    print("You can find all the countries on the website below :0")
    print("https://www.worldometers.info/coronavirus/#countries")

################################################################################
###ALL WEBSITES
a=requests.get('https://www.worldometers.info/coronavirus/')
soup=bs4.BeautifulSoup(a.text,features="html.parser")

b=requests.get('https://www.worldometers.info/coronavirus/coronavirus-death-toll/')
bsoup=bs4.BeautifulSoup(b.text,features="html.parser")

###########USA
c=requests.get('https://virusncov.com/covid-statistics/usa')
csoup=bs4.BeautifulSoup(c.text,features="html.parser")
###########SouthAmerica
d=requests.get('https://virusncov.com/covid-statistics/brazil')
dsoup=bs4.BeautifulSoup(d.text,features="html.parser")

f=requests.get('https://virusncov.com/covid-statistics/colombia')
fsoup=bs4.BeautifulSoup(f.text,features="html.parser")

g=requests.get('https://virusncov.com/covid-statistics/ecuador')
gsoup=bs4.BeautifulSoup(g.text,features="html.parser")

e=requests.get('https://virusncov.com/covid-statistics/argentina')
esoup=bs4.BeautifulSoup(e.text,features="html.parser")

h=requests.get('https://virusncov.com/covid-statistics/Chile')
hsoup=bs4.BeautifulSoup(h.text,features="html.parser")

i=requests.get('https://virusncov.com/covid-statistics/Peru')
isoup=bs4.BeautifulSoup(i.text,features="html.parser")

j=requests.get('https://virusncov.com/covid-statistics/Bolivia')
jsoup=bs4.BeautifulSoup(j.text,features="html.parser")

k=requests.get('https://virusncov.com/covid-statistics/Guyana')
ksoup=bs4.BeautifulSoup(k.text,features="html.parser")

l=requests.get('https://virusncov.com/covid-statistics/Uruguay ')
lsoup=bs4.BeautifulSoup(l.text,features="html.parser")

m=requests.get('https://virusncov.com/covid-statistics/Suriname ')
msoup=bs4.BeautifulSoup(m.text,features="html.parser")

n=requests.get('https://virusncov.com/covid-statistics/Paraguay ')
nsoup=bs4.BeautifulSoup(n.text,features="html.parser")

o=requests.get('https://virusncov.com/covid-statistics/French-guiana ')
osoup=bs4.BeautifulSoup(o.text,features="html.parser")

p=requests.get('https://virusncov.com/covid-statistics/falkland-islands')
psoup=bs4.BeautifulSoup(p.text,features="html.parser")

q=requests.get('https://virusncov.com/covid-statistics/trinidad-and-tobago')
qsoup=bs4.BeautifulSoup(q.text,features="html.parser")
###########Europe
r=requests.get('https://virusncov.com/covid-statistics/France')
rsoup=bs4.BeautifulSoup(r.text,features="html.parser")

s=requests.get('https://virusncov.com/covid-statistics/UK')
ssoup=bs4.BeautifulSoup(s.text,features="html.parser")

t=requests.get('https://virusncov.com/covid-statistics/Netherlands')
tsoup=bs4.BeautifulSoup(t.text,features="html.parser")

u=requests.get('https://virusncov.com/covid-statistics/Greece')
usoup=bs4.BeautifulSoup(u.text,features="html.parser")

v=requests.get('https://virusncov.com/covid-statistics/Switzerland')
vsoup=bs4.BeautifulSoup(v.text,features="html.parser")

w=requests.get('https://virusncov.com/covid-statistics/Poland')
wsoup=bs4.BeautifulSoup(w.text,features="html.parser")

x=requests.get('https://virusncov.com/covid-statistics/Spain')
xsoup=bs4.BeautifulSoup(x.text,features="html.parser")

y=requests.get('https://virusncov.com/covid-statistics/Norway')
ysoup=bs4.BeautifulSoup(y.text,features="html.parser")

z=requests.get('https://virusncov.com/covid-statistics/Iceland')
zsoup=bs4.BeautifulSoup(z.text,features="html.parser")

one=requests.get('https://virusncov.com/covid-statistics/Germany')
onesoup=bs4.BeautifulSoup(one.text,features="html.parser")

two=requests.get('https://virusncov.com/covid-statistics/Italy')
twosoup=bs4.BeautifulSoup(two.text,features="html.parser")
#############Africa
three=requests.get('https://virusncov.com/covid-statistics/Kenya')
threesoup=bs4.BeautifulSoup(three.text,features="html.parser")

four=requests.get('https://virusncov.com/covid-statistics/Uganda')
foursoup=bs4.BeautifulSoup(four.text,features="html.parser")

five=requests.get('https://virusncov.com/covid-statistics/South-africa')
fivesoup=bs4.BeautifulSoup(five.text,features="html.parser")

six=requests.get('https://virusncov.com/covid-statistics/nigeria')
sixsoup=bs4.BeautifulSoup(six.text,features="html.parser")

seven=requests.get('https://virusncov.com/covid-statistics/Australia')
sevensoup=bs4.BeautifulSoup(seven.text,features="html.parser")

#############Asia
eight=requests.get('https://virusncov.com/covid-statistics/Japan')
eightsoup=bs4.BeautifulSoup(eight.text,features="html.parser")

nine=requests.get('https://virusncov.com/covid-statistics/India')
ninesoup=bs4.BeautifulSoup(nine.text,features="html.parser")

ten=requests.get('https://virusncov.com/covid-statistics/Russia')
tensoup=bs4.BeautifulSoup(ten.text,features="html.parser")

eleven=requests.get('https://virusncov.com/covid-statistics/Iran')
elevensoup=bs4.BeautifulSoup(eleven.text,features="html.parser")

twelve=requests.get('https://virusncov.com/covid-statistics/Hong-kong')
twelvesoup=bs4.BeautifulSoup(twelve.text,features="html.parser")
##############Canada
final=requests.get('https://virusncov.com/covid-statistics/Canada')
finalsoup=bs4.BeautifulSoup(final.text,features="html.parser")
################################################################################
#############main
updated = soup.find('div',{'style':'font-size:13px; color:#999; margin-top:5px; text-align:center'}).text

current = soup.find('div',{'content-inner'}).find('span').text

deaths = bsoup.find('div',{'class':'maincounter-number'}).find('span').text

################################################################################
print("Covid19 cases: "+current)
print("Covid19 deaths: "+deaths)
print(updated)
print("Down below is a list of options to find more about covid19 cases")
print ('''
{1}--USA
{2}--South America
{3}--Europe
{4}--Africa
{5}--Australia
{6}--Asia
{7}--Canada
{8}--ALL
{0}--EXIT\n
''')
choice=input("///:")
if choice == "1":
    USA()
elif choice == "2":
    SouthAmerica()
elif choice == "3":
    Europe()
elif choice == "4":
    Africa()
elif choice == "5":
    Australia()
elif choice == "6":
    Asia()
elif choice == "7":
    Canada()
elif choice == "8":
    All()
elif choice == "0":
    exit()
else:
    try:
        print(os.system(choice))
    except:
        pass
#########END
