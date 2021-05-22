def removeChar(st, i):
    if not i in range(len(st)):
        return 'index out of range'
    elif st == '':
        return 'String is empty'
    else:
        return st[:i]+st[i+1:]
        """
        newSt = ''
        newSt += st[:i]
        newSt += st[i+1:]
        """
        """
        for x in range(len(st)):
            if x == i:
                continue
            newSt += st[x]
        """
        # return newSt

print(removeChar('hello world',5))
