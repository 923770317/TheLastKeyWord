#coding=utf-8

import time,os
from datetime import datetime
from config.VarConfig import *

#获取当前团日期
def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(str(timeTup.tm_year)) + '-' + str(timeTup.tm_mon) + '-' +str(timeTup.tm_mday)
    return currentDate


#获取当前时间
def getCurrnetTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H:%M:%S:%f')
    return nowTime

#创建截图存放的目录
def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir,getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName



if __name__== "__main__":
    print getCurrnetTime()