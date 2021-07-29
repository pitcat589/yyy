# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.login_page import LoginPage
from pages.handle_page import HandlePage
from common.logger import Log
from common.connect_sql import ConnectSQL
from common.My_swipe import*


class Test_Vcode_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '8eedcec30404',  # 根据当前测试设备名称修改
            'appPackage': 'com.amethystum.cloud',
            'appActivity': 'com.amethystum.main.view.LauncherActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'automationName': 'UiAutomator2',
            # 'noReset': True
        }
        # 配置
        cls.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(2)
        # 实例化
        # 每子页面的page类都继承了basepage父类，而basepage父类需要传入driver来初始化，所以子类也需传driver来实例化
        cls.login_page = LoginPage(cls.driver)
        cls.handle_page = HandlePage(cls.driver)
        cls.get_sql = ConnectSQL()
        cls.log = Log()

    # @unittest.skip()
    # 未绑定用户验证码登录
    def test_unbind_user_Vcode_login(self):
        self.log.info('开始测试-首次安装后进行验证码登录')
        self.login_page.agree_ins()
        self.login_page.input_username("17683744401")
        self.login_page.tap_code()
        time.sleep(3)
        new_code = self.get_sql.get_code(mobile="17683744401")
        self.login_page.to_input_code(code=new_code)
        self.login_page.tap_login()
        self.login_page.agree_permission()
        time.sleep(1)
        t_info = self.login_page.test_judge().text
        # 断言查看－登录成功且未绑定设备
        self.log.info("未绑定页面提示:" + t_info + ", " + str(self.assertEqual('您还未绑定设备', str(t_info))))
        self.login_page.tran_mine_page()
        self.log.info('未绑定用户验证码登录测试结束\n')

    # 未绑定用户手势密码登录
    def test_unbind_user_gesture_login(self):
        self.log.info('开始测试-未绑定用户手势密码登录')

        self.login_page.security_management_ins()  # 点击安全管理按钮
        self.login_page.first_gesture_unlock()  # 第一次点击手势解锁
        self.login_page.first_password_verification(passwd="123456yyy")  # 第一次点击手势解锁账户密码验证
        self.login_page.slide_scroll()
        self.login_page.tap_next()
        self.login_page.first_draw_gesture_password()

        time.sleep(3)
        self.handle_page.trans_list_back()
        # swipe_right(self.driver)
        self.login_page.tap_logout()
        self.login_page.sure_logout()
        time.sleep(3)
        self.login_page.login_draw_gesture_password()
        time.sleep(1)
        self.login_page.tran_mine_page()
        self.login_page.tap_logout()
        self.login_page.sure_logout()
        self.log.info('未绑定用户手势密码登录测试结束\n')

    # 手势密码登录-切换登录方式
    def test_user_gesture_switchway(self):
        self.log.info('开始测试-手势密码登录-切换登录方式')
        self.login_page.user_gesture_switchway()
        # 断言查看是否切换到输入验证码登录页面按钮是否高亮
        self.log.info('验证码登录页面按钮是否高亮')
        self.login_page.get_login_code_is()

        self.login_page.tran_login_way()
        self.login_page.input_passwd("123456yyy")
        self.login_page.tap_login()
        self.login_page.tran_mine_page()
        self.login_page.tap_logout()
        self.login_page.sure_logout()

        self.log.info('结束测试-手势密码登录-切换登录方式\n')

    # 手势密码登录-切换帐号
    def test_user_gesture_switchcount(self):
        self.log.info('开始测试-手势密码登录-切换帐号')
        self.login_page.user_gesture_switchcount()
        # 断言查看是否切换到输入验证码登录页面按钮是否高亮
        self.log.info('验证码登录页面按钮是否高亮')
        self.login_page.get_login_code_is()

        self.login_page.tran_login_way()
        self.login_page.input_passwd("123456yyy")
        self.login_page.tap_login()
        self.login_page.tran_mine_page()
        self.login_page.tap_logout()
        self.login_page.sure_logout()

        self.log.info('结束测试-手势密码登录-切换帐号\n')

    # 手势密码登录-忘记手势密码
    def test_user_gesture_switchforget(self):
        self.log.info('开始测试-手势密码登录-忘记手势密码')
        self.login_page.user_gesture_switchforget()
        # 断言查看是否切换到输入验证码登录页面按钮是否高亮
        self.log.info('验证码登录页面按钮是否高亮')
        self.login_page.get_login_code_is()
        self.login_page.tran_login_way()
        self.login_page.input_passwd("123456yyy")
        self.login_page.tap_login()
        self.login_page.tran_mine_page()
        self.login_page.tap_logout()
        self.login_page.sure_logout()

        self.log.info('结束测试-手势密码登录-忘记手势密码\n')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.get_sql.close_db()


if __name__ == '__main__':
    unittest.main()
