import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag, BannerCourse
from xadmin.layout import Fieldset, Main, Side, Row
#设置页眉页脚
class GlobalSettings(object):
    site_title = '暮学后台管理系统'
    site_footer = '暮学在线网'
    # menu_style = 'accordion'   折叠菜单

#设置主题
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


# class LessonInline(object):
#     model = Lesson
#     extra = 0

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students']
    search_fields = ['name','desc','detail','degree','students']
    list_filter = ['name','teacher__name','desc','detail','degree','learn_time','students']
    list_editable = ['degree','desc']


class BannerCourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students']
    search_fields = ['name','desc','detail','degree','students']
    list_filter = ['name','teacher__name','desc','detail','degree','learn_time','students']
    list_editable = ['degree','desc']
    model_icon = 'fa fa-window-restore'

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(is_banner=True)
        return qs


from import_export import resources
class MyResource(resources.ModelResource):

    class Meta:
        model = Course
        # fields = ('name', 'description',)
        # exclude = ()

class NewCourseAdmin(object):
    import_export_args = {'import_resource_class': MyResource, 'export_resource_class': MyResource}
    list_display = ['name', 'desc', 'show_image', 'go_to', 'detail', 'degree', 'learn_time', 'students']
    search_fields = ['name','desc','detail','degree','students']
    list_filter = ['name','teacher__name','desc','detail','degree','learn_time','students']
    list_editable = ['degree','desc']
    # readonly_fields = ['click_nums', 'fav_nums', 'students', ]
    exclude = ['add_time']
    ordering = ['-students']
    model_icon = 'fa fa-book'  #自定义图标
    # inlines = [LessonInline]
    #配置富文本
    style_fields = {
        "detail": "ueditor"
    }

    def queryset(self):
        qs = super().queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(teacher=self.request.user.teacher)
        return qs

    def get_form_layout(self):
        #判断是编辑页面才是新格式（可以控制编辑/新增页面的格式）
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(
                        '讲师信息',
                        'teacher','course_org',
                        css_class='unsort no_title'
                    ),
                    Fieldset(
                        '基本信息',
                        'name', 'desc',
                        Row('learn_time', 'degree'),
                        Row('category', 'tag'),
                        'youneed_konw', 'teacher_tell', 'detail'
                    ),
                ),
                Side(
                    Fieldset('访问信息',
                             'fav_nums', 'click_nums', 'students', 'add_time'
                             ),
                ),
                Side(
                    Fieldset('选择信息',
                             'is_banner', 'is_classics',
                             ),
                ),
            )
            return super(NewCourseAdmin, self).get_form_layout()




class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name','add_time']  #加两个下划线是在课程的某一个字段过滤
    model_icon = 'fa fa-sticky-note-o'


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']
    model_icon = 'fa fa-video-camera'


class CourseResourceAdmin(object):
    list_display = ['course','name','file','add_time']
    search_fields = ['course','name','file']
    list_filter = ['course','name','file','add_time']
    model_icon = 'fa fa-gift'

class CourseTagAdmin(object):
    list_display = ['course','tag', 'add_time']
    search_fields = ['course','tag']
    list_filter = ['course','tag', 'add_time']
    model_icon = 'fa fa-tags'

# xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Course, NewCourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)



xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)

xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSettings)

