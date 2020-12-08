#coding：utf-8
#PEP8 简单规范：python 默认库要放在第一，中间放第三方库，自己定义的放在第三; 两个参数中间加空格
from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher, CourseOrg

from DjangoUeditor.models import UEditorField

#1.设计表结构有几个重要的点
'''
实体1 <关系> 实体2
课程  章节  视频  课程资源
'''
#2.实体的具体字段
#3.每个字段的类型，是否必填

class Course(BaseModel):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='讲师')
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name='课程机构')
    name = models.CharField(verbose_name='课程名', max_length=50)
    desc = models.CharField(verbose_name='课程描述', max_length=300)
    learn_time = models.IntegerField(default=0, verbose_name='学习时长（分钟数）')
    degree = models.CharField(verbose_name='难度', choices=(('cj','初级'),('zj','中级'),('gj','高级')), max_length=2)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    notice = models.CharField(verbose_name='课程公告', max_length=300, default='')
    category = models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')
    tag = models.CharField(default='', verbose_name='课程标签', max_length=10)
    youneed_know = models.CharField(default='', max_length=300, verbose_name='课程须知')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name='老师告诉你')
    is_classics = models.BooleanField(default=False, verbose_name='是否经典')

    detail = UEditorField(verbose_name='课程详情', width=950, height=400, imagePath='courses/ueditor/images/',
                          filePath='courses/ueditor/files/', default='')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    is_banner = models.BooleanField(default=False, verbose_name='是否是广告位')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()

    def show_image(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<img src='{}'height='100' width='100'>".format(self.image.url))
    show_image.short_description = '封面图'

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='/course/{}'> 查看详情 </a>".format(self.id))
    go_to.short_description = '跳转'



class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    tag = models.CharField(max_length=100, verbose_name='标签')

    class Meta:
        verbose_name = '课程标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,)#on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    '''null 和 blank的区别
    一个是允许空 一个是允许为none none也是一种类型
    blank的意思是说通过form生成html后，这个字段上会有一个必填的标志，不代表数据库中一定要填写这个字段,
    null表明生成数据表的时候是否必填字段'''
    name = models.CharField(max_length=100, verbose_name='章节名')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长（分钟数）')

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Video(BaseModel):
    lesson = models.ForeignKey(Lesson,verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='视频名')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长（分钟数）')
    url = models.CharField(max_length=1500, verbose_name='访问地址')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    file = models.FileField(upload_to='course/%Y/%m', verbose_name='下载地址', max_length=200)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
