import bs4
import os
import html5lib
from selenium import webdriver
import unittest
import pdfkit

# load the file
#Para desidentar: CTRL + SHIFT + BRACKET IZQ
writingArray=[]
for fname in os.listdir('C:/Users/DELL/Documents/Scripts de python/selenium_python/Automatic_Testing/DELLPC'):
    if ('TestResults') in fname:
        print('se encontro un archivo')
        with open(fname) as iterativedoc:
            txt=iterativedoc.read()
            soup=bs4.BeautifulSoup(txt,"html5lib")
            writingArray.append(soup)
            new_br= soup.new_tag('br')
            soup.body.append(new_br)
        with open("arshivomodificado.html", "w", encoding='utf-8') as file:
            for soups in writingArray:
                file.write(str(soups))

def  main():
    global driver
    #driver = webdriver.Firefox(executable_path=r"C:\Users\ricar\AppData\Local\Programs\Python\Python38\geckodriver.exe")
    driver = webdriver.Firefox(executable_path=r"C:\Users\DELL\Documents\Scripts de python\selenium_python\geckodriver.exe")
    driver.get("file:///C:/Users/DELL/Documents/Scripts%20de%20python/selenium_python/Automatic_Testing/DELLPC/arshivomodificado.html")
    viewButtons = driver.find_elements_by_css_selector(".btn-default")
    for button in viewButtons:
        button.click()
    with open('page.html', 'w') as f:
        f.write(driver.page_source)
        pdfkit.from_file(f, 'out.pdf')
#import pdfkit
#path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
#config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
#pdfkit.from_url("http://google.com", "rajul-url.pdf", configuration=config)
#pdfkit.from_file("output.xml","rajul-pdf.pdf", configuration=config)
if __name__ == "__main__":
    main()







