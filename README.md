# misy350-s18-finalapp
Final project for MISY350 - a flask project instructions for setup are included below

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
