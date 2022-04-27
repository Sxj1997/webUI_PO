from time import sleep
import pytest
from page.LoginPage import LoginPage
from test_data.login import namePassword, noVerification


class TestLogin():

    @pytest.mark.parametrize("name,password",namePassword)
    def test_login(self,name,password):
        """
        账号密码正确或错误+验证码
        """
        page = LoginPage()
        page.open()
        page.turn_password()
        page.password_clear()
        page.name_clear()
        page.name_input(name)
        page.password_input(password)
        for i in range(0,3):
            v64=page.get_verification64()
            page.verification_input(v64)
            sleep(1)
            pageWeb.login()
            sleep(3)
            pageInfo=page.if_login()
            sleep(3)
            if pageInfo:
                break
            else:
                page.verification_clear()
                continue
        pageInfo=page.if_login()
        assert pageInfo

    @pytest.mark.parametrize("name,password",noVerification)
    def test_login2(self,name,password):
        """
        无验证码登录
        """
        #page = LoginPage()
        #page.open()
        #page.turn_password()
        page.password_clear()
        page.name_clear()
        page.name_input(name)
        page.password_input(password)
        sleep(1)
        page.login()
        sleep(1)
        pageInfo=page.if_verification()
        assert pageInfo