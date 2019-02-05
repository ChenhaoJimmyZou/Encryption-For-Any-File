from Crypto.Hash import SHA256

def getKey(passWord):
    hash = SHA256.new(passWord.encode('utf-8'))
    return hash.digest()
