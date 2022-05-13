import re

#<span id="raw-tx">

t = '<span id="raw-tx">02000000027cdc217f7e1dc3c4623b71b84bdd12963ff5a6be787e8b0b4234edd5721709305c0000006b483045022100c074c4312521ed560d73ac25d2>span'
match = re.search(r'(?:\w+\d+\w+)+', t)
print(match[0] if match else 'Not found')