#Yashod Mahela_____ShapeAI

import hashlib

def Md5Convert(text):
   Hash = hashlib.md5()
   Hash.update(text.encode('utf-8'))
   print(Hash.hexdigest())

text = input("Enter Your text : ")

Md5Convert(text)
