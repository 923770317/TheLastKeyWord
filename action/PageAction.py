#coding=utf-8
from selenium import webdriver
from config.VarConfig import *
from util.ObjectMap import *
from util.DirAndTime import *
from util.WaitUtil import *
from selenium.webdriver.chrome.options import Options
import time

driver = None

waitUtil = None

def open_browser(browserName,*arg):
    global  driver,waitUtil
    try:
        if browserName.lower() =='ie':
            driver = webdriver.Ie()
        elif browserName.lower() == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome(chrome_options=None)
        waitUtil = WaitUtil(driver)
    except Exception,e:
        raise e