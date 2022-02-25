import hashlib
text =input("Enter what you want to hash--")
hash_object = hashlib. md5(text. encode())
md5_hash = hash_object. hexdigest()
print(md5_hash)

