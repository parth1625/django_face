# face_recognition heroku_project python setup

# Pre-requisites:
- free Heroku account
- Python installed locally
- Postgres installed locally

# Install heroku(Ubuntu):
- sudo snap install heroku --classic

# Login to heroku command line:
- heroku login

# Clone project from Git(Locally):
- git clone https://github.com/(repo-name)/(project-name).git
- cd (project-name)

# Create heroku app:
- heroku create 
- OR you can use Heroku GUI

# Create heroku remote:     (For existing app)  
- heroku git:remote -a (app-name)

# Deploy app to Heroku:
- git push heroku master

# Define a Procfile(on local root project directory):
- web: gunicorn mysite.wsgi  (Folder which contains your settings.py file)

# Create a Aptfile to install apt packages for OpenCV:
- libsm6
- libxrender1
- libfontconfig1
- libice6

# Add builpacks to heroku:
- heroku buildpacks:add --index 1 heroku-community/apt
- heroku create --buildpack https://github.com/paulfurley/heroku-buildpack-python-opencv-3.1.0.git
- heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt

# Declare app dependencies:
- pip3 install -r requiremenst.txt
- pip3 freeze > requirements.txt

# Collect static files(Locally):
- python3 manage.py collectstatic

# Deploy again after changes:
- git add .
- git commit -m "Demo"
- git push heroku master
- heroku open