import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import time


# Download songs using page count

driver=webdriver.Chrome()
driver.get('https://www.kaumaram.com/audio_k/rmaudio.html')

next_page=True
a = 2

while next_page:   
      url=driver.current_url

      link_down_na = driver.find_elements_by_link_text('download #N/A')
      link_down = driver.find_elements_by_link_text('பதிவிறக்க')
      
      if len(link_down)>0 and len(link_down_na) == 0:
         for i in link_down:
             i.click()
         try:
            value = ('%02d' % a)
            new_value = 'https://www.kaumaram.com/audio_k/rmaudio'+value+'.html'
            st = driver.get(new_value)
            a = a+1
         except:
            break          
      else:
          value = ('%02d' % a)
          new_value = 'https://www.kaumaram.com/audio_k/rmaudio'+value+'.html'
          st = driver.get(new_value)
          a = a+1




driver=webdriver.Chrome()
driver.get('https://www.kaumaram.com/audio_k/graudio.html')
#driver.get('https://www.kaumaram.com/audio_k/ctaudio.html')
#driver.get('https://www.kaumaram.com/audio_k/graudio.html')
#driver.get('https://www.kaumaram.com/audio_k/anaudio.html')
#driver.get('https://www.kaumaram.com/audio_k/skaudio.html')
#driver.get('https://www.kaumaram.com/audio_k/sjaudio.html')
#driver.get('https://www.kaumaram.com/audio_k/sjaudio.html')


next_page=True
a = 2
while next_page:   
      url=driver.current_url
      link_down = driver.find_elements_by_link_text('பதிவிறக்க')
      if len(link_down)>0:
         for i in link_down:
             i.click()
         try:
            value = ('%02d' % a)
            new_value = 'https://www.kaumaram.com/audio_k/graudio'+value+'.html'
            st = driver.get(new_value)
            a = a+1
         except:
            break
      else:
          break












      

