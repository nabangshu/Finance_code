## This is a program to scrape the names of all the listed companies in NASDAQ and NSYSE.
## The website used is not ideal. I am working on a more official website.

import requests
import numpy as np
import string
import bs4

alphabet=list(string.ascii_uppercase)
alphabet.append('0')

company_list=[]
company_symbols=[]
for i in alphabet:
    res=requests.get('https://www.advfn.com/nasdaq/nasdaq.asp?companies=' + i)
    soup=bs4.BeautifulSoup(res.text, "lxml")
    html_list=soup.select('table')[4].select('tr')[2:]
    
    for i in range(len(html_list)):
        try:
            link=html_list[i].select('a')[2].get('href')
            res=requests.get(link)
            soup=bs4.BeautifulSoup(res.text, "lxml")
            temp=soup.find("div", {"class": "TableElement"}).find('b')
            temp=str(temp)
            if (temp.split('(')[1].split(')')[0]=='delisted'):
                continue
            test=html_list[i].select('a')[0]
            test=str(test)
            company_list.append(test.split('>')[1].split('<')[0])
            test=html_list[i].select('a')[1]
            test=str(test)
            company_symbols.append(test.split('>')[1].split('<')[0])
        except:
            continue
company_symbols=np.array(company_symbols).reshape(len(company_symbols),1)
company_list=np.array(company_list).reshape(len(company_list),1)
companies=np.hstack((company_list,company_symbols))
print(companies)

company_list_NYSE=[]
company_symbols_NYSE=[]
for i in alphabet:
    res=requests.get('https://www.advfn.com/nyse/newyorkstockexchange.asp?companies=' + i)
    soup=bs4.BeautifulSoup(res.text, "lxml")
    html_list=soup.select('table')[4].select('tr')[2:]
    
    for i in range(len(html_list)):
        try:
            link=html_list[i].select('a')[2].get('href')
            res=requests.get(link)
            soup=bs4.BeautifulSoup(res.text, "lxml")
            temp=soup.find("div", {"class": "TableElement"}).find('b')
            temp=str(temp)
            if (temp.split('(')[1].split(')')[0]=='delisted'):
                continue
            test=html_list[i].select('a')[0]
            test=str(test)
            company_list_NYSE.append(test.split('>')[1].split('<')[0])
            test=html_list[i].select('a')[1]
            test=str(test)
            company_symbols_NYSE.append(test.split('>')[1].split('<')[0])
        except:
            continue
company_symbols_NYSE=np.array(company_symbols_NYSE).reshape(len(company_symbols_NYSE),1)
company_list_NYSE=np.array(company_list_NYSE).reshape(len(company_list_NYSE),1)
companies_NYSE=np.hstack((company_list_NYSE,company_symbols_NYSE))
print(companies_NYSE)