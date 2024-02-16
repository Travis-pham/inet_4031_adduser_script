# inet_4031_adduser_script
## Description: 
These files are a part of the 4th lab in my INET4031 - Intro to Systems class at the University of Minnesota. The purpose of this script is to automate the process of adding new users to a system and to assign them to certain groups. The reason for this script creation is to cut down the time it takes to do the tedious task of adding users. 
## Operation:
Requirements to run the script - Python 2 downloaded, Linux system, and proper permissions to add users and assign groups. You would also need the python script file and an input file with all of the users/groups that the user needs to be added. 

The script expects input lines to be in this format - username:password:firstname:lastname:groups
Lines starting with # are considered comments and are ignored by the script.

This script takes in the input file by running either of these two codes in the terminal.

1. sudo ./create-users.py < create-users.input
2. at create-users.input | sudo ./create-users.py
