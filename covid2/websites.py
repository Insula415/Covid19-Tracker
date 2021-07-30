from imports import *



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