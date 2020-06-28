from  selenium import webdriver
import time
from ecshop.Pages.basepage import BasePage
from selenium.webdriver.common.by import By
from ecshop.Common.logGenerate import GenLog
from ecshop.Common.getScreenShot import getScreenShot


class LoginPage(BasePage):
    logger = GenLog(logger='登录页面').loggen()
    loginPage = (By.LINK_TEXT,"请登录")
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginbuttom = (By.NAME, "submit")
    user = (By.XPATH, '//*[@id="ECS_MEMBERZONE"]/font/font')

    def login_page(self):
        self.find_element(*self.loginPage).click()

    def input_login(self,username,password):
        self.logger.info('执行input_login方法')
        self.send_keys(self.username,username)
        self.send_keys(self.password, password)

    def login_submit(self):
        self.logger.info('执行login_submit方法')
        self.find_element(*self.loginbuttom).click()

    def login_result(self,username):
        self.logger.info('执行login_result方法')
        self.result = self.find_element(*self.user).text

        if self.result == username:
            self.logger.info('登录成功')
            self.logger.info('截图保留测试结果')
            self.screenShot()
        else:
            self.logger.info('登录失败')

        self.quit_test()

# AA=LoginPage("ecshop")
# AA.login_page()
# AA.input_login("123456","123456")
# AA.login_submit()
# AA.login_result("123456")
