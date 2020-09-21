from urllib.request import urlopen
import argparse
import requests as req
import os
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
search_term = '여자 얼굴'
url = "https://www.google.co.in/search?q="+search_term+"&tbm=isch"
browser = webdriver.Chrome("D:/driver/chromedriver.exe")
browser.get(url)
for i in range(1000):
    browser.execute_script('window.scrollBy(0,10000)')
a = browser.find_elements_by_class_name("rg_i.Q4LuWd")
print(len(a))
for idx,i in enumerate(a):
    img = i.get_attribute("src")
    try:
        raw_img = urllib.request.urlopen(img).read()
    except:
        continue
    File = open("D:/woman/"+str(idx)+".png","wb")
    File.write(raw_img)
    File.close()