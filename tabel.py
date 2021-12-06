# Берем файлы результата выполнения Razbor
import os
import re
dirA = 'raz_tranz/'  # Directory where blk*.dat files are stored
# dirA = sys.argv[1]
dirB = 'wal_adr/'  # Directory where to save parsing results
# dirA = sys.argv[2]

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.txt') and x.startswith('list'))]
fList.sort()
# Источник: https://pythonim.ru/list/metod-sort-python)
j = 0
for j in fList:
    try:

        nameSrc = j
        nameRes = nameSrc.replace('.txt', '.dat')
        resList = []
        SortList = []

        a = 0
        t = dirA + nameSrc
        # resList.append('Start ' + t + ' in ' + str(datetime.datetime.now()))
        print('Start ' + t)

        i = 1
        with open(t) as file:
            while i <= 24:
                exec("x{} = {}".format(i, 'str(file.readline())'))
                i += 1
        x0 = '00'
        x00 = ''
        #print ('x16 равно:' + x16)

        res1 = x1 + x2 + x3 + x4 + x21 + x22 + x10 + x11 + x12 + x0 + x00 + x18 + x19 + x20 + x21 + x22 + x23 + x24
        # re.sub("^\s+|\n|\r|\s+$", '', res)
        res1 = res1.replace("\r", "")
        res1 = res1.replace("\n", "")
        # print(res1)
        # print()

        from binascii import unhexlify
        from hashlib import sha256

        # header = input("Введите длинное число:")
        res1 = unhexlify(res1)
        res1 = sha256(sha256(res1).digest()).hexdigest()
        # print(res1)
        #
        # print()

        res = x1 + x2 + x3 + x4 + x0 + x00 + x10 + x11 + x12 + x21 + x22 + x18 + x19 + x20 + x21 + x22 + x23 + x24
        res = res.replace("\r", "")
        res = res.replace("\n", "")
        # print(res)
        # print()

        res = unhexlify(res)
        res = sha256(sha256(res).digest()).hexdigest()
        # print(res)
        #print()
        c = ""
        c1 = 'p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141'
        #print('p  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141')
        c = c + c1 + '\n'
        c2 = 'r  = 0x' + x6
       #print('r  = 0x' + x6)
        c = c + c2
        c3 = 's1 = 0x' + x8
        #print('s1 = 0x' + x8)
        c = c + c3
        c4 = 's2 = 0x' + x16
        #print('s2 = 0x' + x16)
        c = c + c4
        c5 = 'z1 = 0x' + res1 + '\n'
       #print('z1 = 0x' + res1)
        c = c + c5
        c6 = 'z2 = 0x' + res
        #print('z2 = 0x' + res)
        c = c + c6 + '\n'
        c7 = 'K = GF(p)'
        #print('K = GF(p)')
        c = c + c7 + '\n'
        c8 = 'K((z1*s2 - z2*s1)/(r*(s1-s2)))'
        #print('K((z1*s2 - z2*s1)/(r*(s1-s2)))')
        c = c + c8

        # Запуск браузера выполнение вычислений и возврат результата с сайта https://sagecell.sagemath.org/
        from selenium import webdriver
        import time
        import sys
        browser = webdriver.Edge()


                #browser.set_window_position(0, 0)
        browser.get("https://sagecell.sagemath.org/")
        phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c2 + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c3 + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c4 + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c5 + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c6 + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c7 + '\n')
        # phn = browser.find_element_by_xpath('//*[@id="cell"]/div[1]/div[1]/div/div[1]/textarea').send_keys(c8)

        #time.sleep(2)
        browser.find_element_by_xpath('//*[@id="cell"]/div[1]/button').click()
        time.sleep(5)
        result = browser.find_element_by_xpath('// *[ @ id = "cell"] / div[3] / div[1] / div / div[2]').text
        # print('Всего цифр в данном числе:', len(result))
        # print('Оно выглядит так:', result)



        # finally:
        browser.close()

        # header = input("Введите длинное число:")
        header = result

        import codecs  # If not installed: "pip3 install codecs"
        import hashlib

        # отсюда взять полученный результат https://sagecell.sagemath.org/
        bits_hex = hex(int(header))

        # 0x66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
        private_key = bits_hex[2:]
        # print(private_key)
        # PK0 is  private key.
        PK0 = private_key
        PK1 = '80' + PK0
        PK2 = hashlib.sha256(codecs.decode(PK1, 'hex'))
        PK3 = hashlib.sha256(PK2.digest())
        checksum = codecs.encode(PK3.digest(), 'hex')[0:8]
        PK4 = PK1 + str(checksum)[2:10]  # I know it looks wierd


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
        #print(wallet)

        file = open(dirB + nameRes, 'w')
        file.write(str(wallet))
        file.close()
    except Exception:
        print("Поймана ошибка значения", sys.exc_info()[0])

        # continue
