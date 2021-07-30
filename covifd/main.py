from imports import *
from websites import *

updated = soup.find('div',{'style':'font-size:13px; color:#999; margin-top:5px; text-align:center'}).text

current = soup.find('div',{'content-inner'}).find('span').text

deaths = bsoup.find('div',{'class':'maincounter-number'}).find('span').text

def USA():
    America = csoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}USA{+}--------{")
    print(America)

def SouthAmerica():
    print("Please note that these aren't all the countries in South America")
    Brazil = dsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Brazil{+}--------{")
    print(Brazil)
    Argentina = esoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Argentina{+}--------{")
    print(Argentina)
    Colombia = fsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Colombia{+}--------{")
    print(Colombia)
    Ecuador = gsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Ecuador{+}--------{")
    print(Ecuador)
    Chile = hsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Chile{+}--------{")
    print(Chile)
    Peru = isoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Peru{+}--------{")
    print(Peru)
    Bolivia = jsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Bolivia{+}--------{")
    print(Bolivia)
    Guyana = ksoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Guyana{+}--------{")
    print(Guyana)
    Uruguay  = lsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Uruguay {+}--------{")
    print(Uruguay )
    Suriname  = msoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Suriname{+}--------{")
    print(Suriname)
    Paraguay  = nsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Paraguay{+}--------{")
    print(Paraguay)
    Frenchguiana  = osoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}French Guiana{+}--------{")
    print(Frenchguiana)
    Falklandislands  = psoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Falkland Islands{+}--------{")
    print(Falklandislands)
    Trinidad  = qsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Trinidad and Tobago{+}--------{")
    print(Trinidad)

def Europe():
    print("Please note that these aren't all the countries in Europe")
    France  = rsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}France{+}--------{")
    print(France)
    UK  = ssoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}UK{+}--------{")
    print(UK)
    Netherlands  = tsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Netherlands{+}--------{")
    print(Netherlands)
    Greece  = usoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Greece{+}--------{")
    print(Greece)
    Switzerland  = vsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Switzerland{+}--------{")
    print(Switzerland)
    Poland  = wsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Poland{+}--------{")
    print(Poland)
    Spain  = xsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Spain{+}--------{")
    print(Spain)
    Norway  = ysoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Norway{+}--------{")
    print(Norway)
    Iceland  = zsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Iceland{+}--------{")
    print(Iceland)
    Germany  = onesoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Germany{+}--------{")
    print(Germany)
    Italy  = twosoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Italy{+}--------{")
    print(Italy)

def Africa():
    print("Please note that these aren't all the countries in Africa")
    Kenya  = threesoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Kenya{+}--------{")
    print(Kenya)
    Uganda  = foursoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Uganda{+}--------{")
    print(Uganda)
    SouthAfrica  = fivesoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}South Africa{+}--------{")
    print(SouthAfrica)
    Nigeria  = sixsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Nigeria{+}--------{")
    print(Nigeria)

def Australia():
    Australia  = sevensoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Australia{+}--------{")
    print(Australia)

def Asia():
    print("Please note that these aren't all the countries in Asia")
    Japan  = eightsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Japan{+}--------{")
    print(Japan)
    India  = ninesoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}India{+}--------{")
    print(India)
    Russia  = tensoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Russia{+}--------{")
    print(Russia)
    Iran  = elevensoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Iran{+}--------{")
    print(Iran)
    Hongkong  = twelvesoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Hong Kong{+}--------{")
    print(Hongkong)

def Canada():
    Canada  = finalsoup.find('h2',{'style':'border: 1px solid red;border-radius:5px;background-color: rgba(255,255,0,.03);text-align: center;display: block;padding: 40px;'}).text
    print("}--------{+}Canada{+}--------{")
    print(Canada)

def All():
    print("You can find all the countries on the website below :0")
    print("https://www.worldometers.info/coronavirus/#countries")


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
while True:
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
        print("Thanks for using my program ~ Insula")
        exit()
    else:
        try:
            print(os.system(choice))
        except:
            pass

    if choice == "0":
        print("Thanks for using my program ~ Insula")
        break
