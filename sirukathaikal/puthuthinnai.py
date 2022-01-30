import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os

a='puthuthinnai'
os.mkdir(a)

s=[]

#add a number to a filename if it already exists
def check_filename(c):
    j=1
    if os.path.exists(c+'.txt'):
       while True:
             b=c+'-'+str(j)+'.txt'
             if os.path.exists(b):
                j += 1
             else:
                return b
                break
    else:
       return c
    
#extract title URL
for i in range(1,234):
    data=requests.get('https://puthu.thinnai.com/category/stories/page/'+str(i))
    obj=BeautifulSoup(data.content,features='html.parser')
    blog= obj.find('div',attrs={'class':'blog-lists-blog clearfix'})
    for i in blog.findAll('div',attrs={'class':'blogposts-wrapper clearfix'}):
        for j in i.findAll('div',attrs={'class':'blogposts-inner'}):
            p=j.find('a')['href']
            s.append(p)
            

for total_pg in s:    
    try:
       data=requests.get(total_pg)
       obj=BeautifulSoup(data.content,features='html.parser')
       headline=obj.find('h1',attrs={'class':'entry-title'}).get_text()
       title=re.sub('\s*','',headline)
       content=obj.find('div',attrs={'class':'post_content entry-content'})

       try:

           c=os.path.realpath(a)+'/'+title 
           filename=check_filename(c)
           file1=open(filename,'w',encoding='utf-8')
           for z in content:
               value=z.text
               file1.writelines("%s\n"%value)
       except OSError as exc:
            if exc.errno==36:
               large_title=title.partition('.')
               new=large_title[0]
               file1=open(os.path.realpath(a)+'/'+new+'.txt','w',encoding='utf-8')
               for z in content:
                   value=z.text
                   file1.writelines("%s\n"%value)
    except:
       print(total_pg)





















