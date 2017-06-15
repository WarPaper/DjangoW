import Crypto
from Crypto.Cipher import AES
import binascii

def ocb_encrypt(key,nonce,associated,plaintext):
    key = binascii.unhexlify(key)
    nonce = binascii.unhexlify(nonce)
    associated = binascii.unhexlify(associated)
    plaintext = binascii.unhexlify(plaintext)
    #print("key:   ",binascii.hexlify(key).upper())
    #print("nonce: ",binascii.hexlify(nonce).upper())
    #print("associated: ",binascii.hexlify(associated).upper())
    #print("plaintext:",binascii.hexlify(plaintext).upper())

    cipher = AES.new(key, AES.MODE_OCB, nonce)
    cipher.update(associated)
    ciphertext, mac = cipher.encrypt_and_digest(plaintext)

    #print("cipher:   %s|%s" % (binascii.hexlify(ciphertext).upper(),binascii.hexlify(mac).upper()))
    #print("expect:   81017F8203F081277152FADE694A0A00",)

    #return binascii.hexlify(ciphertext).upper(),binascii.hexlify(mac).upper()
    return ciphertext,mac

def ocb_decrypt(key,nonce,associated,ciphertext,mac):
    key = binascii.unhexlify(key)
    nonce = binascii.unhexlify(nonce)
    associated = binascii.unhexlify(associated)

    cipher = AES.new(key, AES.MODE_OCB, nonce=nonce)
    try:
        cipher.update(associated)
        plaintext = cipher.decrypt_and_verify(ciphertext, mac)
    except ValueError:
        print("Invalid message")
    else:
        print("decrypted:",binascii.hexlify(plaintext).upper())

    return binascii.hexlify(plaintext).upper()

if __name__ == "__main__":
    ci,tg = ocb_encrypt('000102030405060708090A0B0C0D0E0F','BBAA99887766554433221102','0001020304050607','0001020304050607')
    ocb_decrypt('000102030405060708090A0B0C0D0E0F','BBAA99887766554433221102','0001020304050607',ci,tg)
