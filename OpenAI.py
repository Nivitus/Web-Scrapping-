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
        articles = browser.find_elements_by_xpath('//*[@id="post-projects"]')
        for paper in articles:
            for b in paper.find_elements_by_xpath('//*[@id="post-projects"]/div/div[1]/div[1]'):
                data['Paper_Title'] = b.find_elements_by_xpath('//*[@id="post-projects"]/div/div[1]/div[1]/a/div[2]/h5')[0].text
                data['Paper_URL'] = b.find_elements_by_xpath('//*[@id="post-projects"]/div/div[1]/div[1]/div/a')[0].text
            for o in paper.find_elements_by_xpath('//*[@id="post-projects"]/div/div[1]/div[1]/div/a'):    
                data['Post_Year'] = o.find_elements_by_xpath('//*[@id="abs"]/div[1]')[0].text
                data['Abstract'] = o.find_elements_by_xpath('//*[@id="abs"]/blockquote/span')[0].text
                data['Author_Name'] = o.find_elements_by_xpath('//*[@id="abs"]/div[2]/a[2]')[0].text
                data['Author_URL'] = o.find_elements_by_xpath('//*[@id="abs"]/div[2]/a[1]')[0].text
                data['Research_Area'] = b.find_elements_by_xpath('//*[@id="abs"]/div[3]/table/tbody/tr[2]/td[2]/span')[0].text
                df = df.append(data, ignore_index=True)
               
            current += 1
       
    return df 


getdata(url, pages).to_excel('/home/nivitus/OpenAi_Papers.xls')
