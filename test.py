from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
import decimal
import os
import json
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


browser = webdriver.Firefox(executable_path=os.path.join(THIS_FOLDER, 'geckodriver.exe'))
browser.get("https://www.instagram.com/explore/tags/webdesign/")
count = 40
post = set()
while(True) :
    postCount = len(post)
    if(postCount < count) : 
        for posts in browser.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div/div/a') : 
            print(posts.get_attribute("href"))
            post.add(posts.get_attribute("href"))
        browser.execute_script("window.scrollBy(0, 1000)") 
    else : 
        break
    waitFor()
    