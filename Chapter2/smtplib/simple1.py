#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import string

HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "xxx@qq.com"
FROM = "xxx@gmail.com"
text = "Python rules them all"
BODY = string.join((
    # 组装整个的方法的邮件主体内容，各个段落以"\r\n"进行分隔
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
), "\r\n")

server = smtplib.SMTP()
server.connect(HOST,"465")
server.starttls()
server.login()
server.sendmail(FROM,[TO], BODY)
server.quit()