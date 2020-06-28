from  selenium import webdriver

from selenium.webdriver.common.by import By
from ecshop.Common.logGenerate import GenLog
from ecshop.Common.getScreenShot import getScreenShot
from ecshop.Pages.basepage import BasePage
import time

# driver=webdriver.Firefox()
# driver.get("http:10.18.20.17:8081/ecshop/index.php")
# driver.find_element_by_link_text("免费注册").click()
# driver.find_element_by_id("username").send_keys("lihaiyan")
# driver.find_element_by_id("email").send_keys("22@qq.com")
# driver.find_element_by_id("password1").send_keys("lihaiyan")
# driver.find_element_by_id("conform_password").send_keys("lihaiyan")
# flag=driver.find_element_by_name("agreement").click()
# if not flag:
#     pass
# driver.find_element_by_name("Submit").click()
# time.sleep(2)
# username=driver.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/font/font').text
# driver.quit()
# if username =='lihaiyan':
#     print("register succeed")
# else:
#     print("register fail")


class RegisterPage(BasePage):
    logger = GenLog(logger='注册页面').loggen()

    loc = (By.LINK_TEXT, "免费注册")
    username = (By.ID, "username")
    email = (By.ID, "email")
    password = (By.ID, "password1")
    confirm_password = (By.ID, "conform_password")
    submit = (By.NAME, "Submit")

    def register(self,username,eamil,password):
        self.logger.info('执行register方法')

        self.find_element(*self.loc).click()
        self.send_keys(self.username,username)
        self.send_keys(self.email, eamil)
        self.send_keys(self.password, password)
        self.send_keys(self.confirm_password, password)
        self.find_element(*self.submit).click()

    def register_result(self,result):
        self.loginname = (By.XPATH,'//*[@id="ECS_MEMBERZONE"]/font/font')
        self.mes=self.find_element(*self.loginname).text

        if self.mes == result:
            self.logger.info('注册成功')
            self.logger.info('截图保留测试结果')
            self.screenShot()
        else:
            self.logger.info('注册失败')

        self.quit_test()

# AA=RegisterPage("ecshop")
# AA.register("189453","139@qq.com","123456")
# AA.register_result("189453")
