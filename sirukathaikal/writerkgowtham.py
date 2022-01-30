import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os


a='writerkgowtham'
os.mkdir(a)

driver=webdriver.Chrome()
driver.get('https://writerkgowtham.blogspot.com/')
s=[]
next_page=True

while next_page:
      url=driver.current_url
      data=requests.get(url)
      obj=BeautifulSoup(data.content,features='html.parser')
      bookname= obj.findAll('div',attrs={'class':'post hentry uncustomized-post-template'})

      for i in bookname:
          sub_url=i.find('h3',attrs={'class':'post-title entry-title'})
          url=sub_url.find('a')['href']
          s.append(url)
      try:
          st=driver.find_element_by_link_text('பழைய இடுகைகள்')  
          st.click()
      except:
          break

for sub_url in s:
    sub_link=requests.get(sub_url)
    sub_content=BeautifulSoup(sub_link.content, features='html.parser')
    data= sub_content.findAll('div',attrs={'class':'post hentry uncustomized-post-template'})
    for i in data:
        sub_title=i.find('h3',attrs={'class':'post-title entry-title'}).text
        title=re.sub('\s*','',sub_title)
        content=sub_content.find('div',attrs={'class':'post-body entry-content'})
        file1=open(os.path.realpath(a)+'/'+title+'.txt','w',encoding='utf-8')
        for z in content:
            value=z.text
            file1.writelines("%s\n"%value)

