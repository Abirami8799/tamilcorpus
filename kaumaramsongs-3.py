import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import time


driver=webdriver.Chrome()
driver.get('https://www.kaumaram.com/audio_k/sgts01.html')

next_page=True
a = 2
s=[]
while next_page:
      url=driver.current_url
      link_down = driver.find_elements_by_xpath("//table[@class='tbl04b']/tbody/tr/td[2]/audio[1]")
      if len(link_down)>0:
         for i in link_down:
             src = i.get_attribute("outerHTML")
             webelement = BeautifulSoup(src,'html.parser')
             s.append('https://www.kaumaram.com'+webelement.source['src'])

         value = ('%02d' % a)
         new_value = 'https://www.kaumaram.com/audio_k/sgts'+value+'.html'
         st = driver.get(new_value)
         a = a+1
      else:
         break

print(len(s))

for i in s:
    driver.get(i)
    driver.execute_script('''
   
    			let aLink = document.createElement("a");
    			let videoSrc = document.querySelector("video").firstChild.src;
    			aLink.href = videoSrc;
    			aLink.download = "";
    			aLink.click();
    			aLink.remove();
          ''')
