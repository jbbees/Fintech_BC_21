# Crypto Wallet Manager using HD Wallet Derive

* We will create a python program to act as a multi-wallet manager.
* We will use the command-line program `hd-wallet-derive` to generate test software wallets.
* We will execute command line functions within python script using the `subprocess` library.
* We will capture command line output and store in python to execute additional tasks.

## Wallet.py

This is our main program. This program's purpose is to serve as a multi-wallet manager for different crypto currencies our generated software wallets will store. The cryptos are defined in the `constants.py` program we import into main code. 

We will use this program to execute command line tasks only done in `hd-wallet-derive` from python, and then we will capture the command line output and store into python 

## Wallet Keys Environment Variable

We will store the `private key` and/or `mnemonic phrase` generated in `hd-wallet-derive.php` into an **environment variable** file. When we execute our program we will read in the `.env` file using the `os.getenv` function and get the wallet private keys.

## Constants.py

We create a secondary python script called `constants.py` that declares string variables for different coins we will work with. We will import this program into our main program using `from contstant import *`

