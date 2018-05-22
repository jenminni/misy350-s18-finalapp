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
    about = db.Column(db.Text)
    location = db.Column(db.Text)
    team_colors = db.Column(db.Text)
    players = db.relationship('Players', backref='team', cascade='delete')


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    jersey_num = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run()
