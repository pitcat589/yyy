#coding:utf-8
from appium import webdriver
import time,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 这个脚本来测试app首次安装使用 权限弹窗问题?

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'W7X6R20721013334',
    'appPackage': 'com.amethystum.cloud',
    'appActivity': 'com.amethystum.main.view.LauncherActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True
}
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)


def always_allow(driver, number=5):
    """
    args :传driver
    number 判断弹窗次数，默认5次
    """
    for i in range(number):
        loc = ('xpath', '//*[@text="允许"]')
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except Exception as a:
            print(a)
            pass


if __name__ == '__main__':
    always_allow(driver)