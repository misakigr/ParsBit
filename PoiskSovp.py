dirA = 'D:\Игорь\Разное/'  # Directory where blk*.dat files are stored
# dirA = sys.argv[1]
dirB = 'D:\Игорь\Разное/'  # Directory where to save parsing results
# dirA = sys.argv[2]

fList = os.listdir(dirA)
fList = [x for x in fList if (x.endswith('.dat') and x.startswith('blk'))]
fList.sort(reverse=True)
# Источник: https://pythonim.ru/list/metod-sort-python)

for i in fList:
    nameSrc = i
    nameRes = nameSrc.replace('.dat', '.txt')
    resList = []
    a = 0
    t = dirA + nameSrc

DATE_GROUP_SEPARATOR = "DateGroup"
sorted_data = {}

# with open(t) as file:
last_group = None
with open(t) as file:
    for line in file:
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

    f = open(dirA + nameSrc, 'w')
    for j in resList:
        f.write(j + '\n')
    f.close()
    resList = []