from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200,verbose_name='姓名')  #CharField最大长度必填，verbose_name可以理解为注释
    email = models.EmailField(verbose_name='邮箱')
    adders = models.CharField(max_length=100,verbose_name='联系地址')
    message = models.TextField(verbose_name='留言信息')

    class Meta:
        verbose_name = '留言信息'  #自定义一个易于理解的名称
        verbose_name_plural =verbose_name   #如果此项没有设置，Django 会使用 verbose_name + "s"来表示。
        db_table = 'message'   #自定义表名,默认数据表的命名规则为 应用名_类名


