import bs4
import os
import html5lib
from selenium import webdriver
import unittest
import pdfkit

writingArray=[]
for fname in os.listdir('C:/Users/DELL/Documents/Scripts de python/selenium_python/Automatic_Testing/'):
    if ('TestResults') in fname:
        print('se encontro un archivo')
        with open(fname) as iterativedoc:
            txt=iterativedoc.read()
            soup=bs4.BeautifulSoup(txt,"html5lib")
            writingArray.append(soup)
            new_br= soup.new_tag('br')
            soup.body.append(new_br)
        with open("allReports.html", "w", encoding='utf-8') as file:
            for soups in writingArray:
                file.write(str(soups))
    
