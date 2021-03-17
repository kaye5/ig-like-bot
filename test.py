from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import waitFor,getConfig,logger
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))    

browser = webdriver.Firefox(executable_path=os.path.join(THIS_FOLDER, 'geckodriver.exe'))
browser.get('https://www.instagram.com/explore/tags/ui/')
browser.set_window_size(600,728)


for i in range(1,4) : 
    element = browser.find_element_by_xpath(f'/html/body/div[1]/section/main/article/div[1]/div/div/div[' + str(i) +']').page_source()
    print(i,element)
