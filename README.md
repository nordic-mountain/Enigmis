# Enigmis
Enigmis is cipher program that Encrypts and Decrypts different ciphers.
The cipher currently includes the following encryption programs:
* Caesar Cipher
* Vigenère Cipher
* One time pad Cipher

## Requirements
* Python 3.x
* random and string modules

## How-To-Use
Here are the steps:

1. Download the repository
2. Download the modules
3. Import Enigmis to a Python file
4. Use the Functions

## Functions
After you downloaded the repository and imported it, use can use the functions.
There are three ciphers in the program. If you want to encrypt a keyword with one of the ciphers do this:

------------------------------------------------------------------------------------------------------------

### Caesar Cipher
If you want to encrypt with a Caesar Cipher you can use this function:

`Caesar.Encrypt(msg="BluePoo", shift=2)`

The `msg` pram is your string message and the `shift` is how much we would shift each letter in the message.


To decrypt type this:

`Caesar.Decrypt(msg="DnwgRqq", shift=2)`

------------------------------------------------------------------------------------------------------------

### Vigenère Cipher
To encrypt with a Vigenère Cipher you can use this function:

`Vigen.Encrypt(msg="GooLookLikePoo", key="BluePoo")`

The `msg` pram is your string message and the `key` is the key in the cipher.


To decrypt type this:

`Vigen.Decrypt(msg="¶ÞÞ»ÞÞÚ»ØÚÔ¿ÞÞ", key="BluePoo")`

------------------------------------------------------------------------------------------------------------

### One Time Pad Cipher
To encrypt with a One Time Pad Cipher you can use this function:

`OTpad.Encrypt(msg="GooLookLikePoo", Kylngth=30, shwky=True)`

The `msg` pram is your string message and the `Kylngth` is the length of the key in the cipher, and lastly `shwky` will show the key.


To decrypt type this:

`OTpad.Decrypt(msg=(The msg), key="qwdftnvdktndjtmdxopqsarebcvhd")`

------------------------------------------------------------------------------------------------------------
## Creators

* TheTechyKid
