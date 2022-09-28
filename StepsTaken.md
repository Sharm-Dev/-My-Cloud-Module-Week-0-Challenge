### Week 0 Challenge

The steps I took to complete this challenge

### Steps to run on my local 

1. Downloaded the files 
2. Created my own repo as the class one is private 
3. In my repo on my local, created a virtual environment
- python3 -m venv venv 
4.  Activated my virtual environment
- . venv/bin/activate
5. Then installed the requirements for the virtual environment
- pip install -r requirements.txt
6. Then ran the application 
- flask --app server run 

### Deploying to Git hub then to fly.io with continuous commits 

1. In terminal git my API token key
- flyctl auth token 
2. Then in git hub in my repo
- Settings 
- Secrets 
- Actions 
- New reposirory secert 
- Name - FLY_API_TOKEN
- Secert - The token from my terminal 
- Clicked add secert 
3. Then created a fly.toml file in my terminal 
- flycrl apps create
- Choose a name - left if blank for a random one, and hoped for a good name!!!!
- and it wasnt good, Oh well...
4. Then created a github folder, workflows folder and main.yml file
5. Then entered the contents from - https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/ from step 8 
6. Then pushed and prayed for the magic to happen!!!!!!!

### Had some trouble with my app

### In fly.io on the hostname when clicked had a HTTP ERROR 403 page

1. In my app I decided to make my fly.toml again so I ran and went through a new stepup, over writing my app and fly.io file
- flyctl launch

This worked above, now the link in fly.io is updated on ever commit to github

...Also I got a nicer app name its called patient breeze 

........ very ironic and I have been patient but it was not a breeze but loved the challenge   





