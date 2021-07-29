# coding:utf-8
from appium import webdriver
import time
import unittest
from pages.login_page import LoginPage
from common.logger import Log
from common.connect_sql import ConnectSQL


class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '8eedcec30404',#根据当前测试设备名称修改
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
        cls.get_sql = ConnectSQL()
        cls.log = Log()

    # @unittest.skip()
    # 未绑定用户登录
    def test_unbind_user_login(self):
        self.log.info('开始测试-首次安装后进行登录')
        self.login_page.agree_ins()
        self.login_page.input_username("13899999100")
        self.login_page.tran_login_way()
        self.login_page.input_passwd("q12345678")
        self.login_page.tap_login()
        self.login_page.agree_permission()
        time.sleep(1)
        t_info = self.login_page.test_judge().text
        # 断言查看－登录成功且未绑定设备
        self.log.info("未绑定页面提示:"+t_info+", "+str(self.assertEqual('您还未绑定设备', str(t_info))))
        self.login_page.tran_mine_page()
        self.login_page.tap_logout()
        self.login_page.sure_logout()
        self.log.info('未绑定用户登录测试结束\n')

    # 用户注册-登录
    def test_user_to_register(self):
        self.log.info('开始测试-首次安装后进行注册')
        self.login_page.agree_ins()
        self.login_page.switch_register()
        # time.sleep(1)
        # t_info = self.register.test_register_judge().text
        # self.assertEqual('是否是注册页面', str(t_info))
        # self.log.info("注册页面："+t_info)
        # print(t_info)
        self.login_page.input_username("18999991815")
        self.login_page.tap_code()
        new_code = self.get_sql.get_code(mobile="18999991815")
        self.login_page.input_code(code=new_code)
        self.login_page.slide_scroll()
        time.sleep(1)
        self.login_page.tap_next()
        time.sleep(3)
        self.login_page.set_passwd_first(passwd="q12345678")
        self.login_page.set_passwd_second(passwd="q12345678")
        self.login_page.tap_complete_set_passwd()
        self.login_page.tap_immediate_login()
        self.log.info('注册测试结束\n')
        time.sleep(1)
        t_info = self.login_page.test_judge().text
        # 断言查看－登录成功且未绑定设备
        self.assertEqual('您还未绑定设备', str(t_info))
        self.log.info("未绑定页面提示："+t_info)
        self.login_page.tran_mine_page()
        self.login_page.tap_logout()
        self.login_page.sure_logout()
        self.log.info('退出登录，测试结束\n')

    # 异常账号登录
    def test_wrong_user_login(self):
        toast_message = "必须以1开头"
        self.log.info('开始测试-账号{}进行登录'.format("01234567890"))
        self.login_page.input_username("01234567890")
        time.sleep(1)
        self.login_page.tran_login_way()
        time.sleep(1)
        self.login_page.input_passwd("q12345678889")
        self.login_page.tap_login()
        self.log.info("元素检测:"+self.login_page.find_toast(message=toast_message))
        self.log.info('测试toast登录结束\n')

    # 异常密码登录
    def test_wrong_passwd_login(self):
        toast_message = "oops, 登录名或密码好像错了哟~~~"
        self.log.info('开始测试-账号{}进行登录'.format("18999991801"))
        self.login_page.input_username("18999991801")
        time.sleep(1)
        time.sleep(1)
        self.login_page.input_passwd("q12345678889")
        self.login_page.tap_login()
        self.log.info("元素检测:"+self.login_page.find_toast(message=toast_message))
        self.log.info('测试toast登录结束\n')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.get_sql.close_db()


if __name__=='__main__':
    unittest.main()


