from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import chrome
import pandas as pd
import os
import time


path = '/home/nivitus/WebScrap/chromedriver'
chrome_options = Options()
chrome_options.add_argument("-- incognito")
browser = webdriver.Chrome(path, options=chrome_options)
pages = 2
url = "https://www.elsevier.com/catalog?producttype=journal"
def getdata(start_url,pgs):
    current = 1
    urls = browser.get(start_url)
    data = {}
    df = pd.DataFrame(columns=['Paper_Title','Paper_URL','Abstract','Author_Name','Author_URL','Research_Area','Author_Address'])
    while current < pages:
        books = browser.find_elements_by_xpath('//*[@id="maincontent"]/section[1]/div[2]')
        for book in books:
            for b in book.find_elements_by_xpath('//*[@id="maincontent"]/section[1]/div[2]/div[1]'):
                data['Paper_Title'] = b.find_elements_by_xpath('//*[@id="maincontent"]/section[1]/div[2]/div[1]/div[1]/div/div[2]/h5/a/text()')[0].text
                data['Paper_URL'] = b.find_elements_by_xpath('//*[@id="maincontent"]/section[1]/div[2]/div[1]/div[1]/div/div[2]/h5/a')[0].text
                data['Post_Year'] = b.find_elements_by_xpath('//*[@id="maincontent"]/section[1]/div[2]/div[1]/div[1]/div/div[2]/div/p[2]/text()')[0].text
            for a in books.find_elements_by_xpath('//*[@id="maincontent"]/section[1]/div[2]/div[1]/div[2]/div/a'):    
                data['Abstract'] = a.find_elements_by_xpath('//*[@id="PublicationDescription"]/div[2]/p[1]/text()')[0].text
                data['Author_Name'] = a.find_elements_by_xpath('//*[@id="Title"]/div[2]/div/div[3]/span[2]')[0].text
                data['Author_URL'] = a.find_elements_by_xpath('//*[@id="Title"]/div[2]/div/div[3]/a')[0].text
                data['Research_Area'] = a.find_elements_by_xpath('//*[@id="PublicationDescription"]/div[2]/p[3]/em[2]/a')[0].text
            for add in books.find_elements_by_xpath('//*[@id="Title"]/div[2]/div/div[3]/a'):
                data['Author_Address'] = add.find_elements_by_xpath('//*[@id="Content1"]/div[1]/div[2]/span[2]/text()')[0].text
                df = df.append(data, ignore_index=True)
               
            current += 1
        next =  browser.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[2]/ul/li[7]/a')[0].click()
        
    return df 


getdata(url, pages).to_excel('/home/nivitus/Elsevier.xls')
