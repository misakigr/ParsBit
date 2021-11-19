import os
import re

dirA = 'blk/' # Directory where blk*.dat files are stored
#dirA = sys.argv[1]
dirB = 'res/' # Directory where to save parsing results
#dirA = sys.argv[2]

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.txt') and x.startswith('blk'))]
fList.sort()
#Источник: https://pythonim.ru/list/metod-sort-python)

for i in fList:
    nameSrc = i
    nameRes = nameSrc.replace('.txt','.dat')
    resList = []
    SortList = []

    a = 0
    t = dirA + nameSrc
    # resList.append('Start ' + t + ' in ' + str(datetime.datetime.now()))
    print ('Start ' + t)


    with open(t) as file:
        for line in file:
            line = str(line)
            s1 = re.sub("['|[]", "", line)
            s1 = s1[:64]
            SortList.append(s1)
            SortList = list(set(SortList))  # Удаляем дубликаты
            #print(SortList)
        for li in SortList:
            li = str(li)
            s1 = re.sub("['|[]", "", li)
            s1 = s1[:64]
            word = s1.replace('\n', '')  # Искомое слово без перевода строки
            #print (word)

            DATE_GROUP_SEPARATOR = "DateGroup"
            sorted_data = {}

            # with open(t) as file:
            last_group = None
            with open(dirA + nameRes) as file:
                for line in file:
                    line = line.replace('\n', '')
                    if DATE_GROUP_SEPARATOR in line:
                        sorted_data[line] = []
                        last_group = line
                    else:
                        sorted_data[last_group].append(line)
            with open('restest.txt', 'w') as filehandle:
                for date_group, dates in sorted_data.items():
                    if word in (str(dates)[400:]) and word in (str(dates)[:400]): # Если в файле встречается первый скрипт дважды
                        #print(dates)
                        # print(f"{date_group}: {dates}")
                        filehandle.writelines(place for place in (f"{date_group}: {dates}" + '\n'))

            with open('restest.txt') as file:
                for line in file:
                    if word in (line.partition('Input script')[2])[:120]:
                        text = str(line)
                        data = text.split(", ")
                        for temp in data:
                            if 'TX hash = ' in temp:
                                resList.append(temp)

    resList = list(set(resList)) #Удаляем дубликаты
    f = open(dirB + nameRes, 'w')
    for j in resList:
        s1 = re.sub("[:|']", "", j)
        s1 = s1.replace("[", "")
        s1 = s1.replace("]", "")
        s1 = s1.replace('"', "")
        f.write(s1[10:] + '\n')

    f.close()
    resList = []
    SortList = []

    file_name = dirB + nameRes
    file_stats = os.stat(file_name)
    #print(f'File Size in Bytes is {file_stats.st_size}')
    # if file_stats.st_size == 0: # Если файл пустой, то удаляем его
    #     os.remove(file_name)





