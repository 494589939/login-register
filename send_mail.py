from django.core.mail import send_mail
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

'''
Django中发送邮件
settings文件中配置邮件发送参数
用改文件测试发送
'''

if __name__ == '__main__':   

    send_mail(
        '发送邮件标题', 
        '发送邮件内容',
        '494589939@qq.com', # 发送方
        ['494589939@qq.com'], # 接受方
    )