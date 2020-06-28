#coding=utf-8
from selenium import webdriver
from ecshop.Common.readConfig import readConfig
from ecshop.Common.logGenerate import GenLog
import time

def startBrowser(configSection):
    logger = GenLog(logger='浏览器操作').loggen()
    logger.info('读取浏览器配置文件')
    browserType = readConfig('Config',configSection,'browserName')
    browserFlag=True
    logger.info('正在判断浏览器类型')
    if browserType=='FireFox':
        driver=webdriver.Firefox()
    elif browserType=='Ie':
        driver=webdriver.Ie()
    elif browserType=='Chrome':
        driver=webdriver.Chrome()
    else:
        print("浏览器类型错误！")
        browserFlag=False
    if browserFlag :
        logger.info('当前浏览器是：%s' %browserType)
        url=readConfig('Config',configSection,'url')
        logger.info('打开测试地址:%s' %url)
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        return driver

