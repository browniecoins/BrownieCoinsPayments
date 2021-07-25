from web3 import Web3
import json
import config
import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
print (sys.argv[1])

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())
#newArg = sys.argv[1].split('<TO>')
newArg = sys.argv[1].split('ARMENMERIKYAN')

main_address= newArg[1]
contract_address = Web3.toChecksumAddress(newArg[2]) #be sure to use a BSC Address in uppercase format like this 0x9F0818B...

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')

contract = web3.eth.contract(contract_address, abi=abi)

#contract.functions.balanceOf('0x2551d2357c8da54b7d330917e0e769d33f1f5b93').call()


totalSupply = contract.functions.totalSupply().call()

print(web3.fromWei(totalSupply, 'ether'))

print(contract.functions.name().call())
print(contract.functions.symbol().call())


balanceOf = contract.functions.balanceOf(main_address).call()

me = newArg[1]  #send from this address
main_address= '0xf118EAC07d6afe59B62A1d2E9f8AA5D87DDB2Bb7'   #to this address
#main_address = '0xf83d4C26A4A18b73E89baA9874639903Fb7f4C34'
#send = 10
print(main_address)

#amount = web3.toWei(send, 'ether')
#amount =  69 *1000000000
amount =  int(newArg[0]) *1000000000
#amount = 2000000000
print(type(amount))
print(amount)

nonce = web3.eth.getTransactionCount(me)
print(nonce)

token_tx = contract.functions.transfer(main_address, amount).buildTransaction({
    'chainId':56, 'gas': 200000,'gasPrice': web3.toWei('10','gwei'), 'nonce':nonce
})
# TURNED OFF TRANS SIGN
sign_txn = web3.eth.account.signTransaction(token_tx, private_key=newArg[3])
web3.eth.sendRawTransaction(sign_txn.rawTransaction)
print(f"Transaction has been sent to {main_address}")
