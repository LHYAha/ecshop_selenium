from selenium.webdriver.common.by import By
from ecshop.Pages.basepage import BasePage
class LinkPage(BasePage):
    linkstr = (By.LINK_TEXT,'新闻')
    def click_link(self):
        self.find_element(*self.linkstr).click()