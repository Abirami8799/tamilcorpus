import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os


a='iraviesirukatai'
os.mkdir(a)

driver=webdriver.Chrome()
driver.get('https://iravie.com/category/சிறுகதை/')
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

next_page=True
while next_page:
      url=driver.current_url
      data=requests.get(url)
      obj=BeautifulSoup(data.content,features='html.parser')
      bookname= obj.find('main',attrs={'class':'site-main'})
      title=bookname.findAll('article')
      for i in title:
          sub_link=i.find('h2',attrs={'class':'entry-title'})
          url=sub_link.find('a')['href']
          s.append(url)
      try:
          st=driver.find_element_by_partial_link_text("Next")  
          st.click()
      except:
          break


for sub_url in s:
    sub_link=requests.get(sub_url)
    sub_content=BeautifulSoup(sub_link.content, features='html.parser')
    data= sub_content.findAll('article')
    for i in data:
        h=['h1','h2']
        sub_title=i.find(i in h,attrs={'class':'entry-title'}).text
        content=sub_content.find('div',attrs={'class':'entry-content'})
      
        try:
            c=os.path.realpath(a)+'/'+sub_title
            filename=check_filename(c)
            file1=open(filename,'w',encoding='utf-8')
            for z in content:
                value=z.text
                file1.writelines("%s\n"%value)
        except OSError as exc:
             if exc.errno==36:
                large_title=sub_title.partition(':')
                new=large_title[2]
                file1=open(os.path.realpath(a)+'/'+new+'.txt','w',encoding='utf-8')
                for z in content:
                    value=z.text
                    file1.writelines("%s\n"%value)



