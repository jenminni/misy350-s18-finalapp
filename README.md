# MISY350 Final Project
This repo contains my final project for MISY350. <br/>

It is a flask project that includes a web app that allows users access to a database (design details below)
that includes information about the teams and players that have made it to the Conference Finals of the NBA Playoffs. Users are able to view the database, and edit the players or teams as the playoffs continue. There is also an 'About' section of this app that includes some info about me! Instructions for setup are included below. <br/>


# Setup Directions:
Python version 2.7x is needed.
In addition, `virtualenv` is required.
If virtual environment is not already in the project folder, set it up by using the following commands in terminal:

The following command will install virtual environment  

`$ virtual venv`

Next, activate the virtual environment  

`$ source venv/bin/activate`

Install the necessary packages for the project  

`$ pip install -r requirements.txt`

Then, initialize the database  

`$ python manage.py deploy`

Next, to run the development server (should use -d to run the debugger and automatic reloader)

`$ python manage.py runserver -d`



# Database Design:
There are two tables included in my database: Teams and Players. <br/>
There is a one-to-many relationship between the two - as a team can only have one-to-many players, but a player belongs to one and only one team. <br/>

The tables are illustrated below:

Players | Teams
--------|------
ID(PK) | ID(PK)
Name | Name
Age | Location
Height | Team Colors
Weight |        
Position |       
Jersey Number |       
Team ID(FK)   |

Where: <br/>
PK = Primary Key of that table <br/>
FK = Foreign Key of that table
