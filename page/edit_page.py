import time
from selenium.webdriver.common.by import By
from test_server.page.base_page import BasePage
from test_server.page.new_server import NewServerPage


class EditServerPage(BasePage):
    # 设定为元组

    clear = (By.CSS_SELECTOR, ".ivu-form-item-content > .ivu-input-wrapper > .ivu-input:nth-child(3)") # 清除服务名
    servicename = (By.CSS_SELECTOR, ".ivu-form-item-content > .ivu-input-wrapper > .ivu-input:nth-child(3)") # 输入新服务名
    showpublic = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div/div[4]/div/div/div/div/span')  # 点击是否公开
    nopublic = (By.XPATH, '//*[@id="service-layer-tab"]/form/div[1]/div[2]/div[1]/div[4]/div/div/div[2]/ul[2]/li[1]')  # 点击选择不公开
    down = (By.XPATH, '//*[@id="service-layer-list"]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div/span[3]')# 下移
    up = (By.XPATH, '//*[@id="service-layer-list"]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div/span[2]') # 上移
    information = (By.CSS_SELECTOR, ".ivu-form .ivu-tabs-tab:nth-child(3)")  # 点击拓展信息
    watermark = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div[2]/div/div/div/div/div/span')  # 点击水印
    jj = (By.CSS_SELECTOR, "#service-layer-tab > form > div.ivu-tabs > div.ivu-tabs-content.ivu-tabs-content-animated > "
                                 "div:nth-child(2) > div:nth-child(1) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(3)")  # 选择jj
    satellite = (By.XPATH, '//*[@id="service-layer-tab"]/form/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div/span')  # 点击卫星
    gf1 = (By.CSS_SELECTOR, '#service-layer-tab > form > div.ivu-tabs > div.ivu-tabs-content.ivu-tabs-content-animated > '
                            'div:nth-child(2) > div:nth-child(2) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(4)') # 选择gf1
    load = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div[2]/div[3]/div/div/div/div/span')  # 点击负载
    fpws = (By.CSS_SELECTOR, "#service-layer-tab > form > div.ivu-tabs > div.ivu-tabs-content.ivu-tabs-content-animated > "
                             "div:nth-child(2) > div:nth-child(3) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li")  # 选择pws
    type = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div[2]/div[4]/div/div/div/div/span')  # 点击产品类别
    s = (By.CSS_SELECTOR, "#service-layer-tab > form > div.ivu-tabs > div.ivu-tabs-content.ivu-tabs-content-animated > div:nth-child(2) > "
                          "div:nth-child(4) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(2)")  # 12s
    save = (By.CSS_SELECTOR, ".btn-cls > .ivu-btn:nth-child(2) > span")  # 点击保存服务


    def edit_server(self, servername):

        # 删除服务名
        time.sleep(1)
        self.find(self.clear).clear()
        # 输入新服务名
        time.sleep(1)
        self.find(self.servicename).send_keys(servername)
        # 点击是否公开
        time.sleep(1)
        self.find(self.showpublic).click()
        time.sleep(1)
        # 选择不公开
        self.find(self.nopublic).click()
        # 下移
        time.sleep(1)
        self.find(self.down).click()
        # 上移
        time.sleep(1)
        self.find(self.up).click()
        # 点击拓展信息
        time.sleep(1)
        self.find(self.information).click()
        # 点击水印
        time.sleep(1)
        self.find(self.watermark).click()
        time.sleep(1)
        # 选择jj
        self.find(self.jj).click()
        time.sleep(1)
        # 点击卫星
        self.find(self.satellite).click()
        time.sleep(1)
        # 选择gf1
        self.find(self.gf1).click()
        time.sleep(1)
        # 点击负载
        self.find(self.load).click()
        time.sleep(1)
        # 选择pws
        self.find(self.fpws).click()
        time.sleep(1)
        # 点击产品类别
        self.find(self.type).click()
        time.sleep(1)
        # 选择12s
        self.find(self.s).click()
        time.sleep(1)
        # 点击保存服务
        self.find(self.save).click()
        time.sleep(3)

        from test_server.page.service_page import ServicePage
        return ServicePage(self.driver)