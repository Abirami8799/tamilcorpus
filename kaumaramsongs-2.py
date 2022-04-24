import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import time


driver=webdriver.Chrome()

#driver.get('https://www.kaumaram.com/audio_k/kcaudio.html')
#driver.get('https://www.kaumaram.com/audio_k/kpaudio.html')
driver.get('https://www.kaumaram.com/audio_k/dsaudio.html')

next_page=True


# using next button
while next_page:
      url=driver.current_url
      link_down = driver.find_elements_by_link_text('பதிவிறக்க')
      for i in link_down:
          i.click()
      data=requests.get(url)
      obj=BeautifulSoup(data.content,features='html.parser')
      bookname= obj.find('table',attrs={'class':'tbl04d'})
      sub_url= bookname.find('td',attrs={'class':'td20 tdc'})
      try:
          next_page = sub_url.findAll('a')
          next_url = next_page[-1]
          value = next_url.get('href')
          new_value = 'https://www.kaumaram.com/audio_k/'+value
          st = driver.get(new_value)
      except:
          break


