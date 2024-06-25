from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from Crypto.PublicKey import ECC


privateKey = open("alice.pri",'rt',encoding='UTF-8').read()
data = open('data.enc','rb').read()
seckey = open('envelop.dat','rb').read()
iv = b"346BBE8E3F34FFEA"
ensessionkey = decrypt(privateKey,seckey)
#seckey=str(seckey, encoding='latin-1')
#print(seckey)
cipherAES = AES.new(ensessionkey, AES.MODE_CBC,iv=iv)
data = cipherAES.decrypt(data)
print(data.decode("latin-1"))

f = open('data.decode','wt',encoding='UTF-8')
f.write(data.decode("latin-1"))
f.close()



