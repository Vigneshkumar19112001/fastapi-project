from Crypto.Util.Padding import unpad
from base64 import b64decode
import base64
from cryptography.fernet import Fernet
from Crypto.Cipher import AES

secret_key = b'06_AFY4rY5lCy6QrPiA3G0OFQKoN06SQUJzr2Iine9U='
cipher_suite = Fernet(secret_key)
print(type(secret_key))
print(type(cipher_suite))

def decrypt_password(password):
    decrypt_data = cipher_suite.decrypt(password.encode())
    print(decrypt_data.decode())


decrypt_password("U2FsdGVkX18jN23EKuAtXf8eNv55c3Oyw0dCe39jIVs=")