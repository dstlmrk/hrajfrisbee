#!/usr/bin/python
#
# Flask server, woo!
#

import os
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from time import gmtime, strftime
from flask_mail import Mail, Message



# Setup Flask app.
app = Flask(__name__, static_folder="")
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# models need to be imported after db is initialized
import models

### config
# email server
app.config['MAIL_SERVER'] = os.getenv("SMTP_SERVER", "localhost")
app.config['MAIL_PORT'] = 25
# MAIL_USERNAME = None
# MAIL_PASSWORD = None

### -- config

mail = Mail(app)

# Routes
@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/wanna-play', methods=["GET", "POST"])
def wanna_play():
    from models import Prospect
    # import ipdb
    # ipdb.set_trace()

    # append email into the textfile
    with open('results.txt', 'a+') as f:
        f.write(strftime("%d.%m.%Y %H:%M", gmtime()) + ": " + request.form['email'] + ", vek: " + request.form[
            'age'] + ", pohlavi: " + request.form['gender'] + "\n")

    # write informatin into database
    prospect = Prospect(age=request.form['age'], email=request.form['email'], gender=request.form['gender'])
    db.session.add(prospect)
    db.session.commit()


    # send an email with information to the user and to us
    try:
        msg = Message('Nova registrace na hrajfrisbee.cz', sender='root@hrajfrisbee.cz', recipients=['kacerr.cz@gmail.com'])
        msg.body = 'Uzivatel: ' + request.form['email'] + ', vek: ' + request.form['age'] + ", pohlavi: " + request.form[
            'gender'] + ' prave projevil zajem o frisbee.'
        mail.send(msg)
    except Exception as e:
        print("Something went wrong. {}".format(e))

    # redirect to thank you page
    return redirect(request.url_root + '#thank-you', code=302)


@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)


if __name__ == '__main__':
    # initialize database
    db.create_all()
    # db.session.commit()
    app.run(host='0.0.0.0', debug=True)
