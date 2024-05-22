row=97
while row<=101:
    col=101
    while col>=97:
        if col<=row:
            print(chr(row), end=" ")
        else:
            print(" ", end=" ")
        col -= 1
    row += 1
    print()




'''col=97
while col<=101:
    row=101
    while row>=97:
        if row<=col:
            print(chr(col), end=" ")
        else:
            print(" ", end=" ")
        row -= 1
    col += 1
    print()
'''
