from flask_script import Manager
from nba import app, db, Team, Player

manager = Manager(app)


@manager.command
def deploy():
    print "resetting database..."
    db.drop_all()
    db.create_all()

    print "inserting initial data..."
    team1 = Team(name='Cleveland Cavaliers', location='Cleveland, OH', team_colors='Maroon and yellow')
    team2 = Team(name='Philadelphia 76ers', location='Philadelphia, PA', team_colors='Red, white, and blue')
    player1 = Player(name='LeBron James', age=33, height='6ft 8in', weight='250lbs', jersey_num=23)
    player2 = Player(name='Joel Embiid', age=24, height='7ft 0in', weight='249lbs', jersey_num=21)

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(player1)
    db.session.add(player2)

    db.session.commit()



if __name__ == '__main__':
    manager.run()
