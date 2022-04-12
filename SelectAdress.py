import os


dirA = 'wal_adr/' # Directory where blk*.dat files are stored
#dirA = sys.argv[1]
dirB = 'SelectAdress/' # Directory where to save parsing results
#dirA = sys.argv[2]

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.dat') and x.startswith('list'))]
fList.sort(reverse=True)
#Источник: https://pythonim.ru/list/metod-sort-python)

word = 'Public Address 1: '  # Искомое слово
dorw = 'Public Address 1 compressed: '  # Искомое слово 2
resList = []

for i in fList:
    nameSrc = i
    nameRes = nameSrc.replace('.dat','.txt')
    # resList = []
    a = 0
    t = dirA + nameSrc
    # resList.append('Start ' + t + ' in ' + str(datetime.datetime.now()))
    print ('Start ' + t )
    f = open(t)
    for line in f:
        if word in line:
            text = str(line)
            resList.append(text.partition(word)[2])
            # print(kb)
        if dorw in line:
            text = str(line)
            resList.append(text.partition(dorw)[2])

f = open('Lists.txt', 'a')
for j in resList:
    f.write(j)
f.close()
resList = []

    # Удаление дубликатов строк
file ='Lists.txt'
uniqlines = set(open(file,'r', encoding='utf-8').readlines())
gotovo = open(file,'w', encoding='utf-8').writelines(set(uniqlines))