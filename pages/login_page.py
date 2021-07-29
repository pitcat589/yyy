# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction


class LoginPage(BasePage):
    u'登录页面'
    # 定位器，需要用到的元素
    # 同意协议说明按钮
    agree_instruction = (By.ID, "com.amethystum.cloud:id/agree_btn")
    # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView
    # 跳过
    skip_button = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")
    # 切换使用－账号密码登录/验证码登录
    tran_login_ways = (By.ID, "com.amethystum.cloud:id/tv_choose_login_way_tips")
    # 输入账号框
    login_user = (By.ID, "com.amethystum.cloud:id/dropview_edit")
    # 获取登录验证码
    get_login_code = (By.ID, "com.amethystum.cloud:id/cd_btn_captcha")
    # 输入密码框
    login_passwd = (By.ID, "com.amethystum.cloud:id/et_pwd")
    # 登录按钮
    login_button = (By.ID, "com.amethystum.cloud:id/btn_login")
    # 忘记密码
    forget_passwd = (By.ID, "com.amethystum.cloud:id/tv_forget_pwd")
    # 立即注册
    register = (By.ID, "com.amethystum.cloud:id/tv_register")
    # 仅在使用期间有权限
    use_permission = (By.ID, "com.lbe.security.miui:id/permission_allow_foreground_only_button")#红米手机弹出的是系统的弹框定位要改
    # 我的页面按钮
    mine_bt = (By.ID, "com.amethystum.cloud:id/mine_button")

    # 退出登录按钮
    logout_bt = (By.ID, "com.amethystum.cloud:id/logout_btn")
    # 退出登录-确定按钮
    logout_sure_bt = (By.ID, "com.amethystum.cloud:id/sure_btn")

    # 立即绑定按钮
    user_none_bind = (By.ID, "com.amethystum.cloud:id/btn_bind_device")

    user_none_bind_info = (By.ID, "com.amethystum.cloud:id/tv_unbind_device")

    # 切换用户注册按钮
    user_register = (By.ID, "com.amethystum.cloud:id/tv_register")
    # 注册页面标题-com.amethystum.cloud:id/title_txt
    register_title = (By.ID, "com.amethystum.cloud:id/agree_btn")
    # 注册页面－输入注册手机号栏/忘记密码页面-输入手机号码
    register_phone = (By.ID, "com.amethystum.cloud:id/et_phone")
    # 点击获取验证码
    get_verification_code_button = (By.ID, "com.amethystum.cloud:id/cd_btn_captcha")
    # 注册页面－输入验证码栏/忘记密码页面-输入验证码栏
    input_code = (By.ID, "com.amethystum.cloud:id/et_captcha")
    # 滑动验证
    scroll_bar = (By.ID, "com.amethystum.cloud:id/tv_seekbar_tips")
    # 下一步按钮
    to_next_button = (By.ID, "com.amethystum.cloud:id/btn_login")
    # 设置密码---第一次
    set_passwd = (By.ID, "com.amethystum.cloud:id/et_pwd")
    # 设置密码---第二次
    set_passwd_again = (By.ID, "com.amethystum.cloud:id/et_pwd_again")
    # 设置密码完成
    complete_set_passwd = (By.ID, "com.amethystum.cloud:id/btn_complete")
    # 设置密码完成-确认弹窗
    set_passwd_sure = (By.ID, "com.amethystum.cloud:id/sure_btn")

    # 允许紫晶拍摄照片和录制视频+允许访问文件按钮
    allow_take_photo_button = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")

    # 网络搜索绑定按钮
    net_search_bind_btn = (By.ID, "com.amethystum.cloud:id/net_search_bind_btn")

    # 查看绑定教程按钮
    search_bind_course_btn = (By.ID, "com.amethystum.cloud:id/search_bind_course_btn")

    # 进入相册按钮
    photo_album_txt = (By.ID, "com.amethystum.cloud:id/photo_album_txt")

    # 搜索文件输入框id
    search_txt = (By.ID, "com.amethystum.cloud:id/search_txt")

    # 点击安全管理按钮
    security_management_btn = (By.ID, "com.amethystum.cloud:id/tv_security_manager")

    # 第一次点击手势登录手势解锁
    first_gesture_unlock_btn = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[6]/android.view.ViewGroup/android.widget.CompoundButton")

    # 第一次点击手势解锁输入验证密码
    first_password_verification_input = (By.ID, "com.amethystum.cloud:id/password_et")

    # 手势密码登录-切换登录方式
    gesture_switchway_btn = (By.ID, "com.amethystum.cloud:id/switch_login_btn")

    # 手势密码登录-切换帐号
    gesture_switchcount_btn = (By.ID, "com.amethystum.cloud:id/switch_account_btn")

    # 手势密码登录-忘记手势密码
    gesture_switchforget_btn = (By.ID, "com.amethystum.cloud:id/forgot_gesture_btn")

    def test_judge(self):
        time.sleep(1)
        return self.find_element(*self.user_none_bind_info)

    def get_login_code_is(self):
        get_login_code_is_light = self.find_element(*self.get_verification_code_button).is_enabled()
        time.sleep(1)
        print(get_login_code_is_light)

    def agree_ins(self):
        time.sleep(1)
        return self.find_element(*self.agree_instruction).click()

    # 操作用户名输入框
    def input_username(self, user):
        time.sleep(1)
        self.find_element(*self.login_user).clear()
        return self.find_element(*self.login_user).send_keys(user)

    # 切换登录方式
    def tran_login_way(self):
        time.sleep(1)
        return self.find_element(*self.tran_login_ways).click()

    # 密码输入框
    def input_passwd(self, psw):
        time.sleep(1)
        self.find_element(*self.login_passwd).clear()
        return self.find_element(*self.login_passwd).send_keys(psw)

    # 点击登录
    def tap_login(self):
        time.sleep(1)
        return self.find_element(*self.login_button).click()

    # 点击同意权限
    def agree_permission(self):
        time.sleep(1)
        return self.find_element(*self.use_permission).click()

    # 切换我的页面
    def tran_mine_page(self):
        time.sleep(1)
        return self.find_element(*self.mine_bt).click()

    # 点击退出登录
    def tap_logout(self):
        time.sleep(1)
        return self.find_element(*self.logout_bt).click()

    # 再次确认退出登录
    def sure_logout(self):
        time.sleep(1)
        return self.find_element(*self.logout_sure_bt).click()

    # 注册页面群热
    def test_register_judge(self):
        time.sleep(1)
        return self.find_element(*self.register_title)

    # 切换注册到页面
    def switch_register(self):
        time.sleep(1)
        return self.find_element(*self.user_register).click()

    # 操作注册用户名输入框
    def input_register_name(self, user):
        time.sleep(1)
        return self.find_element(*self.register_phone).send_keys(user)

    # 点击获取验证码
    def tap_code(self):
        time.sleep(1)
        return self.find_element(*self.get_verification_code_button).click()

    # 验证码输入框
    def to_input_code(self, code):
        time.sleep(1)
        return self.find_element(*self.input_code).send_keys(code)

    def slide_scroll(self):
        time.sleep(1)
        TouchAction(self.driver).press(x=163, y=931).move_to(x=1011, y=926).release().perform()

    def tap_next(self):
        time.sleep(1)
        return self.find_element(*self.to_next_button).click()

    def set_passwd_first(self, passwd):
        time.sleep(1)
        return self.find_element(*self.set_passwd).send_keys(passwd)

    def set_passwd_second(self, passwd):
        time.sleep(1)
        return self.find_element(*self.set_passwd_again).send_keys(passwd)

    def tap_complete_set_passwd(self):
        time.sleep(1)
        return self.find_element(*self.complete_set_passwd).click()

    def tap_immediate_login(self):
        time.sleep(1)
        return self.find_element(*self.set_passwd_sure).click()

    def tap_bind_device(self):
        time.sleep(1)
        return self.find_element(*self.user_none_bind).click()

    def allow_photo_permission(self):
        time.sleep(1)
        return self.find_element(*self.allow_take_photo_button).click()

    # 点击安全管理按钮
    def security_management_ins(self):
        time.sleep(1)
        return self.find_element(*self.security_management_btn).click()

    # 第一次点击手势解锁
    def first_gesture_unlock(self):
        time.sleep(1)
        return self.find_element(*self.first_gesture_unlock_btn).click()

    # 第一次点击手势解锁账户密码验证
    def first_password_verification(self, passwd):
        time.sleep(1)
        return self.find_element(*self.first_password_verification_input).send_keys(passwd)

    # 第一次绘制密码九宫格
    def first_draw_gesture_password(self):
        time.sleep(1)
        # TouchAction(self.driver).press(x=163, y=931).move_to(x=1011, y=926).release().perform()
        # list_gesture_pwd = self.driver.find_elements_by_class_name("com.amethystum.cloud:id/gesture_lock_view")
        # TouchAction(self.driver).press(list_gesture_pwd[0]).move_to(list_gesture_pwd[0]).move_to(list_gesture_pwd[1]).move_to(list_gesture_pwd[2]).wait(100).move_to(list_gesture_pwd[4]).move_to(list_gesture_pwd[8]).release().perform()
        # print("再次输入手势密码")
        # time.sleep(1)
        # TouchAction(self.driver).press(list_gesture_pwd[0]).move_to(list_gesture_pwd[0]).move_to(list_gesture_pwd[1]).move_to(list_gesture_pwd[2]).wait(100).move_to(list_gesture_pwd[4]).move_to(list_gesture_pwd[8]).release().perform()
        TouchAction(self.driver).press(x=258, y=461).move_to(x=520, y=456).move_to(x=812, y=471).wait(100).move_to(x=812, y=743).move_to(x=812, y=1006).release().perform()
        time.sleep(1)
        TouchAction(self.driver).press(x=258, y=461).move_to(x=520, y=456).move_to(x=812, y=471).wait(100).move_to(x=812, y=743).move_to(x=812, y=1006).release().perform()
    # 登录页绘制手势密码

    def login_draw_gesture_password(self):
        time.sleep(1)
        TouchAction(self.driver).press(x=265, y=858).move_to(x=540, y=858).move_to(x=815, y=858).wait(100).move_to(x=815, y=1150).move_to(x=810, y=1401).release().perform()


    # 手势密码登录-切换登录方式点击
    def user_gesture_switchway(self):
        time.sleep(1)
        return self.find_element(*self.gesture_switchway_btn).click()


    def user_gesture_switchcount(self):
        time.sleep(1)
        return self.find_element(*self.gesture_switchcount_btn).click()

    def user_gesture_switchforget(self):
        time.sleep(1)
        return self.find_element(*self.gesture_switchforget_btn).click()

