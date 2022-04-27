import base64
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.login import testURL
import ddddocr


class BasePage():
    """
    基础Page层,封装一些常用方法
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = testURL

    # 打开页面
    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # 元素定位
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time, 1).until(EC.visibility_of_element_located(locator))

    # 退出网页
    def close(self):
        self.driver.quit()

    # 获取指定路径信息
    def get_info(self, locator, src):
        info = self.find_element(locator).get_attribute(src)
        return info

    @staticmethod
    # 处理图片base64
    def get_img64(img):
        num = img.find(',')
        img_base64 = img[num+1:]
        return img_base64

    @staticmethod
    # 转换图片并保存
    def img_result(img_base64):
        img=base64.b64decode(img_base64)
        with open('verification.jpeg', 'wb') as wf:
            wf.write(img)

    # 识别图像文字
    @staticmethod
    def verification_ocr():
        ocr = ddddocr.DdddOcr()
        with open('verification.jpeg', 'rb') as rf:
            img = rf.read()
        res = ocr.classification(img)
        return res

    # 获得div文字信息
    def verification_text(self, locator):
        verification_text = self.find_element(locator).text
        return verification_text
