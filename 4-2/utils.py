from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

def rsa_keygen():
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    return public_key, private_key

def rsa_encode(key, data):
    key = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(data)

def rsa_decode(key, data):
    key = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(data)

def aes_keygen():
    return get_random_bytes(16)

def aes_encode(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ct_bytes

def aes_decode(key, data):
    iv = data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
    return pt