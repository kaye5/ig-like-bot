from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
import decimal
browser = webdriver.Firefox(executable_path=r"C:\\Users\\LENOVO LEGION\\Desktop\\test-webbot\\geckodriver.exe")
browser.get("https://instagram.com")

username = ""
password = ""
count = 10
tag = "#webdesign"
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
    itterateBot(count,tag)

def waitFor(start,end,msg) :
    randomWaitTime = float(decimal.Decimal(random.randrange(start, end))/100)
    logger("Waiting for",str(randomWaitTime) + "s",msg)
    time.sleep(randomWaitTime)

def itterateBot(count,tag) :
    search(tag)
    post = getPost(count)
    for i in range(0,count) :
        postPage = browser.get(post[i])
        waitFor(300,600,"Like post")
        pressLike()
        

def getPost(count) :    
    post = []-
    while(True) : 
        if(len(browser.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div/div/a')) < count) : 
            browser.execute_script("window.scrollBy(0, 1000)") 
        else : 
            break
    for posts in browser.find_elements_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div/div/a') : 
        print(posts.get_attribute("href"))
        post.append(posts.get_attribute("href"))
    return post
    
def pressLike() : 
    likeBtn = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
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

def logger(*args) : 
    print(" ".join(args),flush = True)

bot()