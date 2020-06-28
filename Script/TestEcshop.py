from ecshop.Pages.register import RegisterPage
from ecshop.Pages.searchpage import SearchPage
from ecshop.Pages.login import LoginPage
class ECShop():

    def register(self,username,eamil,password):
        self.registerObj = RegisterPage("ecshop")
        self.registerObj.register(username,eamil,password)
        self.registerObj.register_result(username)
    def login(self,username,password):
        self.loginObj = LoginPage("ecshop")
        self.loginObj.login_page()
        self.loginObj.input_login(username,password)
        self.loginObj.login_submit()
        self.loginObj.login_result(username)
    def search(self,searchmes):
        self.searchObj = SearchPage("ecshop")
        self.searchObj.input_search(searchmes)
        self.searchObj.submit_search()
        self.searchObj.search_result(searchmes)

ecshopObj = ECShop()
# ecshopObj.register("589453","399@qq.com","123456")
ecshopObj.login("589453","123456")
ecshopObj.search("智能相机")
