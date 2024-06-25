from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from Crypto.PublicKey import ECC
#讀檔 alice.pri
"""
f = open('alice.pri','rt')
key = ECC.import_key(f.read())#讀alice.pri
"""


#讀取 pubk
f= open('alice.pub','rt')
key = f.read()
f.close()

#f1 = open ('data.txt',"rt",encoding="utf-8")
f1 = open ('data.txt',"rt")
data=  f1.read()
data = bytes(data,encoding='UTF-8')#utf-8
f1.close()

#key= key.public_key().export_key(format='SEC1')
#key=unicode(key, errors='ignore')
#print(key)
#bytes(key.pointQ,encoding='utf-8')


#建立隨機 AES key
sessionkey=get_random_bytes(16)
iv = b"346BBE8E3F34FFEA"
# 以 ECC 金鑰加密 Session 金鑰


ensessionkey = encrypt(key,sessionkey)

#ciphperECC = PKCS1_OAEP.new(key)
#ensessionkey = encrypt(newkey,sessionkey)
#print(ensessionkey)
#print("+++++++++++++++++++++++++")
#print()
#encSessionKey = ciphperECC.encrypt(sessionkey)



# 以ecc加密data
cipherAES =  AES.new(sessionkey, AES.MODE_CBC,iv=iv)
ct_bytes = cipherAES.encrypt(pad(data, AES.block_size))
print(ct_bytes)

f = open('data.enc','wb+')
f.write(ct_bytes)#生成alice.pri
f.close()

f= open('envelop.dat','wb+')
f.write(ensessionkey)
f.close()

