import pymysql.cursors

db = pymysql.Connect(
    host='ametest.photoegg.club',
#测试环境：ametest.photoegg.club/正式环境：47.107.108.83
#海外：8.209.66.9
    port=3306,
    user='root',
    passwd='$amehc123456',
#$amehc123456正式环境去掉hc
    db='cserver'
)

cur = db.cursor()

mobile = input("请输入号码:")

cur.execute("select * from ame_user where mobile='{}'".format(mobile))
#如果是海外环境请给{}加上引号为'{}'

data = cur.fetchall()
print(data)

delete_sql = "DELETE from ame_user where mobile='{}'".format(mobile)
#如果是海外环境请给{}加上引号为'{}'
cur.execute(delete_sql)
# input("回车确认:{}".format(delete_sql))
# 提交后确认
db.commit()

data = cur.fetchall()
print(data)


def delete_db(sql_delete):
    '''删除操作'''
    # 打开数据库连接
    db = pymysql.Connect(
        host='ametest.photoegg.club',
        port=3306,
        user='root',
        passwd='$amehc123456',
        db='cserver'
    )

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    try:
        cur.execute(sql_delete)  # 执行
        # 提交
        db.commit()
    except Exception as e:
        print("操作异常：%s" % str(e))
        # 错误回滚
        db.rollback()
    finally:
        db.close()
