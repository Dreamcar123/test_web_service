import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_server.page.base_page import BasePage
from test_server.page.edit_page import EditServerPage
from test_server.page.new_server import NewServerPage


class ServicePage(BasePage):

    newservice = (By.CSS_SELECTOR, ".ivu-btn:nth-child(2) > span:nth-child(2)")  # 点击新建服务
    firstservice = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div'
                              '/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div[1]/div[1]/img')  # 移动鼠标悬停第一个服务
    edit = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/div[1]/'
                      'div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div[1]/div[2]/a[1]/div/div/span')  # 编辑
    delete = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/div[1]'
                        '/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div[1]/div[2]/a[3]/div/div/span')  # 删除
    sure = (By.CSS_SELECTOR, 'body > div:nth-child(19) > div.ivu-modal-wrap.deleteModal.vertical-center-modal '
                             '> div > div > div.ivu-modal-footer > button.ivu-btn.ivu-btn-primary > span')  # 弹出提示框点击确定

    def goto_new_server(self):
        """
        跳转到新建服务页面
        :return:
        """
        # 点击新建服务
        self.find(self.newservice).click()
        time.sleep(1)
        return NewServerPage(self.driver)

    def goto_edit_server(self):
        """
        鼠标悬停编辑按钮
        点击编辑
        跳转到编辑服务页面
        :return:
        """
        # 移动鼠标悬停第一个服务
        element = self.find(self.firstservice)  # 定位触发隐藏元素显示的位置
        time.sleep(1)
        ActionChains(self.driver).move_to_element(element).perform()  # 鼠标移动到触发点
        # 鼠标移动到编辑按钮
        time.sleep(1)
        element_edit = self.find(self.edit)  # 定位触发隐藏元素显示的位置
        time.sleep(1)
        ActionChains(self.driver).move_to_element(element_edit).perform()  # 鼠标移动到触发点
        # 点击编辑按钮
        time.sleep(1)
        self.find(self.edit).click()

        return EditServerPage(self.driver)


    def delete_server(self):
        element = self.find(self.firstservice)  # 定位触发隐藏元素显示的位置
        time.sleep(1)
        ActionChains(self.driver).move_to_element(element).perform()  # 鼠标移动到触发点
        # 鼠标移动到删除按钮
        time.sleep(1)
        element_delete = self.find(self.delete)  # 定位触发隐藏元素显示的位置
        time.sleep(1)
        ActionChains(self.driver).move_to_element(element_delete).perform()  # 鼠标移动到触发点
        # 点击删除按钮
        time.sleep(1)
        self.find(self.delete).click()
        # 弹出提示框点击确定
        time.sleep(3)
        self.find(self.sure).click()
        time.sleep(3)
        return ServicePage(self.driver)


    def get_service_list(self):
        """
        服务页面获取服务列表
        :return:
        """
        # 获取元素列表
        ele_list = self.driver.find_elements(By.CSS_SELECTOR,
                                             '[style="height: 28px; display: flex; justify-content: space-between; '
                                             'margin-bottom: 4px; overflow: hidden;"]')
        print(ele_list)
        service_list = []
        # 遍历元素列表，通过元素的text属性提取文本数据信息
        for ele in ele_list:
            service_list.append(ele.text)
        print(service_list)

        return service_list