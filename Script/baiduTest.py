from ecshop.Common.startBrowser import startBrowser
import time,random
from ecshop.Common.readCase import readCase
from ecshop.Common.getScreenShot import getScreenShot
from ecshop.Common.logGenerate import GenLog

class baidu():
    def __init__(self):
        self.logger = GenLog(logger='对百度进行操作').loggen()
        self.logger.info("执行__init__方法" )
        self.driver = startBrowser()
    def search(self,message):
        self.logger.info("执行search方法")
        self.driver.find_element_by_id('kw').send_keys(message)
        self.driver.find_element_by_id('su').click()
        getScreenShot(self.driver,"d:\\")
        self.logger.info("截图完成")
        time.sleep(2)
        self.driver.quit()
        self.logger.info("退出浏览器")
    def clicLinTest(self,linkValue):
        self.logger.info("执行clicLinTest方法")
        self.length=linkValue.__len__()
        self.i=random.randint(1,self.length-1)
        self.driver.find_element_by_link_text(linkValue[self.i]).click()
        getScreenShot(self.driver, "d:\\")
        self.logger.info("截图完成")
        time.sleep(2)
        self.driver.quit()
        self.logger.info("退出浏览器")


# testDate=readCase("C:\\Users\\Administrator\\Desktop\\linkTest.xlsx","Sheet1")
# baidu().clicLinTest(testDate)

# driver = startBrowser()
# driver.find_element_by_id('kw').send_keys("软件测试")
# driver.find_element_by_id('su').click()
# time.sleep(2)
# driver.quit()