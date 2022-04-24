import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import time



driver=webdriver.Chrome()
driver.get('https://www.kaumaram.com/audio_k/bcaudio.html')
link_down = driver.find_element_by_link_text('இப்பாடலைக் கேட்க')
link_down.click()

next_page=True

while next_page:
    try:
        url=driver.current_url
        driver.execute_script('''
   
    			let aLink = document.createElement("a");
    			let videoSrc = document.querySelector("audio").childNodes[1].src;
    			aLink.href = videoSrc;
    			aLink.download = "";
    			aLink.click();
    			aLink.remove();
          ''')

        link_down = driver.find_element_by_xpath("//table[@class='tbl00 bgdrk']/tbody/tr/td[3]")
        src = link_down.find_elements_by_tag_name('a')
        next_page = src[-1]
        src = next_page.get_attribute('href')
        driver.get(src)
    except:
        break
