from flask import render_template
from flask import request

from CTFd.models import db
from CTFd.utils import admins_only, is_admin

from CTFd.models import db, Challenges, Files, Solves, WrongKeys, Keys, Tags, Teams, Awards, Hints, Unlocks, Gamble

from CTFd import utils


from CTFd.plugins.keys import get_key_class
from CTFd.models import db, Keys

# class Gamble(db.Model):

# use gamble point
def load(app):
    # @app.route('/gamble/', methods=['GET'])
    # def gamble(code):
    #     return render_template('page.html', content="<h1>" + request.args['code'] +  "</h1>")

    @app.route('/gamble/point', methods=['GET'])
    def getPoint():
        teamid = request.args.get('id')
        points = Gamble.query.filter_by(teamid=teamid).all()
        gamble = 0
        for point in points:
            gamble += point.value

        return render_template('page.html', content=gamble)

    @app.route('/gamble/add', methods=['POST'])
    def addGamble():
        return render_template('page.html', content="")

    @app.route('/gamble/shop', methods=['GET, POST'])
    def view_gamble_shop():
        if request.methods == 'POST':
            gamble_point = request.form['gamble_point']

        return render_template('page.html', content="")

