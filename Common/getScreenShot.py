from selenium import webdriver
from ecshop.Common.logGenerate import GenLog
import time
import os
from ecshop.Common.startBrowser import startBrowser
#截图
def getScreenShot(driver):
    logger = GenLog(logger='执行截图方法').loggen()
    timeFormat=time.strftime("%Y%m%d%H%m",time.localtime(time.time()))
    screenShotName = os.path.dirname(os.path.abspath('.'))
    driver.get_screenshot_as_file(screenShotName+"\Pictures\\"+timeFormat+'.png')
    logger.info("有执行截图方法")

# timeFormat=time.strftime("%Y%m%d%H%m",time.localtime(time.time()))
# screenShotName = os.path.dirname(os.path.abspath('.'))
# timeFormat=time.strftime("%Y%m%d%H%m",time.localtime(time.time()))
# print(timeFormat)