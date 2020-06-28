from ecshop.Pages.basepage import BasePage
from selenium.webdriver.common.by import By
from ecshop.Common.logGenerate import GenLog
from ecshop.Common.getScreenShot import getScreenShot
class SearchPage(BasePage):
    searchtext = (By.ID, "keyword")
    searchbutton = (By.NAME, "imageField")
    logger = GenLog(logger='搜索页面').loggen()

    def input_search(self,searchstr):
        self.logger.info('执行input_search方法')
        self.find_element(*self.searchtext).send_keys(searchstr)

    def submit_search(self):
        self.logger.info('执行submit_search方法')
        self.find_element(*self.searchbutton).click()

    def search_result(self,searchmes):
        self.click = (By.LINK_TEXT,searchmes)
        self.productName = (By.CLASS_NAME, "goods_style_name")
        self.find_element(*self.click).click()
        self.actualValue = self.find_element(*self.productName).text
        if self.actualValue == searchmes:
            self.logger.info('查找成功')
            self.logger.info('截图保留测试结果')
            self.screenShot()
        else:
            self.logger.info('查找失败')
        self.quit_test()

# AA=SearchPage("ecshop")
# AA.input_search("智能相机")
# AA.submit_search()
# AA.search_result("智能相机")