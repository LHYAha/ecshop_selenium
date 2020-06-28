from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ecshop.Common.startBrowser import startBrowser
from ecshop.Common.getScreenShot import getScreenShot
from ecshop.Common.logGenerate import GenLog
import time
class BasePage(object):
    def __init__(self,configSection):
        logger = GenLog(logger='基准页面').loggen()
        self.driver = startBrowser(configSection)

    def find_element(self,*loc):
        self.logger.info('执行重写的find_element方法')
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.logger.info('找不到目标元素')
    def send_keys(self,loc,value):
        self.logger.info('执行重写的send_keys方法')
        try:
            # loc = getattr(self,'_%s' %loc)
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.logger.info('无法输入keyword')
    def quit_test(self):
        time.sleep(3)
        self.driver.quit()

    def screenShot(self):
        self.logger.info('执行截图方法')
        getScreenShot(self.driver)
        self.logger.info('截图成功')

# keyword = (By.ID,"keyword")
# submit = (By.NAME,"imageField")
# obj=BasePage("http:10.18.20.17:8081/ecshop/index.php")
# obj.send_keys(keyword,"智能相机")
# obj.find_element(submit).click()