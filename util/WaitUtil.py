#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil(object):

    def __init__(self,driver):
        self.locationTypeDict = {'xpath':By.XPATH,
                                 'id':By.ID,
                                 'name':By.NAME,
                                 'class_name':By.CLASS_NAME,
                                 'tag_name':By.TAG_NAME,
                                 'link_text':By.LINK_TEXT,
                                 'partial_link_text':By.PARTIAL_LINK_TEXT,
                                'css_selector':By.CSS_SELECTOR}
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    def presenceOfElementLocated(self,locatorMethod,locationExpress,*arg):
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(EC.presence_of_element_located((self.locationTypeDict[locatorMethod.lower()],locationExpress)))
            else:
                raise TypeError(u'未找到定位方式')
        except Exception,e:
            raise e



    def frame_available_and_switch_to_it(self,locationType,locationExpress,*arg):
        try:
            element = self.wait.until(EC.frame_to_be_available_and_switch_to_it(()))
            return element
        except Exception,e:
            raise e

    def visibility_element_located(self,locationType,locationExpress,*arg):
        try:
            element = self.wait.until(EC.visibility_of_any_elements_located((self.locationTypeDict[locationType.lower()],locationExpress)))
        except Exception,e:
            raise e

if __name__ =="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('http://mail.126.com')