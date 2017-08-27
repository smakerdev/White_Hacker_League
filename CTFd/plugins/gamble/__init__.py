from flask import render_template
from flask import request

from CTFd.models import db
from CTFd.utils import admins_only, is_admin

from CTFd.models import db, Challenges, Files, Solves, WrongKeys, Keys, Tags, Teams, Awards, Hints, Unlocks

from CTFd import utils


from CTFd.plugins.keys import get_key_class
from CTFd.models import db, Keys

# class Gamble(db.Model):

# use gamble point
def load(app):
    @app.route('/gamble/', methods=['GET'])
    def gamble(code):
        return render_template('page.html', content="<h1>" + request.values['code'] +  "</h1>")

    @app.route('/gamble/add', methods=['POST'])
    def addGamble():
        return render_template('page.html', content="")

    @app.route('/gamble/shop', methods=['GET'])
    def view_gamble_shop():
        return render_template('page.html', content="")
        
    