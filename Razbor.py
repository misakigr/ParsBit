resList = []
word = '022100'
k = 0
i = 0
with open('trans.txt') as file:
    for line in file:
        # С начала
        text = str(line)
        if text.isprintable() == False:
            text = text[:(len(text) - 1)]
        i += 1

        c = (text[:8])  # 1
        b = (text[8:])
        b_end = c
        resList.append(c)

        c = (b[:2])  # 2
        b = (b[2:])
        resList.append(c)

        c = (b[:64])  # 3
        b = (b[64:])
        resList.append(c)

        c = (b[:8])  # 4
        b = (b[8:])
        resList.append(c)

        # 5
        if '0220' in b[:20]:
            resList.append(b.partition('0220')[0] + '0220')
            b = b.partition('0220')[2]

        else:
            resList.append(b.partition('022100')[0] + word)
            b = b.partition('022100')[2]

        # 6
        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        # 7
        if '022100' in b[:20]:
            resList.append('022100')
            b = b.partition('022100')[2]
        else:
            resList.append('0220')
            b = b.partition('0220')[2]

        # 8
        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        b = (b[:-86])

        # 9
        if 'ffffffffff' in b:
            k = (b.rfind('ffffffffff'))
        elif 'fffffffff' in b:
            k = (b.rfind('fffffffff'))
        elif 'ffffffff' in b:
            k = (b.rfind('ffffffff'))
        c = (b[:k])
        b = (b[k:])
        resList.append(c)

        # 10
        c = (b[:8])
        b = (b[8:])
        resList.append(c)

        # 11
        if '01000000' in b[:80]:
                c = (b.partition('01000000')[0])
                clen = len(str(c))
                b = (b[clen:])
        elif '00000000' in b[:80]:
                c = (b.partition('00000000')[0])
                clen = len(str(c))
                b = (b[clen:])
        else:
            if '00000001' in b[:80]:
                c = (b.partition('00000001')[0])
                clen = len(str(c))
                b = (b[clen:])
        # c = (b.partition('01000000')[0])
        # b = (b.partition('01000000' + '01000000')[2])
        resList.append(c)

        #12
        c = (b[:8])
        b = (b[8:])
        resList.append(c)

        # 13
        if '0220' in b[:20]:
            resList.append(b.partition('0220')[0] + '0220')
            b = b.partition('0220')[2]

        else:
            resList.append(b.partition('022100')[0] + word)
            b = b.partition('022100')[2]

        # 14
        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        # 15
        if '0220' in b[:20]:
            resList.append(b.partition('0220')[0] + '0220')
            b = b.partition('0220')[2]

        else:
            resList.append(b.partition('022100')[0] + word)
            b = b.partition('022100')[2]

        c = (b[:64])
        b = (b[64:])
        resList.append(c)

        resList.append(b)

        # С конца

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

        file_name = 'raz_tranz/list00{}.txt'.format(i)
        f = open(file_name, 'w')
        for j in resList:
            f.write(j + '\n')
        f.close()
        resList = []
