# coding = utf-8
from appium import webdriver
import time
import unittest
from pages.handle_page import HandlePage
from pages.login_page import LoginPage
from common.logger import Log


class Test_lgin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '8eedcec30404',
            'appPackage': 'com.amethystum.cloud',
            'appActivity': 'com.amethystum.main.view.LauncherActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            # ui获取toast
            'automationName': 'UiAutomator2',
        }
        # 配置
        cls.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(2)
        # 实例化
        # 每子页面的page类都继承了basepage父类，而basepage父类需要传入driver来初始化，所以子类也需传driver来实例化
        cls.login_page = LoginPage(cls.driver)
        cls.handle_page = HandlePage(cls.driver)
        cls.log = Log()

    # def test_login01(self):
    #     self.log.info('开始登录-测试')
    #     self.login_page.agree_ins()
    #     self.login_page.input_username("19124022596")
    #
    #     self.login_page.tran_login_way()
    #     time.sleep(1)
    #     self.login_page.input_passwd("q123456789")
    #     self.login_page.tap_login()
    #     t_info = self.login_page.test_judge().text
    #     self.log.info("未绑定页面提示:"+t_info+", "+str(self.assertEqual('您还未绑定设备', str(t_info))))
    #
    #     self.log.info('测试登录结束\n')

    def test_handle01(self):
        toast_message = "新建文件夹成功"
        self.log.info('开始测试-上传至新建文件夹')
        self.handle_page.upload_btn()
        self.handle_page.create_dir_btn()
        self.handle_page.named_dir_name("TestX_9")
        self.handle_page.confirm_new_dir_btn()

        self.log.info("元素检测:" + str(self.handle_page.find_toast(message=toast_message)))

        self.handle_page.dir_upload_file_btn()
        self.handle_page.upload_pic()
        self.handle_page.choice_pic_type()
        self.handle_page.choice_specific_pic()
        self.handle_page.upload_confirm_btn()
        time.sleep(15)
        self.handle_page.trans_list_back()
        time.sleep(6)
        self.log.info('上传测试结束\n')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()

