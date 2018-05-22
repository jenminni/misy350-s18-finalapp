import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


# setting up SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# defining database tables
class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    team_colors = db.Column(db.Text)
    players = db.relationship('Player', backref='team', cascade='delete')


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    height = db.Column(db.Text)
    weight = db.Column(db.Text)
    position = db.Column(db.Text)
    jersey_num = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/teams')
def all_teams():
    teams = Team.query.all()
    return render_template('all-teams.html', teams=teams)


@app.route('/players')
def all_players():
    players = Player.query.all()
    return render_template('all-players.html', players=players)


@app.route('/teams/edit/<int:id>', methods=['GET', 'POST'])
def teams_edit(id):
    teams = Team.query.filter_by(id=id).first()
    if request.method == 'GET': # show the form to update
        return render_template('team-edit.html', teams=teams)

    if request.method == 'POST': # this is update
        teams.name = request.form['name']
        teams.location = request.form['location']
        teams.team_colors = request.form['team_colors']
        db.session.commit()
    return redirect(url_for('all_teams'))


@app.route('/players/edit/<int:id>', methods=['GET', 'POST'])
def players_edit(id):
    players = Player.query.filter_by(id=id).first()
    if request.method == 'GET': # show the form to update
        return render_template('player-edit.html', players=players)

    if request.method == 'POST': # this is update
        players.name = request.form['name']
        players.age = request.form['age']
        players.height = request.form['height']
        players.weight = request.form['weight']
        players.position = request.form['position']
        players.jersey_num = request.form['jersey_num']
        db.session.commit()
    return redirect(url_for('all_players'))




if __name__ == '__main__':
    app.run()
