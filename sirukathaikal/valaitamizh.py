import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os

path='valaitamizh'
os.mkdir(path)

a=[]

def file_check(c):
    j=1
    z=c+'.txt'
    if os.path.exists(z):
       while True:
             b=c+'-'+str(j)+'.txt'
             if os.path.exists(b):
                j += 1
             else:
                return b
                break
    else:
       return z

for i in range(1,11):
     page_name='https://www.valaitamil.com/article_titles.php?cid=literature&sid=short-story&trd=&pg='+str(i)
     data=requests.get(page_name)
     obj=BeautifulSoup(data.content,features='html.parser')
     bookname= obj.find('div',attrs={'class':'home_content MT3'})
     table=bookname.find('tr')
     for i in table.findAll('table'):
         m=i.find('tr')
         n=m.find('td')
         s=n.find('a')['href']
         if s != 'index.php':
            a.append('https://www.valaitamil.com/'+s)
            

for sub_url in a:
    sub_link=requests.get(sub_url)
    sub_content=BeautifulSoup(sub_link.content, features='html.parser')
    link=sub_content.find('div',attrs={'class':'home_content MT3'})
    title=link.find('h1').text
    table=link.find('table')
    try:
       c=os.path.realpath(path)+'/'+title 
       filename=file_check(c)

       file1=open(filename,'w',encoding='utf-8')

       for z in link.findAll('p'):
           value=z.text
           file1.writelines("%s\n"%value)

    except:
        print(sub_url)
             

      
  

