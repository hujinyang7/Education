# coding:utf8
from django.shortcuts import render
from .models import Message

# 配置一个HTML页面显示的步骤
# 1.配置 url
# 2.配置对应的 view 逻辑
# 3.拆分静态文件（css.js，image）放入到 static，html 放入 templates 之下。（可以放到对应的app下面，也可以放到全局的static和templates下）
# 4.配置全局 static 文件访问路径 STATICFILES_DIRS

# def message_form(request):
    # 一、queryset
    # 1.进行for循环
    # 2.进行切片
    # 3.queryset本身并没有执行sql操作,不会查询数据库
    # all_message = Message.objects.all()[:1]

    #二、filter
    # all_message = Message.objects.filter(name='jaye') #等于 select * from message WHERE 'name'='jaye'
    # print(all_message.query)
    # for message in all_message:
    #     print(message.name)

    # 三、get
    # 返回的是一个对象，数据不存在或者有多条数据存在会抛出异常
    # get会马上查询数据库
    # message = Message.objects.get(name='jayee')
    # message.delete()
    # print(message.name)

    #进行数据插入操作
    # message = Message()
    # message.name = 'xiaoming'
    # message.email = 'xiaomingqq.com'
    # message.adders = '四川'
    # message.message = '十二2'
    # message.save()

def message_form(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        adders = request.POST.get('address','')
        message_text = request.POST.get('message','')

        message = Message()
        message.name = name
        message.email = email
        message.adders = adders
        message.message = message_text
        message.save()
        return render(request,'message_form.html',{'message':message})

    if request.method == 'GET':
        var_dict = {}
        all_messages = Message.objects.all()
        if all_messages:
            message = all_messages[16]
            var_dict = {'message' : message}
        return render(request,'message_form.html',var_dict)


