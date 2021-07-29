#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import traceback


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 重写元素定位
    def find_element(self,*loc): # *loc任意数量的位置参数（带单个星号参数）
        try:
            WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('页面未找到%s元素' %(loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print('页面未找到%s元素' % (loc))

    # 获取toast方法
    def find_toast(self, message, timeout=10, poll_frequency=0.01):
        try:
            message1 = "//*[@text=\'{}\']".format(message)
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located((By.XPATH, message1)))
            return element.text
        except:
            traceback.print_exc()
            return False

    # 封装一个长按元素方法
    def long_press(self, loc, t):
        """
        loc 是元素的定位
        t是长按操作持续的时间
        """
        TouchAction(self.driver).long_press(loc, duration=t).perform()

    # 重写send_keys
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

    # 封装判断是否存在toast消息，存在返回True,不存在返回False
    def is_toast_exist(self, driver, text):
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
            e = WebDriverWait(self.driver, 30, 0.01).until(EC.presence_of_element_located(toast_loc))
            print(e.text)
            return True
        except Exception as e:
            print(e)
            return False
