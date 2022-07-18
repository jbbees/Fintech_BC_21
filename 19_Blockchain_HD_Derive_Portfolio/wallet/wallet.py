# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv('keys.env')
mnemonic = os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
 
from constants.py import *
 
# Create a function called `derive_wallets`
def derive_wallets(# YOUR CODE HERE):
    
    # YOUR CODE HERE 
    command = ''

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
# YOUR CODE HERE

coins = {}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE