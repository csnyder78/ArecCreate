#!/usr/bin/python

import sys 
import os

from godaddypy import Client, Account
my_acct = Account(api_key=os.environ['GODAD_key'], api_secret=os.environ['GODAD_secret'])
client = Client(my_acct)

client.add_record(sys.argv[3], {'data':sys.argv[2],'name':sys.argv[1],'ttl':3600, 'type':'A'})

