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
    team2 = Team(name='Houston Rockets', location='Houston, TX', team_colors='Red, silver, black, white')
    team3 = Team(name='Golden State Warriors', location='Oakland, CA', team_colors='Royal blue and golden yellow')
    team4 = Team(name='Boston Celtics', location='Boston, MA', team_colors='Green and white')
    player1 = Player(name='LeBron James', age=33, height='6ft 8in', weight='250lbs', position="Forward", jersey_num=23, team_id=1)
    player2 = Player(name='Chris Paul', age=33, height='6ft 0in', weight='175lbs', position="Point guard", jersey_num=3, team_id=2)
    player3 = Player(name='Stephen Curry', age=30, height='6ft 3in', weight='190lbs', position="Point guard", jersey_num=30, team_id=3)
    player4 = Player(name='Kyrie Irving', age=26, height='6ft 3in', weight='193lbs', position="Point guard", jersey_num=11, team_id=4)
    player5 = Player(name='Kevin Love', age=29, height='6ft 10in', weight='251lbs', position="Forward/Center", jersey_num=0, team_id=1)

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)
    db.session.add(team4)
    db.session.add(player1)
    db.session.add(player2)
    db.session.add(player3)
    db.session.add(player4)
    db.session.add(player5)

    db.session.commit()



if __name__ == '__main__':
    manager.run()
