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
    jersey_num = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teams')
def all_teams():
    teams = Team.query.all()
    return render_template('all-teams.html', teams=teams)


@app.route('/players')
def all_players():
    players = Player.query.all()
    return render_template('all-players.html', players=players)






if __name__ == '__main__':
    app.run()
