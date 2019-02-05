import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import Encryption.py
import Decryption.py
import Generate_Key.py

def Main():
    correct_Key = ['E', 'e', 'D', 'd']
    quit_Key = ['N', 'n']
    print("Welcome to the Smart Encryption program!")
    while True:
        task = input("Would you like to perform Encryption or Decryption? Enter E/e for Encryption or D/d for Decryption...")
        if task in correct_Key:
            if task == 'E' or task == 'e':
                fileName = input("Please enter the name of the file you wish to encrypt: ")
                passWord = input("Please set a password: ")
                encryption(getKey(passWord), filename)
                print("Finished.")
            else:
                fileName = input("Please enter the name of the file you wish to decrypt: ")
                passWord = input("Please enter the password: ")
                decryption(getKey(passWord), fileName)
                print("Finished.")
            continue_option = input("Do you want to perform another tesk? Please enter any key besides N/n to continue, or N/n to quit...")
            if (continue_option in quit_Key):
                break;
        else:
            exit_option = input("No/Wrong option selected, please enter any key besides N/n to try again or N/n to quit...")
            if (continue_option in quit_Key):
                break;
    print("Thanks for using the program!")

if __name__ == '__main__':
    Main()
