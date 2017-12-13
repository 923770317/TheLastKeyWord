#coding=utf-8
from util.ObjectMap import *
from util.WaitUtil import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def TestSendMailWithAttachment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print u'启动浏览器成功'
    print u'访问126邮箱登录页...'
    driver.get("http://mail.126.com")
    time.sleep(3)

    assert u'126网易免费邮--你的专业电子邮局' in driver.title
    print u'访问126邮箱登录页成功'

    wait = WaitUtil(driver)
    wait.frame_available_and_switch_to_it('id','x-URS-iframe')
    username = getElement(driver,'xpath','//*[@id="auto-id-1513160228022"]')
    username.send_keys('haha')

if __name__ =="__main__":
    TestSendMailWithAttachment()