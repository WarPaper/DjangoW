import Crypto
from Crypto.Cipher import AES
import binascii

def ocb_encrypt(key,nonce,associated,plaintext):
    key = binascii.unhexlify(key)
    nonce = binascii.unhexlify(nonce)
    associated = binascii.unhexlify(associated)
    plaintext = binascii.unhexlify(plaintext)
    #print("key:   ",binascii.hexlify(key).upper())
    #print("associated: ",binascii.hexlify(associated).upper())
    #print("nonce: ",binascii.hexlify(nonce).upper())
    #print("plaintext:",binascii.hexlify(plaintext).upper())

    cipher = AES.new(key, AES.MODE_OCB, nonce)
    ciphertext, mac = cipher.encrypt_and_digest(plaintext)

    #print("cipher:   ",binascii.hexlify(ciphertext).upper())
    #print("mac tag:  ",binascii.hexlify(mac).upper())

    return binascii.hexlify(mac).upper(),binascii.hexlify(mac).upper()

def ocb_decrypt(key,ciphertext,mac):
    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, mac)
    except ValueError:
        print("Invalid message")
    else:
        print("decrypted:",binascii.hexlify(plaintext).upper())


if __name__ == "__main__":
    ocb_encrypt('000102030405060708090A0B0C0D0E0F','BBAA99887766554433221101','0001020304050607','0001020304050607')
