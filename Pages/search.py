from  selenium import webdriver
import time
from ecshop.Pages.base import baseOperator
from selenium.webdriver.common.by import By
from ecshop.Common.logGenerate import GenLog
from ecshop.Common.getScreenShot import getScreenShot

# driver=webdriver.Firefox()
# driver.get("http:10.18.20.17:8081/ecshop/index.php")
# driver.find_element_by_id("keyword").send_keys("智能相机")
# driver.find_element_by_name("imageField").click()
# driver.find_element_by_link_text("智能相机").click()
# time.sleep(2)
# productName = driver.find_element_by_class_name("goods_style_name").text
# if productName == '智能相机':
#     print("商品已经找到")
# else:
#     print("商品没有找到")
#
# driver.quit()

class Search(baseOperator):

    def __init__(self):
        self.logger = GenLog(logger='搜索页面').loggen()

    def search(self):
        self.logger.info('执行search方法')
        self.keyword = (By.ID,"keyword")
        self.send_keys(self.keyword, "软件测试")

        self.buttom = (By.NAME,"imageField")
        self.click(self.buttom)

        self.result = (By.LINK_TEXT,"智能相机")
        self.click(self.result)

        self.productName = (By.CLASS_NAME,"goods_style_name")
        self.actualValue = self.find_element(self.productName).text

        if self.actualValue == '智能相机':
            self.logger.info('查找成功')
            getScreenShot(baseOperator, "d:\\")
            self.logger.info('已经截图保留测试结果')
        else:
            self.logger.info('查找失败')

        self.quit_test()



# keyword = (By.ID,"keyword")
# # submit = (By.NAME,"imageField")
# # obj.send_keys(keyword,"智能相机")
# # obj.click(submit)
# Search().search()