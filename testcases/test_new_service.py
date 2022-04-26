import pytest
from test_server.page.data_page import DataPage


class TestNewService:
    """
    编写测试用例
    """

    # def setup_class(self):
    #     self.serviceinfo = ServiceInfo()

    def setup(self):
        self.data_page = DataPage()

    @pytest.mark.parametrize("servername, keyword", [("test_海南", "小浪底")])
    def test_new_service(self, servername, keyword):

        # 链式调用
                                    # 1.跳转到服务页面 2.跳转到新建服务页面 3.新建服务                        4.获取服务列表
        service_list = self.data_page.goto_service().goto_new_server().new_server(servername, keyword).get_service_list()
        assert servername in service_list

    # @pytest.mark.parametrize("servername", ["A"])
    # def test_new_service(self, servername):
    #     self.data_page.goto_service().goto_new_server().new_server_fail(servername)
        # assert servername in service_list