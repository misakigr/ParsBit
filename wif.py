# From private key(hex) to Wallet Import Format(WIF)
# Reference: https://medium.freecodecamp.org/how-to-create-a-bitcoin-wallet-address-from-a-private-key-eca3ddd9c05f
#            https://docs.python.org/2/library/hashlib.html
import codecs  #If not installed: "pip3 install codecs"
import hashlib
# отсюда взять полученный результат https://sagecell.sagemath.org/
bits_hex = hex(61383798063007952593650999102428655071380504251029294557659553501352212980146)

# 0x66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
private_key = bits_hex[2:]
# print(private_key)
# PK0 is  private key.
PK0 = private_key
PK1 = '80'+ PK0
PK2 = hashlib.sha256(codecs.decode(PK1, 'hex'))
PK3 = hashlib.sha256(PK2.digest())
checksum = codecs.encode(PK3.digest(), 'hex')[0:8]
PK4 = PK1 + str(checksum)[2:10]  #I know it looks wierd

# Define base58
def base58(address_hex):
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_string = ''
    # Get the number of leading zeros
    leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
    # Convert hex to decimal
    address_int = int(address_hex, 16)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add ‘1’ for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = '1' + b58_string
    return b58_string

WIF = base58(PK4)
# print(WIF)

from bitcoinaddress import Wallet

wallet = Wallet(WIF)
print(wallet)