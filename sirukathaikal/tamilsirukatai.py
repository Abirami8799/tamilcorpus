import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os


a='tamilsirukatai'
os.mkdir(a)

driver=webdriver.Chrome()
driver.get('https://tamilsirukatai.blogspot.com/')
s=[]
next_page=True

while next_page:
      url=driver.current_url
      data=requests.get(url)
      obj=BeautifulSoup(data.content,features='html.parser')
      bookname= obj.findAll('div',attrs={'class':'post hentry'})

      for i in bookname:
          sub_url=i.find('a')['href']
          s.append(sub_url)
      try:
          st=driver.find_element_by_link_text('Older Posts')  
          st.click()
      except:
          break

for sub_url in s:
    sub_link=requests.get(sub_url)
    sub_content=BeautifulSoup(sub_link.content, features='html.parser')
    headline=sub_content.find('h1',attrs={'class':'post-title entry-title'}).text
    title=re.sub('\s*','',headline)
    content=sub_content.find('div',attrs={'class':'post-body entry-content'})
    file1=open(os.path.realpath(a)+'/'+title+'.txt','w',encoding='utf-8')
    for z in content:
        end_text='Home'
        value=z.text
        value=value.replace(end_text,'')
        file1.writelines("%s\n"%value)



      

