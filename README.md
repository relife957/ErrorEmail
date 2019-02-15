# ErrorEmail
当程序发生错误时发送邮件提示( Send a mail alert when an error occurs in the program)

## 声明
不是原创

## 使用
在程序中`msg_from = 'xxxxx@qq.com' ; passwd = 'xxxx' ; msg_to = 'xxx@xxx.com'
`这段代码中分别填写自己的信息,msg_from填写发送邮件的邮箱地址,passwd填写对应邮箱设置的客户端授权码,不是你的邮箱密码,msg_to填写接收邮箱的地址;

这段程序暂时适合qq邮箱发送,如果要使用其他邮箱,修改这段代码`s = smtplib.SMTP_SSL('smtp.qq.com', 465)`中的`smtp.qq.com`和后面的端口号465

## 效果图

[![kreSOA.md.jpg](https://s2.ax1x.com/2019/02/15/kreSOA.md.jpg)](https://imgchr.com/i/kreSOA)