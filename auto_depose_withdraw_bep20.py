#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:35:16 2023

@author: crypto_2024
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:42:45 2023
@author: crypto_2024
"""
from web3 import  Web3, HTTPProvider
from decimal import Decimal
rpc= "https://bsc-dataseed.binance.org"
w3 = Web3(HTTPProvider(rpc)) #实例化Web3
#connecting web3 to Ganache
if w3.is_connected() == True:
    print("web3 connected...\n")
else :
    print("error connecting...")
      
#accounts value and private key
account_1 = "" ## add public key from first account (sender)
account_2 = "" ## add public key from second account (reciver)
private_key = "" ## add ETH private key from first account (sender)
private_key_2 = "" ## add ETH private key from second account (receiver)
account_4='' #another receiver account
#Get balance account_2
balance_2=w3.eth.get_balance(account_2)

#send gas from account_2 to account_1
def build_transaction(balance):
    #get nonce number
    nonce = w3.eth.get_transaction_count(account_2)
    #build transaction
    tx = {
        'nonce':nonce,
        'to':account_1,
        'value':w3.to_wei(balance,'ether'),
        'gas':21000,
        'gasPrice':w3.to_wei('3','gwei')
    }
    #sign transaction with private key
    signed_tx = w3.eth.account.sign_transaction(tx,private_key_2)
    #send Transaction
    tx_hash= w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(w3.to_hex(tx_hash))
build_transaction(0.008)

#withdraw zbc reward
def transfer_zbc(token_contract, source_address,target_address,balance, gas_price=5, gas_limit=500000):
    nonce = w3.eth.get_transaction_count(source_address)
    params = {
        "from": source_address,
        "value": 0,
        'gasPrice': w3.to_wei(gas_price, 'gwei'),
        "gas": gas_limit,
        "nonce": nonce
    }
    func = token_contract.functions.transfer(target_address, w3.to_wei(balance, "ether"))
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash= w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(w3.to_hex(tx_hash))

zbc_bsc_address = w3.to_checksum_address('0x37a56cdcD83Dce2868f721De58cB3830C44C6303')
zbc_bsc_abi ='[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner_","type":"address"},{"internalType":"address","name":"spender_","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account_","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"chainId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender_","type":"address"},{"internalType":"uint256","name":"subtractedValue_","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender_","type":"address"},{"internalType":"uint256","name":"addedValue_","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"},{"internalType":"uint8","name":"decimals_","type":"uint8"},{"internalType":"uint64","name":"sequence_","type":"uint64"},{"internalType":"address","name":"owner_","type":"address"},{"internalType":"uint16","name":"chainId_","type":"uint16"},{"internalType":"bytes32","name":"nativeContract_","type":"bytes32"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nativeContract","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender_","type":"address"},{"internalType":"address","name":"recipient_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"},{"internalType":"uint64","name":"sequence_","type":"uint64"}],"name":"updateDetails","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
token_contract = w3.eth.contract(address=zbc_bsc_address, abi=zbc_bsc_abi)
balance_zbc = w3.from_wei(token_contract.functions.balanceOf(account_1).call(), "ether")    
while balance_zbc==0:
    try:
        balance_zbc = w3.from_wei(token_contract.functions.balanceOf(account_1).call(), "ether")
        print(balance_zbc)
    except Exception as e:
        print(e)
transfer_zbc(token_contract,account_1,account_4,balance_zbc)
#withdraw the gas token
balance_bnb = w3.eth.get_balance(account_1)
gas_fee = 21000*3
gas_fee = Decimal(gas_fee)
gas_fee = w3.from_wei(gas_fee,'Gwei')

def get_balance_loop():
    balance=0
    while True:
        while 0.00005>balance:
            #Get balance account
            balance = w3.eth.get_balance(account_1)
            balance = w3.from_wei(balance, "ether") #convert to ether value
            print(balance)
        try:
            balance = balance-gas_fee
            print(balance)
            print(w3.from_wei(balance, "ether"))
            build_transaction(balance)
        except Exception as e:
            print(e)

def build_transaction(balance):
    #get nonce number
    nonce = w3.eth.get_transaction_count(account_1)
    #build transaction
    tx = {
        'nonce':nonce,
        'to':account_2,
        'value':w3.to_wei(balance,'ether'),
        'gas':21000,
        'gasPrice':w3.to_wei('3','gwei')
    }
    #sign transaction with private key
    signed_tx = w3.eth.account.sign_transaction(tx,private_key)
    #send Transaction
    tx_hash= w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(w3.to_hex(tx_hash))
    get_balance_loop()
get_balance_loop()



    

    