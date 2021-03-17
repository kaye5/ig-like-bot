from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import waitFor,getConfig,logger
from IGBot import IGBot
import random

following = []
def initExplorerLikeBot(count,tag) :
    search(tag)
    getPost(count)

def getPost(count) :    
    firstPost = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a")
    firstPost.send_keys(Keys.RETURN)    
    for _ in range(0,count) : 
        waitFor(300,800,"Load Post")
        try:            
            slidePic()
            wantFollow()
            pressLike()                                
        except :
            logger("Something went wrong")
            pass        
        waitFor(150,250,"Next Img")
        browser.execute_script('document.getElementsByClassName("_65Bje")[0].click()')

def wantFollow() : 
    number = random.randint(1,10)    
    if number % 2 == 0 :
        waitFor(150,250,"wait follow")        
        user = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").get_attribute("href")
        logger("Followed",user)
        following.append(user)
        follow = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
        follow.send_keys(Keys.RETURN)

def slidePic() : 
    number = random.randint(1,3)
    try:
        for _ in range (0,number) : 
            waitFor(500,350,"next slide")
            nextSlide = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div[1]/div[2]/div/button")
            nextSlide.send_keys(Keys.RETURN)
    except :
        return

def pressLike() : 
    waitFor(150,350,"wait for like")
    likeBtn = browser.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    likeBtn.send_keys(Keys.RETURN)

def search(tag) : 
    waitFor(300,400,"ig feed load")
    input = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    input.send_keys(tag)
    waitFor(200,300,"wait for search")
    link = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
    link.send_keys(Keys.RETURN)
    waitFor(600,700,"get search tag")

config = getConfig()    
browser = IGBot().getBotBrowser()
count = config['count']
tag = config['tag']

initExplorerLikeBot(count,tag)

logger("Followed total",str(len(following)))
print(following)