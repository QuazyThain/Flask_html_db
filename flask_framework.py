# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:40:03 2014

@author: quazythain
"""

from flask import Flask
from flask import render_template
from flask import request
from users import Users
app = Flask(__name__)


@app.route("/user/<id>")
def view_user(id=None):
    u = Users()
    name, last_name, user_login = list(u.get_user(id))[0]
    return render_template("index.html", name=name, last_name=last_name,
                           user_login=user_login)


if __name__ == "__main__":
    app.debug = True
    app.run()
