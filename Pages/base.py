from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ecshop.Common.startBrowser import startBrowser
from ecshop.Common.logGenerate import GenLog
import time

class baseOperator(object):
    logger = GenLog(logger='基准页面').loggen()

    def __init__(self):
        self.startBrowser()

    def find_element(self,*loc):
        self.logger.info('执行重写的find_element方法')
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AttributeError:
            self.logger.info('找不到目标元素')

    def send_keys(self,loc,value):
        self.logger.info('执行重写的send_keys方法')
        try:
            # loc=getattr("_%s" %loc)
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.logger.info('无法输入keyword')

    def click(self,loc):
        self.logger.info('执行重写的click方法')
        try:
            self.find_element(*loc).click()
        except AttributeError:
            self.logger.info('点击按钮找不到')

    def quit_test(self):
        self.logger.info('执行重写的quit方法')
        time.sleep(3)
        self.driver.quit()

# obj=baseOperator("baidu")
# keyword = (By.ID,"kw")
# submit = (By.ID,"su")
#
# obj.send_keys(keyword,"软件测试")
# obj.click(submit)
