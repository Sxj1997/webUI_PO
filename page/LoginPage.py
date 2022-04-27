from selenium.webdriver.common.by import By
from base.base import BasePage

class LoginPage(BasePage):
    """
    登录页
    """
    # 定位器，通过元素定位
    login_button=(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[6]/div/button[1]')
    name=(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[2]/div/div/input')
    password=(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[3]/div/div/input')
    verification=(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div[1]/div/input')
    turn_button=(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[3]/div/button[2]')
    verification64=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div[2]/img')
    verificationText=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/form/div[4]/div/div[3]')
    pageInfo=(By.XPATH,'//*[@id="app"]/div')

    # 点击登入
    def login(self):
        self.find_element(self.login_button).click()

    # 清空用户名输入
    def name_clear(self):
        self.find_element(self.name).clear()

    # 输入用户名
    def name_input(self,name):
        self.find_element(self.name).send_keys(name)

    # 输入密码
    def password_input(self,password):
        self.find_element(self.password).send_keys(password)

    # 清空密码输入
    def password_clear(self):
        self.find_element(self.password).clear()

    # 切换到密码登录
    def turn_password(self):
        self.find_element(self.turn_button).click()

    # 识别验证码
    def get_verification64(self):
        img64=self.get_info(self.verification64,'src')
        img=self.get_img64(img64)
        self.img_result(img)
        verification=self.verification_ocr()
        return verification

    # 填写验证码
    def verification_input(self,verification):
        self.find_element(self.verification).send_keys(verification)

    # 判断是否登录成功
    def if_login(self):
        info=self.get_info(self.pageInfo,'class')
        if info=='app-wrapper openSidebar':
            return True
        else:
            return False

    # 清空验证码
    def verification_clear(self):
        self.find_element(self.verification).clear()

    # 判断是是否提示验证码未输入
    def if_verification(self):
        info=self.verification_text(self.verificationText)
        if info=='验证码不能为空':
            return True
        else:
            return False