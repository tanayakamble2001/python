col=97
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

