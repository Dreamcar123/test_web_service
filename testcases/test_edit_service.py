import pytest
from test_server.page.data_page import DataPage


class TestEditService:


    def setup(self):
        self.data_page = DataPage()

    @pytest.mark.parametrize("servername", ["test_上海"])
    def test_edit_service(self, servername):
        service_list = self.data_page.goto_service().goto_edit_server().edit_server(servername).get_service_list()
        assert servername in service_list