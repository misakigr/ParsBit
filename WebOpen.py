import os

from selenium import webdriver

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


                browser.find_element_by_xpath('//*[@id="tx-info"]/div/i').click()
                result = browser.find_element_by_xpath('//*[@id="raw-tx"]').text

                file = open('trans.txt', 'a')
                file.write(result + '\n')
                file.close()

            finally:
                # browser.close()
                pass

    browser.close()
