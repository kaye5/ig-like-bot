from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import waitFor,getConfig,logger
import random
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

following = []

def bot() :     
    waitFor(100,300,"input username")
    input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    input.send_keys(username)
    waitFor(50,200,"input password")
    input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    input.send_keys(password)
    btn = browser.find_element_by_class_name("sqdOP.y3zKF")
    btn.send_keys(Keys.RETURN)
    closeSaveLogin()
    closeNotif()
    runBot(count,tag)

def runBot(count,tag) :
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
    link = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]")
    link.send_keys(Keys.RETURN)
    waitFor(600,700,"get search tag")

def closeSaveLogin() : 
    waitFor(500,600,"close save login")
    try : 
        btn = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        btn.send_keys(Keys.RETURN)
        print("close")
    except : 
        print("skip close")

def closeNotif() : 
    waitFor(500,600,"close notif")
    try : 
        btn = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        btn.send_keys(Keys.RETURN)
        print("close notif")
    except : 
        print("skip close")


config = getConfig()

browser = webdriver.Firefox(executable_path=os.path.join(THIS_FOLDER, 'geckodriver.exe'))
browser.get("https://instagram.com")

username = config['username']
password = config['password']
count = config['count']
tag = config['tag']

bot()

logger("Followed total",str(len(following)))
print(following)