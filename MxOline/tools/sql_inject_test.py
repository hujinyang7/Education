import MySQLdb


# username = 'jaye2'
# password = '1993hjy'
#
# conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1993hjy',db='mxonline')
# cursor = conn.cursor()
# sql = "select * from users_userprofile where username='{}' and password='{}'".format(username,password)
# cursor.execute(sql)
#
# for row in cursor.fetchall():
#     print(row)


username = "' or 1=1 #"
password = ''

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='Test')
cursor = conn.cursor()
sql = "select * from users_userprofile where username='{}' and password='{}'".format(username,password)
print(sql)

cursor.execute(sql)

# for row in cursor.fetchall():
#     print(row)


#1.表单验证
#2.查询用户逻辑
#3.Django 的 orm 会对特殊字符转义，orm 会确保用户输入的安全性
