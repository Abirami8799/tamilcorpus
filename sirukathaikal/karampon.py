import requests
from bs4 import BeautifulSoup
import re
import os

a='சிறுகதைகள்'
os.mkdir(a)

s=[]
for total_pg in range(1,3):
    data=requests.get('http://karampon.net/home/archives/category/sirukathaikal/page/'+str(total_pg))
    obj=BeautifulSoup(data.content,features='html.parser')
    for j in obj.findAll('article'):
        link=j.find('a')['href']
        s.append(link)

for total_pg in s:
    data=requests.get(total_pg)
    obj=BeautifulSoup(data.content,features='html.parser')
    headline=obj.find('h1',attrs={'class':'entry-title'}).get_text()
    title=re.sub('\s*','',headline)
    content=obj.find('div',attrs={'class':'entry-content clearfix'})
    file1=open(os.path.realpath(a)+'/'+title+'.txt','w',encoding='utf-8')
    for z in content.findAll('p'):
        value=z.get_text()
        file1.writelines("%s\n"%value)
        

