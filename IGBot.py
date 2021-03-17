from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import waitFor,getConfig,logger
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))    

class IGBot :
    browser = None
    def __init__(self):
        config = getConfig()        
        self.username = config['username']
        self.password = config['password']
        IGBot.browser = webdriver.Firefox(executable_path=os.path.join(THIS_FOLDER, 'geckodriver.exe'))
        IGBot.browser.set_window_position(0, 0)
        IGBot.browser.set_window_size(768, 1024)
        IGBot.browser.get("https://instagram.com")
        self.loginBot()
        self.closeSaveLogin()
        self.closeNotif()

    def loginBot(self): 
        waitFor(100,300,"input username")
        input = IGBot.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        input.send_keys(self.username)
        waitFor(50,200,"input password")
        input = IGBot.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        input.send_keys(self.password)
        btn = IGBot.browser.find_element_by_class_name("sqdOP.y3zKF")
        btn.send_keys(Keys.RETURN)
    def closeSaveLogin(self) : 
        waitFor(500,600,"closing save login")
        try : 
            btn = IGBot.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
            btn.send_keys(Keys.RETURN)
            print("save login closed")
        except : 
            print("skip close")
    def closeNotif(self) : 
        waitFor(500,600,"closing notif")
        try : 
            btn = IGBot.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            btn.send_keys(Keys.RETURN)
            print("notif closed")
        except : 
            print("skip close")
    def getBotBrowser(self):
        return IGBot.browser