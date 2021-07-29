# coding=utf-8
import pymysql.cursors


class ConnectSQL():
    def __init__(self):
        self.db = pymysql.Connect(
            # 正式
            # host='47.107.108.83',
            # 海外 8.209.66.9
            # host='8.209.66.9',

            # 测试
            host='ametest.photoegg.club',
            passwd='$amehc123456',
            port=3306,
            user='root',
            db='cserver'
        )
        self.cur = self.db.cursor()

    # 获取验证码
    def get_code(self,mobile):
        try:
            self.cur.execute("select mobile,sms_code from ame_sms_log where mobile='{}' order by create_time DESC limit 1".format(mobile))
            self.data = self.cur.fetchall()
            # print("{}的验证码:{}".format(self.data[0][0], self.data[0][1]))
            return self.data[0][1]
        except Exception as e:
            print("操作异常：%s" % str(e))
            # 错误回滚
            self.db.rollback()

    # 删除用户注册信息
    def delete_user(self, mobile):
        try:
            self.cur.execute("DELETE from cserver.ame_user where mobile='{}'".format(mobile))
            self.db .commit()
        except Exception as e:
            print("操作异常：%s" % str(e))
            # 错误回滚
            self.db.rollback()

    def close_db(self):
        self.db.close()
        """
            delete_sql = "DELETE from cserver.ame_user where mobile='{}'".format(mobile)
input("回车确认")
cur.execute(delete_sql)

# input("回车确认:enter")
db.commit()

data = cur.fetchall()
print(data)
            """

