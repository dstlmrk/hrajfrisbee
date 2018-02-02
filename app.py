#!/usr/bin/python
#
# Flask server, woo!
#

import os 
from flask import Flask, request, redirect, url_for, send_from_directory
from time import gmtime, strftime
from flask_mail import Mail, Message


# Setup Flask app.
app = Flask(__name__, static_folder="")
app.debug = True


### config
# email server
MAIL_SERVER = os.getenv("SMTP_SERVER", "localhost")
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

### -- config

mail = Mail(app)


# Routes
@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/wanna-play', methods=["GET", "POST"])
def wanna_play():
  #import ipdb
  #ipdb.set_trace()
  # append email into the textfile
  with open('results.txt', 'a+') as f:
    f.write(strftime("%d.%m.%Y %H:%M", gmtime()) + ": " + request.form['email'] + ", vek: " + request.form['age'] + ", pohlavi: " + request.form['gender'] + "\n") 

  # send an email with information to the user and to us
  msg = Message('Nova registrace na hrajfrisbee.cz', sender='root@hrajfrisbee.cz', recipients=['kacerr.cz@gmail.com'])
  msg.body = 'Uzivatel: ' + request.form['email'] + ', vek: ' + request.form['age'] + ", pohlavi: " + request.form['gender'] + ' prave projevil zajem o frisbee.'
  mail.send(msg)

  # redirect to thank you page
  return redirect(request.url_root + '#thank-you', code=302)

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


if __name__ == '__main__':
  app.run()
