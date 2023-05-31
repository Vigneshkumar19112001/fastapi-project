# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# from base64 import b64decode
# import base64

# key = b'\xce\xd0\x18{](\x89t\x89"q\x06e\x98\xa8N'
# key_string = key.decode('latin1')
# print(key_string)


# encrypted_data = 'sp1Tcj+ODWS9TZ3DCHHTQS3NX4I3q6mg0SS5WSYITTE='  # The encrypted data obtained from the frontend

# def decrypt_password(encrypted_password):
#     key = b'encryptionKey'  # Same encryption key used in the frontend
#     encrypted_password = base64.b64decode(encrypted_password)
#     cipher = AES.new(key, AES.MODE_ECB)
#     decrypted_password = unpad(cipher.decrypt(encrypted_password), AES.block_size).decode('utf-8')
#     return decrypted_password

# decrypt_password(encrypted_data)

