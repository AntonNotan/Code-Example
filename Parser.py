import urllib.request
from bs4 import BeautifulSoup

url="http://www.cbr.ru/scripts/XML_daily.asp"
webFile = urllib.request.urlopen(url)
data = webFile.read()
soup=BeautifulSoup(data, 'lxml')
table=soup.findAll('valute')
maxim = 0
minim = 10000

for i in table:
    if float(i.text[len(i.text)-7:len(i.text)].replace(',','.'))>maxim:
        maxim=float(i.text[len(i.text)-7:len(i.text)].replace(',','.'))
        maxvalute=i.find('name').text

    if float(i.text[len(i.text)-7:len(i.text)].replace(',','.'))<minim:
        minim=float(i.text[len(i.text)-7:len(i.text)].replace(',','.'))
        minvalute=i.find('name').text
if minvalute[len(minvalute)-1:len(minvalute)]=='а':
    print('Наименьшая валюта -'+minvalute.replace('х','й')+' равна '+str(minim)+' рублей')
else:
    print('Наименьшая валюта -' + minvalute.replace('х', 'й') + ' равен ' + str(minim) + ' рублей')
if maxvalute[len(minvalute)-1:len(minvalute)]=='а':
    print('Наибольшая валюта -'+maxvalute.replace('х','й')+' равна '+str(maxim)+' рублей')
else:
    print('Наибольшая валюта -' + maxvalute.replace('х', 'й') + ' равен ' + str(maxim) + ' рублей')
