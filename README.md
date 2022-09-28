# Cloud Module Application

This is an web application written in Python. It does things and we'd like help deploying it.

## Requirements and Developing locally

* Python 3.8 or higher is required to run the application
* All requirements are specified in the requirements.txt file
  * You can install the requirements via pip (which comes with python): `pip install -r requirements.txt`
  * the use of Virtualenv is strongly suggested for local development to avoid installing packages globally
* The application can be run via the `flask run` command

## Production

As part of the requirements, gunicorn is installed - the app can be run via `gunicorn server:app`


## Cloud Module Challenge

This repo is used as a challenge for the Cloud Module.

Requirements:
* Deploy this app on [Fly.io](https://fly.io) via a Github Actions Pipeline that runs on each commit.

### Notes on the challenges

* Search engines and blogs/tutorials are your Friends.
* You don't need to learn Python, or even have a local install to complete the challenge. Running the code locally might be fun tho!
* Fly.io is similar to Heroku. Depending on how you learn, you might find it easier to deploy from your local and then move to building a pipeline.
* Help each other and work in groups.
* You will be asked to present and illustrate what you've done to get it working and how you succeeded/failed.

### My Notes on the challenges

 I made the fly.io account and forked the repo 
 I created a fly.io secret and linked that to my forked repo 
 I cloned the repo to my machine
 Signed into fly.io on the command line 
 Ran flyctl, and named my application and choose my region
 Then I deployed it 

