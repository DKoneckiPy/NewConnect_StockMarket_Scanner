'''NewConnect'''
# Getting company data by ticker


#Library import

import pandas as pd 
import pandas_datareader as pdr
import datetime as dt
import numpy as np
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request
import csv

# First tool: scraping company data by ticker & drawing chart. Run & enter company ticker,year(format yyyy),month(format m),day(format d)

stock=input("Enter the name of the company(ticker):")
year=int(input("Enter the starting year(yyyy):"))
month=int(input("Enter the starting month(m):"))
day=int(input("Enter the starting day(d):"))

nc = pdr.get_data_stooq(stock+'.pl',start=dt.datetime(year,month,day))
dataframe = nc['Close'] 
dataframe.plot(figsize=(10,10))

"""#NewConnect market scanner"""

#Second tool: web scraping all NewConnect companies data from each page, joining tables, 
#filter setting (in this script daily change price(%) > 10%

"""## NewConnect components - scraping - DataFrame 1 (1-50)

"""

#Data source
URL =  'https://stooq.pl/q/i/?s=ncindex'

#html code from website
html = requests.get(URL)

#parsing html with BeautifulSoup
soup = BeautifulSoup(html.text, 'html.parser')
print(soup)

# checking table data
table = soup.find('table', attrs={'class': 'fth1'})
ilosc_wierszy = table.find_all('tr')
ilosc_wierszy

# row length in table except first row zliczenie liczby wierszy w tabeli, ale pominiecie pierwszego jako naglowka, wynikiem powinno byc 20
print('Liczba spółek', len(ilosc_wierszy)-1)

# creating list and add headline
wiersze = []
wiersze.append(['Symbol', 'Nazwa', 'Kurs', 'Zmiana', 'Zmiana', 'Zmiana 1r','Zmiana 1r', 'Wolumen', 'Data'])
print(wiersze)

# find all <td> loop
for wiersz in ilosc_wierszy:
    data = wiersz.find_all('td')
    # data checking
    if len(data) == 0:
        continue

    # column content to variable
    symbol = data[0].getText()
    nazwa = data[1].getText()
    kurs = data[2].getText()
    zmiana1 = data[3].getText()
    zmiana2 = data[4].getText()
    zmiana1r1 = data[5].getText()
    zmiana1r2 = data[6].getText()
    wolumen = data[7].getText()
    data = data[8].getText()
    

    # append result to wiersze
    wiersze.append([symbol, nazwa, kurs, zmiana1, zmiana2, zmiana1r1,zmiana1r2 , wolumen, data])

print(wiersze)

# Creating csv file and append output to fileTworzy plik csv 
with open('ncindex.csv','w', newline='') as plik_wynikowy:
    csv_output = csv.writer(plik_wynikowy)
    csv_output.writerows(wiersze)

ncindex = pd.read_csv('/content/ncindex.csv')
indexname = ncindex[ncindex['Symbol'] == 'NCINDEX'].index
ncindex.drop(indexname,inplace=True)
ncindex['Zmiana'] = ncindex['Zmiana'].str.rstrip('%').astype('float') 
ncindex.rename(columns={'Zmiana':'ZmianaD1(%)'},inplace=True)
ncindex.drop(columns=['Zmiana 1r','Zmiana.1','Zmiana 1r.1','Wolumen','Data'],inplace=True )
ncindex

# CREATING def 
def NCtable(i):
  #Data source
  URL =  'https://stooq.pl/q/i/?s=ncindex&l='+str(i)
  #html code from website
  html = requests.get(URL)
  #parsing html with BeautifulSoup
  soup = BeautifulSoup(html.text, 'html.parser')
  print(soup)
  # checking table data
  table = soup.find('table', attrs={'class': 'fth1'})
  ilosc_wierszy = table.find_all('tr')
  ilosc_wierszy
  # row length in table except first row zliczenie liczby wierszy w tabeli, ale pominiecie pierwszego jako naglowka, wynikiem powinno byc 20
  print('Liczba spółek', len(ilosc_wierszy)-1)
  # creating list and add headline
  wiersze = []
  wiersze.append(['Symbol', 'Nazwa', 'Kurs', 'Zmiana', 'Zmiana', 'Zmiana 1r','Zmiana 1r', 'Wolumen', 'Data'])
  # petla przeszukująca cala tabele
  for wiersz in ilosc_wierszy:
    data = wiersz.find_all('td')
    # sprawdz czy kolumny posiadaja dane
    if len(data) == 0:
        continue
    # column content to variable
    symbol = data[0].getText()
    nazwa = data[1].getText()
    kurs = data[2].getText()
    zmiana1 = data[3].getText()
    zmiana2 = data[4].getText()
    zmiana1r1 = data[5].getText()
    zmiana1r2 = data[6].getText()
    wolumen = data[7].getText()
    data = data[8].getText()   
    # append result to wiersze
    wiersze.append([symbol, nazwa, kurs, zmiana1, zmiana2, zmiana1r1,zmiana1r2 , wolumen, data])
  print(wiersze)
  return wiersze

"""## NewConnect components - scraping - DataFrame 2 (51-100) """

wiersze=NCtable(2)
  with open('ncindex2.csv','w', newline='') as plik_wynikowy:
    csv_output = csv.writer(plik_wynikowy)
    csv_output.writerows(wiersze)
  ncindex2 = pd.read_csv('/content/ncindex2.csv')
  indexname = ncindex2[ncindex2['Symbol'] == 'NCINDEX'].index
  ncindex2.drop(indexname,inplace=True)
  ncindex2['Zmiana'] = ncindex2['Zmiana'].str.rstrip('%').astype('float') 
  ncindex2.rename(columns={'Zmiana':'ZmianaD1(%)'},inplace=True)
  ncindex2.drop(columns=['Zmiana 1r','Zmiana.1','Zmiana 1r.1','Wolumen','Data'],inplace=True )
  ncindex2

"""## NewConnect components - scraping - DataFrame 3 (101-150)"""

wiersze=NCtable(3)

with open('ncindex3.csv','w', newline='') as plik_wynikowy:
    csv_output = csv.writer(plik_wynikowy)
    csv_output.writerows(wiersze)

ncindex3 = pd.read_csv('/content/ncindex3.csv')
indexname = ncindex3[ncindex3['Symbol'] == 'NCINDEX'].index
ncindex3.drop(indexname,inplace=True)
ncindex3['Zmiana'] = ncindex3['Zmiana'].str.rstrip('%').astype('float') 
ncindex3.rename(columns={'Zmiana':'Zmiana(%)'},inplace=True)
ncindex3.drop(columns=['Zmiana 1r','Zmiana.1','Zmiana 1r.1','Wolumen','Data'],inplace=True )
ncindex3

"""## NewConnect components - scraping - DataFrame 4 (151-200)"""

wiersze=NCtable(4)

with open('ncindex4.csv','w', newline='') as plik_wynikowy:
    csv_output = csv.writer(plik_wynikowy)
    csv_output.writerows(wiersze)

ncindex4 = pd.read_csv('/content/ncindex4.csv')
indexname = ncindex4[ncindex4['Symbol'] == 'NCINDEX'].index
ncindex4.drop(indexname,inplace=True)
ncindex4['Zmiana'] = ncindex4['Zmiana'].str.rstrip('%').astype('float') 
ncindex4.rename(columns={'Zmiana':'Zmiana(%)'},inplace=True)
ncindex4.drop(columns=['Zmiana 1r','Zmiana.1','Zmiana 1r.1','Wolumen','Data'],inplace=True )
ncindex4

"""## NewConnect components - scraping - DataFrame 5 (201-215)"""

wiersze=NCtable(5)

with open('ncindex5.csv','w', newline='') as plik_wynikowy:
    csv_output = csv.writer(plik_wynikowy)
    csv_output.writerows(wiersze)

ncindex5 = pd.read_csv('/content/ncindex5.csv')
indexname = ncindex5[ncindex5['Symbol'] == 'NCINDEX'].index
ncindex5.drop(indexname,inplace=True)
ncindex5['Zmiana'] = ncindex5['Zmiana'].str.rstrip('%').astype('float') 
ncindex5.rename(columns={'Zmiana':'Zmiana(%)'},inplace=True)
ncindex5.drop(columns=['Zmiana 1r','Zmiana.1','Zmiana 1r.1','Wolumen','Data'],inplace=True )
ncindex5

"""## Scanner -> ChangeD1(%)>20%"""

portfolio = pd.concat([ncindex,ncindex2,ncindex3, ncindex4, ncindex5],keys = ['ncindex','ncindex2','ncindex3','ncindex4','ncindex5'], names = ['Symbol','Number'])
portfolio

filtr = portfolio[portfolio['ZmianaD1(%)'] > 10]
filtr

nc_stocks = []

for i in filtr['Symbol']:
  nc_stocks.append(i+".pl")

nc = pdr.get_data_stooq(nc_stocks,start=dt.datetime(2020,1,1))
dataframe = nc['Close'] 
dataframe.plot(figsize=(10,10))
