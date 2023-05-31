from Crypto.Random import get_random_bytes

# Generate a random AES key
key = get_random_bytes(16)  # 16 bytes key (128 bits)

print('AES Key:', key)