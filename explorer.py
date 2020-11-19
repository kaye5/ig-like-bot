from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import waitFor,getConfig
import random
import os




def itterateBot(count) : 
    waitFor(300,400,"Load feed")
    explorerBtn = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a")
    explorerBtn.send_keys(Keys.RETURN)
    waitFor(500,600,"Load Explorer")
    firstPost = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a")
    firstPost.send_keys(Keys.RETURN)    
    for _ in range(0,count) : 
        waitFor(300,800,"Load Post")
        slidePic()
        wantFollow()
        pressLike()        
        waitFor(150,250,"Next Img")
        browser.execute_script('document.getElementsByClassName("_65Bje")[0].click()')

def wantFollow() : 
    number = random.randint(1,10)    
    if number % 2 == 0 :
        waitFor(150,250,"wait follow")        
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
    likeBtn = browser.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    likeBtn.send_keys(Keys.RETURN)

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

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

config = getConfig()

browser = webdriver.Firefox(executable_path=os.path.join(THIS_FOLDER, 'geckodriver.exe'))
browser.get("https://instagram.com")

username = config['username']
password = config['password']
count = config['count']
tag = config['tag']


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
itterateBot(10)

print("Follow Total",str(followCount))