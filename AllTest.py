__author__ = 'zengyue'
#coding=utf-8
import unittest,time
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os



#==========定义发送邮件===========

def send_mail(file_new):
    sender = 'XXX@163.com'
    receiver = 'XXX@XXX.com'
    smtpserver = 'smtp.163.com'
    username = 'XXX@163.com'
    password = '******'
    #定义邮件
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '%s 自动化测试报告 ' %time.strftime('%Y-%m-%d %H_%M')
    #定义正文
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    file=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(file)

    #构建附件
    att = MIMEText(open('%s' % file_new,'rb').read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att)

    #定义发送时间
    msg['date']=time.strftime('%a,%d%b%Y%H:%M:%S%z')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print 'email has send out!'



#==========查找测试报告目录，找到最新生成的测试报告文件==========

def send_report(testreport):
    result_dir=testreport
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir+fn))
    print (u'最新测试生成的报告：'+lists[-1])
    #找到最新生成的文件
    file_new=os.path.join(result_dir,lists[-1])
    print file_new
    #调用发送邮件模块
    send_mail(file_new)


#==========将用例添加到测试套件==========

def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='/Users/zengyue/PycharmProjects/API_Test/Test_Case/'
    #定义discover方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test*.py',top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print test_case
        testunit.addTests(test_case)
    return testunit

if __name__ == '__main__':
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    testreport='/Users/zengyue/PycharmProjects/API_Test/Report/'
    filename=testreport+now+'result.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'API自动化测试报告',
        description=u'用例执行情况:'
    )
    alltestnames=creatsuite()
    runner.run(alltestnames)
    fp.close()#关闭生成的报告
    send_report(testreport) #发送报告