import pytest
from test_server.page.data_page import DataPage


class TestDeleteService:


    def setup(self):
        self.data_page = DataPage()


    def test_delete_service(self):
        service_list = self.data_page.goto_service().delete_server().get_service_list()
        assert "test_海南" not in service_list