# Zbank Ethereum Poof-of-Authority Puppernet Token/Testnet

## Please Read First!

I am student, not a professional programmer, doing an exercise intended for students self-learning blockchain. 

**WARNING:** This assignment involves open-source Ethereum software and online digitial wallet applications. If you plan on doing this project, please make sure you have up-to-date anti-virus software installed on your computer. We are using the **Geth-Network** command-line software, or **"Geth"**, to complete these tasks, and running this software will expose your local computer to the internet. The exposure risk only happens at the final steps when we officially turn on and execute our ethereum testnet to mine our tokens. The latest versions of Geth are much safer from hackers, but still have anti-virus enabled and don't click 'ALLOW' or any permission window that pops up. The real risk is if you share information about your test netowrk or private keys to others online while the network is running.  

A few final things to note about what we're doing:
* This is a custom test-blockchain-network we are building on our local machine. 
* Nothing we do in this project will be on the Ethereum mainnet, or any of the test networks such as: Ropsten, Kovan, or Rinkeby.
* The crypto tokens produced by our testnet will have no monetary value. There's no real Ethereum involved.
* This will be a **proof-of-authority** network. The only nodes running this network should be your own computer.
* Do not share any private keys or network RPC addresses to others online unless you trust them to help you with your testnet.
* Terminating your git bash sessions will immediately stop the network and close your connection online. 

## Premise

We are a blockchain developer working for a fictional bank called ZBank that's looking to get into blockchain. ZBank wants to issue a crypto token called "puppernet". We want to develop a test blockchain-network and mine these tokens. Then we will send these mined bank tokens to a digitial wallet, in this case using MetaMask, and then from MetaMask create a mock transaction to transfer some tokens to another wallet address. All we need is a snapshot of the transaction when it successfully completes. 

## Tools Used

* Git Bash (required), Geth only works in git.
* Geth, or GO-Ethereum, a command-line tool used to generate and run Ethereum-based blockchain networks.  
* MetaMask, an online digitial crypto wallet. There is the option of MyCrypto, but I personally find it better to use MetaMask.

## Setup-Geth

First download the Geth tool. After downloading, store in a folder on your C: drive. I named mine *geth* because it's memorable to me. You'll see multiple applications. The Geth suite has multiple programs. We are only going to to need the **geth** and **puppeth** applications. 

## Part 1 - geth: Creating Network Node 1

Blockchains require nodes to run the network. We create nodes in geth application that will generate wallet addresses.

* On Git-bash navigate to your folder with your Geth tools.
* Enter the command **./geth account new --datadir zbank/node1** and then hit enter. 
* Create a password, or you can hit enter. *I'd advise making a password*. 
* Repeat the password, or hit enter. 
* Generate a wallet address. **Copy the wallet address**. 
* The private key (the password) is stored in a secure keystore file. 
* A folder called **zbank** is created. And inside zbank folder is a subfolder called **node1**. This is what the **--datadir** flag passed in the command does.

## Part 2 - geth: Creating Network Node 2

* Repeat the same command, only change the name of the node. 
* **./geth account new --datadir zbank/node2**
* This will generate its own wallet address. **Copy this wallet address**. There will be a new subfolder for **node2** created. 

Every network node will have its own wallet address, its own subfolder, that will store its own keystore file, and its own copy of the genesis block. 

## Part 3 - puppeth: Creating Puppernet Network and Genesis Block

We use the puppeth application to make an Ethereum test network, and genesis block that is the foundation of any blockchain.

* On Git-bash navigate to your folder with your Geth tools.
* Enter **./puppeth** command to run puppeth applicaiton.
* Enter "puppernet" as the network name in lowercase. Hit enter. *You can't use capital letters, spaces, or symbols in puppeth*.
* What would like to do? Hit option 2, Configure new genesis.
* Create new genesis from scratch.
* Which consensus to use? Option 2, proof-of-authority.
* How many seconds should blocks take? Hit enter. The default is fine.
* **CRITICAL: Which accounts are allowed to seal?** Enter the wallet addresses from your two network nodes created, and do not include the 0x at the beginning. Hit enter.
* **CRITICAL: Which accounts should be pre-funded?** Enter the wallet addresses from your network nodes. Hit enter.
* Should the precompile addresses be re-funded with 1 wei? NO. *We are not going to do that even if it's advisable*. 

## Part 4 - Initialize the genesis block

Every network node requires a copy of the genesis block. We need to go back into the geth application to intialize it.

*

## Part 5 - Start the blockchain

You need to have two Git-bash sessions running. 
