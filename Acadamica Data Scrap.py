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
url = "http://www.academia.edu/Documents/in/Artificial_Intelligence?page=1"
def getdata(start_url,pgs):
    current = 1
    urls = browser.get(start_url)
    data = {}
    df = pd.DataFrame(columns=['Paper_Title','Paper_URL','Abstract','Author_Name','Author_URL','Research_Area'])
    while current < pages:
        books = browser.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]')
        for book in books:
            for b in book.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[1]'):
                data['Paper_Title'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div')[0].text
                data['Paper_URL'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/a')[0].text
                data['Post_Year'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/ul/li[3]/ul/script')[0].text
                data['Abstract'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[2]')[0].text
                data['Author_Name'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/ul/li[3]/ul/li[1]/span/span/a')[0].text
                data['Author_URL'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/ul/li[3]/ul/li[1]/span/span/a')[0].text
                data['Research_Area'] = b.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/ul/li[3]/ul/li[5]/span/a[1]')[0].text
                df = df.append(data, ignore_index=True)
               
            current += 1
        next =  browser.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/div[1]/div[2]/ul/li[7]/a')[0].click()
        
    return df 


getdata(url, pages).to_excel('/home/nivitus/AI_Data.xls')
