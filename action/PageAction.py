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
            driver = webdriver.Chrome()
        waitUtil = WaitUtil(driver)
    except Exception,e:
        raise e


def visit_url(url,*arg):
    global driver
    try:
        driver.get(url)
    except Exception,e:
        raise e

def close_browser(*arg):
    global driver
    try:
        driver.quit()
    except Exception,e:
        raise e

def sleep(sleepSeconds,*arg):
    try:
        time.sleep(sleepSeconds)
    except Exception ,e:
        raise e


def clear(locationType,locationExpression,*arg):
    global driver
    try:
        getElement(driver,locationType,locationExpression).clear()
    except Exception,e:
        raise e

def input_string(locationType,locationExpression,inputContent):
    global driver
    try:
        getElement(driver, locationType, locationExpression).send_keys(inputContent)
    except Exception,e:
        raise e

def click(locationType,locationExpression,arg):
    global driver
    try:
        getElement(driver, locationType, locationExpression).click()
    except Exception,e:
        raise e

def assert_string_in_pagesource(assertString,*arg):
    global driver
    try:
        assert assertString in driver.page_source,u'%s not found in page source' %assertString
    except AssertionError,e:
        raise AssertionError(e)
    except Exception,e:
        raise e

def assert_title(titleStr,*arg):
    global driver
    try:
        assert titleStr in driver.title,u'%s not found in title' %titleStr
    except AssertionError,e:
        raise AssertionError(e)
    except Exception,e:
        raise e

def getTitle(*arg):
    global driver
    try:
        return driver.title
    except Exception,e:
        raise e

def getPageSource(*arg):
    global driver
    try:
        return driver.page_source
    except Exception,e:
        raise e

def switch_to_frame(locationType,locationExpression,*arg):
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locationType,locationExpression))
    except Exception,e:
        raise e

#切除frame
def switch_to_defalut_content(*arg):
    global driver
    try:
        driver.switch_to.default_content()
    except Exception,e:
        raise e

#模拟CTRL+V
def paste_string(pasetSring,*arg):
    pass

def maximize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception,e:
        raise e

def capture_screen(*arg):
    global driver
    currTIme = getCurrnetTime()
    picNameAndPath = str(createCurrentDateDir())+ "\\" + str(currTIme) + '.png'
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace("\\",r'\\'))
    except Exception,e:
        raise e
    else:
        return picNameAndPath

def waitPressenceOfElementLocated(locationType,locationExpression,*arg):
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType,locationExpression)
    except Exception,e:
        raise e


def waitFrameToBeAvailableAndSwitchToIt(locationType,locationExpression,*arg):
    global waitUtil
    try:
        waitUtil.frame_available_and_switch_to_it(locationType, locationExpression)
    except Exception, e:
        raise e

def waitVisiblityOfElementLocated(locationType,locationExpression,*arg):
    global waitUtil
    try:
        waitUtil.visibility_element_located(locationType, locationExpression)
    except Exception, e:
        raise e
