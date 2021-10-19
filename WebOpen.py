from selenium import webdriver
import time
import os
import re

c = ''

dirA = 'res/'  # Directory where blk*.dat files are stored
# dirA = sys.argv[1]
dirB = 'res/'  # Directory where to save parsing results
# dirA = sys.argv[2]

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.dat') and x.startswith('blk'))]
fList.sort()
# Источник: https://pythonim.ru/list/metod-sort-python)

for i in fList:
    nameSrc = i
    nameRes = nameSrc.replace('.dat', '.txt')
    resList = []
    SortList = []

    a = 0
    t = dirA + nameSrc
    # resList.append('Start ' + t + ' in ' + str(datetime.datetime.now()))
    print('Start ' + t)

    with open(t) as file:
        for line in file:
            c = str(line)
            #print(c)

            # c = '53**53'
            browser = webdriver.Edge()

            try:
                browser.set_window_size(250, 250)
                browser.set_window_position(900, 900)
                browser.get("https://btc.bitaps.com/raw/transaction/%s?format=json" % c)

                # browser.find_element_by_xpath('//*[@id="search-box"]"]').send_keys(c)
                # time.sleep(1)
                browser.find_element_by_xpath('//*[@id="tx-info"]/div/i').click()
                result = browser.find_element_by_xpath('//*[@id="raw-tx"]').text
                # print('Транзакция:', result)
                # resList.append(result)

                file = open('trans.txt', 'a')
                file.write(result + '\n')
                file.close()
                # time.sleep(2)
                # browser.find_element_by_xpath('//*[@id="tx-hash"]/table/tbody/tr[6]/td[2]/a/text()').click()
                # time.sleep(15)
                # result = browser.find_element_by_xpath('// *[ @ id = "cell"] / div[3] / div[1] / div / div[2]').text
                # print('Всего цифр в данном числе:', len(result))
                # print('Оно выглядит так:', result)

            finally:
                # browser.close()
                pass

        # f = open('trans.txt', 'a')
        # for j in resList:
        #     f.write(j + '\n')
        # f.close()

browser.close()
