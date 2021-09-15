# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 18:47:55 2021

@author: UserARAKS
"""

from binascii import unhexlify

from hashlib import sha256

header = input("Введите длинное число:")
header = unhexlify(header)

print("Копируй:",sha256(sha256(header).digest()).hexdigest())
