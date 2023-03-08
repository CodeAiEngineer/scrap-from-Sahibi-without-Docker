# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_mail import Message


# E-posta gönderme
class SendMail:
    def send_email(self,aracListesiStr,email):
        app = Flask(__name__)
        app.config['MAIL_DEFAULT_SENDER'] = 'info@example.com'
        app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
        app.config['MAIL_PORT'] = 2525
        app.config['MAIL_USERNAME'] = '70ef773e4d2346'
        app.config['MAIL_PASSWORD'] = '363b75bc961bf8'
        app.config['AUTH'] = 'PLAIN'
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False

        mail = Mail(app)

        with app.app_context():
            message = Message('Başlık', recipients=[email])
            message.body = str(aracListesiStr)
            mail.send(message)