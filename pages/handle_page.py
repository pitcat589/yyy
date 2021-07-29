# coding:utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction


class HandlePage(BasePage):
    # 登陆后操作

    # 上传按钮
    upload_button = (By.ID, "com.amethystum.cloud:id/iv_add")

    # 新建文件夹按钮
    create_new_dir_button = (By.ID, "com.amethystum.cloud:id/tv_new_dir")

    # 输入文件夹名称输入框
    input_new_dir_name = (By.ID, "com.amethystum.cloud:id/edt_content")

    # 取消新建文件夹按钮---保存路径选择＿取消选择保存按钮
    cancel__button = (By.ID, "com.amethystum.cloud:id/btn_cancel")

    # 确认新建文件夹按钮----创建成功toast---创建文件夹成功
    confirm_create_dir_button = (By.ID, "com.amethystum.cloud:id/btn_confirm")
    # TouchAction(driver).tap(x=351, y=1312).perform()

    # 上传图片按钮
    upload_photo_button = (By.ID, "com.amethystum.cloud:id/tv_upload_photo")

    # 上传视频按钮
    upload_video_button = (By.ID, "com.amethystum.cloud:id/tv_upload_video")

    # 上传文档按钮
    upload_document_button = (By.ID, "com.amethystum.cloud:id/tv_upload_document")

    # 上传音频按钮
    upload_audio_button = (By.ID, "com.amethystum.cloud:id/tv_upload_audio")

    # 上传其他文件按钮
    upload_other_file_button = (By.ID, "com.amethystum.cloud:id/tv_upload_other_file")

    # 选择图片文件3
    choice_pic = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[1]")
    choice_pic__ = (By.XPATH, "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[2]")

    # 确认开始上传按钮
    upload_confirm_button = (By.ID, "com.amethystum.cloud:id/btn_upload")

    # 路径选择
    upload_to_where_confirm_button = (By.ID, "com.amethystum.cloud:id/tv_upload_to_where")

    # 保存路径选择＿我的云盘空间
    upload_to_my_space_c = (By.ID, "com.amethystum.cloud:id/img_select_my_space")

    # 保存路径选择＿共享圈空间
    upload_to_share_c = (By.ID, "com.amethystum.cloud:id/img_select_share_moment")

    # 保存路径选择＿保存按钮
    upload_to_where_save = (By.ID, "com.amethystum.cloud:id/btn_save")

    # 返回上一页
    left_back = (By.ID, "com.amethystum.cloud: id/left_layout")



    """
    /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[1]
        位置定位
    TouchAction(driver).tap(x=595, y=291).perform()
    """

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

    # 传输列表后退按钮
    list_left_ = (By.ID, "com.amethystum.cloud:id/left_layout")#img_left改成了left_layout

    # 传输列表垃圾桶按钮
    list_trash_ = (By.ID, "com.amethystum.cloud:id/right_img")

    # 传输列表选择文件---上传完成文件的选择---清除记录
    choice_trash_file = (By.ID, "com.amethystum.cloud:id/upload_finished_cb")

    # 传输列表选择文件---底部删除按钮
    delete_file_btn = (By.ID, "com.amethystum.cloud:id/bottom_window_delete")

    # 点击上传
    def upload_btn(self):
        time.sleep(1)
        return self.find_element(*self.upload_button).click()

    # 创建新文件夹
    def create_dir_btn(self):
        time.sleep(1)
        return self.find_element(*self.create_new_dir_button).click()

    # 命名新建文件夹名称
    def named_dir_name(self,dir_name):
        time.sleep(1)
        return self.find_element(*self.input_new_dir_name).send_keys(dir_name)

    # 点击确认创建文件夹按钮
    def confirm_new_dir_btn(self):
        time.sleep(1)
        return self.find_element(*self.confirm_create_dir_button).click()

    # 创建文件夹后的上传文件按钮
    def dir_upload_file_btn(self):
        time.sleep(1)
        return TouchAction(self.driver).tap(x=351, y=2000).perform()#该坐标不适用所有手机，需要更改……yaoyao

    # 选择图片上传
    def upload_pic(self):
        time.sleep(1)
        return self.find_element(*self.upload_photo_button).click()

    # 选择对应的图片分类上传
    def choice_pic_type(self):
        time.sleep(1)
        return self.find_element(*self.choice_pic).click()

    # 选择图片分类后具体的图片上传
    def choice_specific_pic(self):
        time.sleep(1)
        return self.find_element(*self.choice_pic__).click()

    # 点击选择图片文件底部的上传按钮
    def upload_confirm_btn(self):
        time.sleep(1)

        return self.find_element(*self.upload_confirm_button).click()

    # 传输列表后退操作
    def trans_list_back(self):
        time.sleep(1)
        return self.find_element(*self.list_left_).click()

