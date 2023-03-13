# Enigmis.py

"""A cipher program that Encrypts and Decrypts different ciphers."""

import secrets
import string

class Caesar():
    """Caesar Cipher.
There is two functions, Encrypt and Decrypt.

Encrypt Function
To use this function put in the open-and-close
parentheses the message and the shift number (how many time you shift)

Example:
Caesar.Encrypt("GOTOPARK", 3)

----------------------------------------------------------------------------------

Decrypt Function
To use this function put in the open-and-close
parentheses the Encrypt message and the shift number key (how many time you shift)

Example:
Caesar.Decrypt((your msg), 3)
"""
    def Encrypt(msg, shift):
        shift = shift
        msg = msg
        output = ""
        
        if isinstance(msg, str):
            for letter in msg:
                x = ord(letter)+shift
                y = chr(x)

                output += y
            return output
        else:
            print("Input Error: Type is not a 'str'")
    
    def Decrypt(msg, shift):
        shift = shift
        msg = msg
        output = ""
        
        if isinstance(msg, str):
            for letter in msg:
                x = ord(letter)-shift
                y = chr(x)
                
                output += y
            return output
        else:
            print("Input Error: Type is not a 'str'")

class Vigen():
    """The Vigenère cipher
There is two functions, Encrypt and Decrypt.

Encrypt Function
To use this function put in the open-and-close
parentheses the message and the key.

Example:
Vigen.Encrypt("GOTOPARK", "BluePoo")

----------------------------------------------------------------------------------

Decrypt Function
To use this function put in the open-and-close
parentheses the Encrypt message and the key.

Example:
Vigen.Decrypt((your msg), 3)
"""
    
    def Encrypt(msg, key):
        message = msg
        key = key
        output = ""

        if isinstance(msg, str):
            for keys in key:
                keytonumber = ord(keys)
            for messages in message:
                messagex = ord(messages) + keytonumber
                messagey = chr(messagex)

                output += messagey
            return output
        else:
            print("Input Error: Type is not a 'str'")
        
    def Decrypt(msg, key):
        message = msg
        key = key
        output = ""

        if isinstance(msg, str):
            for keys in key:
                keytonumber = ord(keys)
            for messages in message:
                messagex = ord(messages) - keytonumber
                messagey = chr(messagex)
                output += messagey
            return output
        else:
            print("Input Error: Type is not a 'str'")

class OTpad():
    """OTpad (One-time-pad) cipher
There is two functions, Encrypt and Decrypt.

Encrypt Function
To use this function put in the open-and-close
parentheses the message, key length, and shwkey pram

Example:
OTpad.Encrypt("GOTOPARK", 30, True)

----------------------------------------------------------------------------------

Decrypt Function
To use this function put in the open-and-close
parentheses the Encrypt message and the the Key (The key should be a string and is letters)

Example:
OTpad.Decrypt((your msg), "BluePoo")

"""
    
    def randomKey(length):
        alphabet = string.ascii_letters
        return ''.join(secrets.choice(alphabet) for i in range(length))
    
    def Encrypt(msg, Kylngth, shwky):
        msg = msg
        shwky = shwky
        output = ""
        Kylngth = Kylngth
        key = OTpad.randomKey(Kylngth)
        
        # sanitize the input
        if not isinstance(msg, str) or not msg.isalpha():
            raise ValueError("Input Error: Encrypted message must be a string containing only letters")
        if not isinstance(Kylngth, int) or Kylngth <= 0:
            raise ValueError("Input Error: Key length must be a positive integer")
        
        for keys in key:
            keytonumber = ord(keys)
        for messages in msg:
            messagex = ord(messages) + keytonumber
            messagey = chr(messagex)
            output += messagey
        if shwky == True:
            print(key)
            return output
        else:
            return output
    
    def Decrypt(msg, key):
        msg = msg
        output = ""
        key = key

        # sanitize the input
        if not isinstance(msg, str) or not msg.isalpha():
            raise ValueError("Input Error: Encrypted message must be a string containing only letters")
        if not isinstance(key, str) or not key.isalpha():
            raise ValueError("Input Error: Key must be a string containing only letters")

        for keys in key:
            keytonumber = ord(keys)
        for messages in msg:
            messagex = ord(messages) - keytonumber
            messagey = chr(messagex)
            output += messagey

        return output
