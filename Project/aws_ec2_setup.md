
#Section Tutorial Recording:
https://stanford.zoom.us/recording/play/n7vPHA_K4K8d__OvXCkAV0W0LWm_qzVafEjjxAZrpfL5xqkIOGu4IhH9Mw8BI-qf?continueMode=true

#Create instance: 
- need to have limit increase (0 instance to 1, done by aws support ticket)
- go through steps
- switch on protection from interruptions
- increase storage to 500g
- create key pair

#conect to instance:
- connect, select a standalone SSH client
- download as cs230-sgao.pem file

#Tunnel to jupyter
mv ~/Downloads/cs230-sgao.pem !/.ssh
cd ~/.ssh
chmod 400 cs230-sgao.pem
(base) SHENs-MacBook-Pro-2:.ssh shengao1$ ssh -i "cs230-sgao.pem" ubuntu@ec2-52-42-198-109.us-west-2.compute.amazonaws.com
The authenticity of host 'ec2-52-42-198-109.us-west-2.compute.amazonaws.com (52.42.198.109)' can't be established.
ECDSA key fingerprint is SHA256:1HpB/pIq/zuwx0ORsbIP8uSwJbLqysM+Z/67LJ+5/8I.
Are you sure you want to continue connecting (yes/no)? yes

- launch jupyter
sudo apt update
pip3 install jupyter
jupyter notebook (if not showing up, use localhost:9999)

- copy token if no pw is set: 

Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=5e6420dc302e5267be9b3d001a7bc2bd6740bc8a96e151b8&token=5e6420dc302e5267be9b3d001a7bc2bd6740bc8a96e151b8

jupyter pw = 12345

- shutdown instance: click stop on aws webpage