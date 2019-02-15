# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sendEmail
   Description :
   Author :       wangyi
   date：          2/15/19
-------------------------------------------------
   Change Activity:
                   2/15/19:
-------------------------------------------------
"""
__author__ = 'wangyi'

import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import traceback


def send_email(name, ex, ex_detail):
    """

    :param name: 程序名
    :param ex: 异常名
    :param ex_detail: 异常细节
    :return:
    """
    # 当前时间
    now_time = datetime.strftime(datetime.today(), "%Y-%m-%d %H:%M:%S:%f")
    msg_from = 'xxxxx@qq.com'
    passwd = 'xxxx'
    msg_to = 'xxx@xxx.com'
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    subject = "【程序异常提醒】{name}-{date}".format(name=name,date=now_time)

    # 标题
    content = '''<div class="emailcontent" style="width:100%;max-width:720px;text-align:left;margin:0 auto;padding-top:80px;padding-bottom:20px">
        <div class="emailtitle">
            <h1 style="color:#fff;background:#51a0e3;line-height:70px;font-size:24px;font-weight:400;padding-left:40px;margin:0">程序运行异常通知</h1>
            <div class="emailtext" style="background:#fff;padding:20px 32px 20px">
                <p style="color:#6e6e6e;font-size:13px;line-height:24px">程序：<span style="color:red;">【{name}】</span>运行过程中出现异常错误，下面是具体的异常信息，请及时核查处理！</p >
                <table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-top:1px solid #eee;border-left:1px solid #eee;color:#6e6e6e;font-size:16px;font-weight:normal">
                    <thead>
                        <tr>
                            <th colspan="2" style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center;background:#f8f8f8">异常详细信息</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center;width:100px">异常简述</td>
                            <td style="padding:10px 20px 10px 30px;border-right:1px solid #eee;border-bottom:1px solid #eee;line-height:30px">{ex}</td>
                        </tr>
                        <tr>
                            <td style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center">异常详情</td>
                            <td style="padding:10px 20px 10px 30px;border-right:1px solid #eee;border-bottom:1px solid #eee;line-height:30px">{ex_detail}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>'''.format(ex=ex,ex_detail=ex_detail,name=name)

    # 正文
    msg = MIMEText(content,_subtype='html',_charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = '程序小助手<{0}>'.format(msg_from)
    msg['To'] = msg_to

    try:
        s.login(msg_from,passwd)
        s.sendmail(msg_from,msg_to,msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print(traceback.format_exc())
        print("发送失败")

    finally:
        s.quit()


if __name__ == '__main__':
    try:
        a = int("哈哈哈")

    except Exception as e:
        print(traceback.format_exc())
        send_email(name="wangyi程序测试",ex=repr(e) ,ex_detail=traceback.format_exc())