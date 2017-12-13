#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait


def getElement(driver,locateType,locateExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x: x.find_element(by=locateType, value=locateExpression))
        return element
    except Exception,e:
        raise e


def getElements(driver,locateType,locateExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x: x.find_elements(by=locateType, value=locateExpression))
        return elements
    except Exception,e:
        raise e


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver,'id','kw')
    print searchBox.tag_name
    aList = getElements(driver,'tag name','a')
    print len(aList)