import time

from selenium.webdriver.common.by import By

from test_server.page.base_page import BasePage
from test_server.page.service_page import ServicePage


class DataPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """
    def goto_service(self):
        """
        跳转到服务页面
        :return:
        """
        # 点击服务
        self.driver.find_element(By.CSS_SELECTOR, ".ivu-menu-item:nth-child(3) > span").click()
        time.sleep(1)

        return ServicePage(self.driver)

