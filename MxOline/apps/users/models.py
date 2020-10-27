#coding:utf-8
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (('male','男'),('female','女'))


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        abstract = True   #此类不可生成对象，必须被继承使用。 Abstract可以将子类的共性最大限度的抽取出来，放在父类中，以提高程序的简洁性。


class UserProfile(AbstractUser):
    nick_name =models.CharField(max_length=50,verbose_name='昵称',default='')
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(verbose_name='性别',choices=GENDER_CHOICES,max_length=6)
    address = models.CharField(max_length=100,verbose_name='地址',default='')
    mobile = models.CharField(max_length=11,verbose_name='手机号码')
    image = models.ImageField(upload_to='head_image/%Y/%m',default='default.jpg',verbose_name='用户头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
