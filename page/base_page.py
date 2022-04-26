import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver的实例化
    """

    def __init__(self, base_driver=None): # 没有参数传入，会取默认None，如果有参数传入，会取传入的参数
        """
        driver重复实例化，导致页面重启多次
        解决driver重复实例化 导致页面启动多次
        :param base_driver:
        """
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

            # 登录
            self.driver.get("http://192.168.1.145:9080/seis_base/server/login/index.html")
            self.driver.find_element(By.ID, "loginname").click()
            self.driver.find_element(By.ID, "loginname").send_keys("admin")
            self.driver.find_element(By.ID, "loginpws").send_keys("123456")
            self.driver.find_element(By.ID, "logincode").click()
            time.sleep(10)
            # self.driver.find_element(By.ID, "logincode").send_keys("bxmdj")
            self.driver.find_element(By.ID, "loginbtn").click()
            # 隐式等待
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele = None):
        """

        :param by:定位方式 css, xpath, id...
        :param ele:元素定位信息
        :return:
        """
        # 两种传入定位元素方式，提高代码的兼容性
        if ele == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)
