#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: email.py
@time: 2018/12/4 8:47
@desc:
"""
from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            return False


def send_email(to, subject, template, **kwargs):
    msg = Message('[FISHER]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
