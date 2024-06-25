from Crypto.Cipher import AES
from Crypto.PublicKey import ECC
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

#生成ECC密鑰
privKey = generate_eth_key()
privKeyHex = privKey.to_hex()
pubKeyHex = privKey.public_key.to_hex()





f = open('alice.pri','wt')
f.write(privKeyHex)#生成alice.pri
f.close()

f = open('alice.pub','wt')
f.write(pubKeyHex)
f.close()
