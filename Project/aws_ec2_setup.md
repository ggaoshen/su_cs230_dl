
# Section Tutorial Recording:
https://stanford.zoom.us/recording/play/n7vPHA_K4K8d__OvXCkAV0W0LWm_qzVafEjjxAZrpfL5xqkIOGu4IhH9Mw8BI-qf?continueMode=true

# Create instance: 
- need to have limit increase (0 instance to 1, done by aws support ticket)
- go through steps
- choose p2.xlarge
- switch on protection from interruptions
- increase storage to 500g
- create key pair (only need to do once)

#conect to instance:
- connect, select a standalone SSH client
- download cs230-sgao.pem file

# Connect to instance
## in terminal
mv ~/Downloads/cs230-sgao.pem !/.ssh
cd ~/.ssh
chmod 400 cs230-sgao.pem
## (below shows up in popup box on aws web when clicking "connect")
(base) SHENs-MacBook-Pro-2:.ssh shengao1$ 
ssh -i "cs230-sgao.pem" ubuntu@ec2-52-42-198-109.us-west-2.compute.amazonaws.com 

The authenticity of host 'ec2-52-42-198-109.us-west-2.compute.amazonaws.com (52.42.198.109)' can't be established.
ECDSA key fingerprint is SHA256:1HpB/pIq/zuwx0ORsbIP8uSwJbLqysM+Z/67LJ+5/8I.
Are you sure you want to continue connecting (yes/no)? 

yes

## launch jupyter (continue from same terminal)
sudo apt update
pip3 install jupyter
jupyter notebook (if not showing up, use localhost:9999)
## tunnel jupyter: open in new terminal
cd ~/.ssh

ssh -fNL 9999:localhost:8888 -i "cs230-sgao.pem" ubuntu@ec2-52-42-198-109.us-west-2.compute.amazonaws.com

curl http://localhost:9999 # this will open up jupyter, use token in jupyter terminal to login
## (end) tunnel jupyter: open in new terminal
## go back to previous terminal


- copy token to log in or set up new pw: 
Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=5e6420dc302e5267be9b3d001a7bc2bd6740bc8a96e151b8&token=5e6420dc302e5267be9b3d001a7bc2bd6740bc8a96e151b8

- shutdown instance: click stop on aws webpage


## installing other dependencies
- install git on ubuntu
sudo apt install git-all