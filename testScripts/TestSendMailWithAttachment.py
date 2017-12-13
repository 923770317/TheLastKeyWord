#coding=utf-8
from util.ObjectMap import *
from util.WaitUtil import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def TestSendMailWithAttachment():
    driver = webdriver.Firefox()
    driver.maximize_window()
    print u'启动浏览器成功'
    print u'访问126邮箱登录页...'
    driver.get("http://mail.126.com")
    time.sleep(3)

    assert u'126网易免费邮--你的专业电子邮局' in driver.title
    print u'访问126邮箱登录页成功'

    wait = WaitUtil(driver)
    wait.frame_available_and_switch_to_it('id','x-URS-iframe')
    username = getElement(driver,'name','email')
    username.send_keys('zhangc_brave')
    password = getElement(driver,'name','password')
    password.send_keys('821222zc')
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    assert u'网易邮箱' in driver.title

    element  = wait.visibility_element_located('css','')
    element.click()

    receiver = getElement(driver,'css','')
    receiver.send_keys('923770317@qq.com')

    subject = getElement(driver,'css','')
    subject.send_keys('Nothing to say!!!')


if __name__ =="__main__":
    TestSendMailWithAttachment()