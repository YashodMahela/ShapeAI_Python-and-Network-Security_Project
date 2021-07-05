#Yashod Mahela____ShapeAI

import hashlib

text = input("Enter Text : ").encode()

# hash with SHA-2
#(SHA-256 & SHA-512)
print("SHA-256:", hashlib.sha256(text).hexdigest())

print("SHA-512:", hashlib.sha512(text).hexdigest())

# hash with SHA-3
#(SHA-256 & SHA-512)
print("SHA-3-256:", hashlib.sha3_256(text).hexdigest())

print("SHA-3-512:", hashlib.sha3_512(text).hexdigest())

# hash with BLAKE2
#(SHA-256 & SHA-512)
# 256-bit BLAKE2 (or BLAKE2s)
print("BLAKE2c:", hashlib.blake2s(text).hexdigest())
# 512-bit BLAKE2 (or BLAKE2b)
print("BLAKE2b:", hashlib.blake2b(text).hexdigest())
