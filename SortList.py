import os

dirA = 'C:/2/' # Directory where blk*.dat files are stored
dirB = 'C:/1/' # Directory where to save parsing results

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.txt') and x.startswith('blk'))]
fList.sort()

for i in fList:
    nameSrc = i
    nameRes = nameSrc.replace('.txt','.dat')
    # resList = []
    a = 0
    t = dirA + nameSrc
    # resList.append('Start ' + t + ' in ' + str(datetime.datetime.now()))
    print ('Обработка файла ' + t )
    n = 0
    with open(t, 'r+') as f:
        f.writelines( ["\n"]+[f.readlines(),f.seek(0)][0] )
    with open(t, "r") as f, open("restest.txt", "w") as outfile:
        for i in f.readlines():
    
            if not i.strip():
                outfile.write('DateGroup' + str(n) + '\n')
                n += 1
                continue
            if i:
                outfile.write(i)
    
    
    DATE_GROUP_SEPARATOR = "DateGroup"
    sorted_data = {}
    
    with open('restest.txt') as file:
        last_group = None
        for line in file.readlines():
            line = line.replace('\n', '')
            if DATE_GROUP_SEPARATOR in line:
                sorted_data[line] = []
                last_group = line
            else:
                sorted_data[last_group].append(line)
    with open('restest.txt', 'w') as filehandle:
        for date_group, dates in sorted_data.items():
            # print(f"{date_group}: {dates}")
            filehandle.writelines(place for place in (f"{date_group}: {dates}" + '\n'))
    
    
    word = 'Inputs count = 02'  # Искомое слово
    dorw = 'Outputs count = 1'  # Искомое слово 2
    resList = []
    with open('restest.txt') as file:
        for line in file:
            if word in line and dorw in line:
                text = str(line)
                data = text.split(", ")
                for temp in data:
                    resList.append(temp)
    
    f = open(dirA+nameSrc, 'w')
    for j in resList:
        f.write(j + '\n')
    f.close()
    resList = []
    os.replace(dirA + nameSrc, dirB + nameSrc)
    
    word = 'Input script'  # Искомое слово
    with open(dirB+nameSrc) as file:
        for line in file:
            if word in line:
                text = str(line)
                b = text.partition('022')[2]
                b = b.partition('022')[0]
                if len(b) < 80 and len(b) > 60:
                    resList.append(b[-64:]+'\n')
    
        
        f = open('restest.txt', 'w')
        for j in resList:
            f.write(j + '\n')
        f.close()
    
        # убираем пустые строки и записываем в выходной файл
        with open("restest.txt", "r") as f, open("outfile.txt", "w") as outfile:
            for i in f.readlines():
                if not i.strip():
                    continue
                if i:
                    outfile.write(i)
        os.remove('restest.txt')
        
        
    
    
        from collections import defaultdict
        res = defaultdict(list)
        with open('outfile.txt') as infile:
            for line in infile:  # Iterate each line
                val = line.strip().split()  # Get first word
                #print (str(val)[2:66])
                res[val[0]].append(line)
            for k, v in res.items():
                if len(v) > 1:
                    a=1
                    file = open(dirB+nameRes, 'a')
                    text = str(v)
                    data = text.split(", ")
                    for temp in data:
                        file.write(temp + '\n')
                    file.close()
            res = []
    if a==0:
        os.remove(dirB+nameSrc)
    a=0
                
        
        
        
