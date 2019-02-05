import os
from Crypto.Cipher import AES

def decryption(key, fileName):
    textSize = 64 * 1024
    outPutFile = fileName[11:]

    with open(fileName, 'rb') as inputFile:
        fileSize = int(inputFile.read(16))
        IV = inputFile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outPutFile, 'wb') as outputFile:
            while True:
                text = inputFile.read(textSize)

                if len(text) == 0:
                    break

                outputFile.write(decryptor.decrypt(text))
            outputFile.truncate(fileSize)
