# Import HD Derive wallets.
# Capturing output from the standard output buffer, from command line into python. 
# Enter 
# HD Derive can only be executed on command line. This program will import it into python script and execute it. 
# python script that can be used to build a universal wallet manager.

import subprocess     # lib that permits command-line tools in python.
import json           

# store the command line command we want to run. 
# make sure to use the --format=json or --format=jsonpretty in your command
command = './der -g --key="xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c" --cols=path,address,privkey,pubkey --coin=ETH --format=jsonpretty'   # this is the command-line command we will execute. 


# Create a subprocess object
# Popen() and pass the command
# command line programs has 2 standard ports/buffer it displays output to. stdout and stderr. 
# stdout is output, so if command is valid this is the port that works. 
# stderr is if there's an error. So command not found comes
# shell=True means program is interactive 
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) 

# Capture the output on the command line and imported as a tuple. p.communicate will receive output from both buffers. 
(output, err) = p.communicate 

# Caputres the status
p_status = p.wait()

# print the output command line buffer
print(output)

# load the command output into a json format object called keys
keys = json.load(output)
print(keys)

# print first wallet address
print(keys[0]['address'])

#parse through the json object called keys to fetch the first 5 wallet addresses.
for i in range(5):
    print(keys[i]['address'])




