import hashlib
import os

password = input("Enter Your password : ")
password = password.encode()
salt = os.urandom(16)
password_hash = hashlib.pbkdf2_hmac("sha256", password, salt, 100000)

print(password_hash)
