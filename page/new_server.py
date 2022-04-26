import time
from selenium.webdriver.common.by import By
from test_server.page.base_page import BasePage


class NewServerPage(BasePage):
    # 设定为元组
    servicename = (By.CSS_SELECTOR, ".ivu-form-item-content > .ivu-input-wrapper > .ivu-input:nth-child(3)") # 输入服务名
    showpublic = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div/div[4]/div/div/div/div/span') # 点击是否公开
    public = (By.XPATH, '//*[@id="service-layer-tab"]/form/div[1]/div[2]/div[1]/div[4]/div/div/div[2]/ul[2]/li[2]') # 点击选择公开
    addlayer = (By.CSS_SELECTOR, ".ivu-btn-default:nth-child(1) > span") # 点击添加图层
    searchbox = (By.CSS_SELECTOR, ".ivu-col-span-6 .ivu-form-item-content > .ivu-input-wrapper > .ivu-input") # 关键字输入框
    search = (By.CSS_SELECTOR, ".ivu-col > .ivu-btn:nth-child(2) > span") # 点击检索按钮
    addxiaolangdi = (By.XPATH,
                                 '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/div[3]/div[2]'
                                 '/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[4]/div/div/button/span') # 点击添加小浪底
    resetbutton = (By.CSS_SELECTOR, ".ivu-col > .ivu-btn:nth-child(1)") # 点击重置按钮
    addjianbian2 = (By.XPATH,
                                 '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/div[3]/div[2]'
                                 '/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[4]/div/div/button/span') # 添加渐变-2
    nextpage = (By.CSS_SELECTOR, "div:nth-child(1) > .ivu-page > .ivu-page-next .ivu-icon") # 点击下一页
    addhenan3 = (By.XPATH,
                                 '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/div[3]/div[2]'
                                 '/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/div/button/span') # 点击添加河南省3
    closeaddlayer = (By.CSS_SELECTOR, ".view-modal-visible .ivu-modal-close > .ivu-icon") # 关闭添加图层
    information = (By.CSS_SELECTOR, ".ivu-form .ivu-tabs-tab:nth-child(3)") # 点击拓展信息
    watermark = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div[2]/div/div/div/div/div/span') # 点击水印
    dd = (By.CSS_SELECTOR, ".ivu-select-visible .ivu-select-item:nth-child(4)") # 选择dd
    satellite = (By.XPATH, '//*[@id="service-layer-tab"]/form/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div/span') # 点击卫星
    t = (By.CSS_SELECTOR, ".ivu-select-visible .ivu-select-item:nth-child(2)") # 选择123t
    load = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div[2]/div[3]/div/div/div/div/span') # 点击负载
    ffff = (By.CSS_SELECTOR, ".ivu-select-visible .ivu-select-item") # 选择ffff
    type = (By.XPATH, '//*[@id="service-layer-tab"]/form/div/div[2]/div[2]/div[4]/div/div/div/div/span') # 点击产品类别
    d = (By.CSS_SELECTOR, ".ivu-select-visible .ivu-select-item:nth-child(5)") # 12DDD
    save = (By.CSS_SELECTOR, ".btn-cls > .ivu-btn:nth-child(2) > span") # 点击保存服务


    def new_server(self, servername, keyword):

        # 输入服务名
        # self.driver.find_element(*self.servicename).send_keys(servername)
        self.find(self.servicename).send_keys(servername)
        time.sleep(1)
        # 点击是否公开
        self.driver.find_element(*self.showpublic).click()
        time.sleep(1)
        # 点击选择公开
        self.driver.find_element(*self.public).click()
        time.sleep(1)
        # 点击添加图层
        self.driver.find_element(*self.addlayer).click()
        time.sleep(1)
        # 输入小浪底
        self.driver.find_element(*self.searchbox).send_keys(keyword)
        time.sleep(1)
        # 点击检索按钮
        self.driver.find_element(*self.search).click()
        time.sleep(1)
        # 点击添加小浪底
        self.driver.find_element(*self.addxiaolangdi).click()
        time.sleep(1)
        # 点击重置
        self.driver.find_element(*self.resetbutton).click()
        time.sleep(1)
        # 添加渐变-2
        self.driver.find_element(*self.addjianbian2).click()
        time.sleep(1)
        # 点击下一页
        self.driver.find_element(*self.nextpage).click()
        time.sleep(1)
        # 点击添加河南省3
        self.driver.find_element(*self.addhenan3).click()
        time.sleep(1)
        # 关闭添加图层
        self.driver.find_element(*self.closeaddlayer).click()
        time.sleep(1)
        # 点击拓展信息
        self.driver.find_element(*self.information).click()
        time.sleep(1)
        # 点击水印
        self.driver.find_element(*self.watermark).click()
        time.sleep(1)
        # 选择dd
        self.driver.find_element(*self.dd).click()
        time.sleep(1)
        # 点击卫星
        self.driver.find_element(*self.satellite).click()
        time.sleep(1)
        # 选择123t
        self.driver.find_element(*self.t).click()
        time.sleep(1)
        # 点击负载
        self.driver.find_element(*self.load).click()
        time.sleep(1)
        # 选择ffff
        self.driver.find_element(*self.ffff).click()
        time.sleep(1)
        # 点击产品类别
        self.driver.find_element(*self.type).click()
        time.sleep(1)
        # 12DDD
        self.driver.find_element(*self.d).click()
        time.sleep(1)
        # 点击保存服务
        self.driver.find_element(*self.save).click()
        time.sleep(3)

        from test_server.page.service_page import ServicePage
        return ServicePage(self.driver)