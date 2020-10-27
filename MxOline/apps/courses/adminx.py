import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


#设置页眉页脚
class GlobalSettings(object):
    site_title = '暮学后台管理系统'
    site_footer = '暮学在线网'
    # menu_style = 'accordion'   折叠菜单

#设置主题
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students']
    search_fields = ['name','desc','detail','degree','students']
    list_filter = ['name','teacher__name','desc','detail','degree','learn_time','students']
    list_editable = ['degree','desc']


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']  #加两个下划线是在课程的某一个字段过滤


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']


class CourseResourceAdmin(object):
    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSettings)

