resList = []
word = '022100'
k = 0
i = 0
with open('trans.txt') as file:
    for line in file:
        #С начала
        text = str(line)
        if text.isprintable() == False:
            text = text[:(len(text)-1)]
        i += 1

        c = (text[:8])
        b = (text[8:])
        b_end = c
        resList.append(c)

        c = (b[:2])
        b = (b[2:])
        resList.append(c)

        c = (b[:64])
        b = (b[64:])
        resList.append(c)


        c = (b[:8])
        b = (b[8:])
        resList.append(c)

        if '0220' in line:
            resList.append(b.partition('0220')[0] + '0220')
            b = b.partition('0220')[2]


        else:
            resList.append(b.partition('022100')[0] + word)
            b = b.partition('022100')[2]


        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        if '022100' in b[:64]:
            resList.append('022100')
            b = b.partition('022100')[2]
        else:
            resList.append('0220')
            b = b.partition('0220')[2]

        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        b = (b[:-86])


        if 'ffffffffff' in b:
            k = (b.rfind('ffffffffff'))
        elif 'fffffffff' in b:
            k = (b.rfind('fffffffff'))
        elif 'ffffffff' in b:
            k = (b.rfind('ffffffff'))

        c = (b[:k])
        b = (b[k:])
        resList.append(c)

        c = (b[:8])
        b = (b[8:])
        resList.append(c)

        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        c = (b[:8])
        b = (b[8:])
        resList.append(c)

        if '0220' in b:
            resList.append(b.partition('0220')[0] + '0220')
            b = b.partition('0220')[2]

        else:
            resList.append(b.partition('022100')[0] + word)
            b = b.partition('022100')[2]

        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        if '0220' in b:
            resList.append(b.partition('0220')[0] + '0220')
            b = b.partition('0220')[2]

        else:
            resList.append(b.partition('022100')[0] + word)
            b = b.partition('022100')[2]

        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        resList.append(b)


        #С конца

        c = (text[-86:-78])
        resList.append(c)

        c = (text[-78:-76])
        resList.append(c)


        c = (text[-76:-60])
        resList.append(c)

        c = (text[-60:-58])
        resList.append(c)

        c = (text[-58:-8])
        resList.append(c)

        c = (text[-8:])
        resList.append(c)

        resList.append(b_end)

        file_name = 'raz_tranz/list-tranz_{}.txt'.format(i)
        f = open(file_name, 'w')
        for j in resList:
            f.write(j + '\n')
        f.close()
        resList = []