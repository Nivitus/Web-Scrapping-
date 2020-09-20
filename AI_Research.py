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
pages = 1
url = "http://airesearch.com/category/ai-research-papers/"
def getdata(start_url,pgs):
    current = 1
    urls = browser.get(start_url)
    data = {}
    df = pd.DataFrame(columns=['Paper_Title','Paper_URL','Post_Year','Abstract','Author_Name','Author_URL','Research_Area'])
    while current < pages:
        articles = browser.find_elements_by_xpath('//*[@id="primary"]')
        for paper in articles:
            for b in paper.find_elements_by_xpath('//*[@id="post-357"]'):
                data['Paper_Title'] = b.find_elements_by_xpath('//*[@id="post-357"]/header/h2/a/text()')[0].text
                data['Paper_URL'] = b.find_elements_by_xpath('//*[@id="post-357"]/header/h2/a')[0].text
                data['Post_Year'] = b.find_elements_by_xpath('//*[@id="post-334"]/footer/span[1]/a/time[1]')[0].text
                data['Abstract'] = b.find_elements_by_xpath('//*[@id="post-334"]/div/p[2]')[0].text
                data['Author_Name'] = b.find_elements_by_xpath('//*[@id="post-334"]/footer/span[3]/a[2]')[0].text
                data['Author_URL'] = b.find_elements_by_xpath('//*[@id="post-334"]/footer/span[3]/a[5]')[0].text
                data['Research_Area'] = b.find_elements_by_xpath('//*[@id="post-326"]/footer/span[3]/a[1]')[0].text
                df = df.append(data, ignore_index=True)
               
            current += 1
       
    return df 


getdata(url, pages).to_excel('/home/nivitus/AiResearch.xls')
