import hashlib

def phash(password):
    return hashlib.sha512(password).hexdigest()