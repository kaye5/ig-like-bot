from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
import decimal
import os
import json
from datetime import datetime
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def logger(*args) : 
    print(" ".join(args),flush = True)

def getConfig() : 
    config = os.path.join(THIS_FOLDER, 'config.json')
    f = open(config)
    return json.load(f)

def waitFor(start,end,msg) :
    randomWaitTime = float(decimal.Decimal(random.randrange(start, end))/100)
    logger(str(datetime.now()),"Waiting for",str(randomWaitTime) + "s",msg)
    time.sleep(randomWaitTime)