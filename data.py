from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import json

authors=[]
quotes=[]

URL='https://www.goodreads.com/quotes/tag/motivation'
webpage=requests.get(URL)
soup=BeautifulSoup(webpage.text,'html.parser')
quoteText=soup.find_all('div',attrs={'class':'quoteText'})

for c in quoteText:
  quote=c.text.strip().split('\n')[0]
  quote=quote.replace('\u201c','')
  quote=quote.replace('\u201d','')
  quote=quote.replace('\u2019',"'")
  quote=quote.replace(',"','"')
  quotes.append(quote)
  author=c.find('span',attrs={'class':'authorOrTitle'}).text.strip()
  authors.append(author)

lst=[]
for i in range(len(authors)):
  lst.append([f'quote: {quotes[i]}', f'author: {authors[i]}'])
with open('quotes/quotes.json','w') as f:
  json.dump(lst,f,indent=8)