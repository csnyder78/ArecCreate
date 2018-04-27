# ArecCreate
create a godaddy A record through API

This is just a simple python script for creating an A record through godaddy.com's API.  One needs to put the folling in their .bashrc or other.  
export GODAD_key=goddaddy_key and export GODAD_secret=secret
then run source ~/.bashrc so that your session re-reads your bash session

This is for python 2.7.

After that just run $python godaddy.py hostname IP_address domain 
