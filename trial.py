# BLAST
#from jsonrpc import ServiceProxy
from jsonrpc import ServiceProxy
from binascii import hexlify, unhexlify
import hashlib
from merkletools import *
import cPickle as pickle
from secp256k1 import PrivateKey, PublicKey
import random, string
import time
import thread
import requests
import json

EPOCH_TIME=1

gen_tx = "fc64c5ad44c7fd43891392699a5dfd9d499207ee6f073a85e67093897ed79456"

rpc_user = "gatto"
rpc_pwd = "gatto"
rpc = ServiceProxy("http://%s:%s@127.0.0.1:18332/" % (rpc_user, rpc_pwd))


print rpc.getblockcount()
rpc.generate(100)
print rpc.getblockcount()

my_tx = "fcd690be5e2b659fddf8770e67107087bcf5a620818d949f24b9cf3a30f631f9"


unspent_txs = rpc.listunspent()
#print rpc.listunspent()
for utx in unspent_txs:
	if(utx['txid'] in my_tx):
		print utx
		sel_tx = utx
		in_txid = utx['txid']
		in_vout = utx['vout']
print "THIS: ", in_vout, "\n"
print "List: ", sel_tx

print "Searching for ... ", my_tx, "\n"
sel_tx = rpc.gettransaction(my_tx)
print sel_tx, "\n"
print sel_tx['txid'], "\n"
print sel_tx['vout'], "\n"
