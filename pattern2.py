#print(ord('a')) ASCII value
#print(chr(97)) character
row=97
while row<=101:
    col=97
    while col<=row:
        print(chr(row), end=" ")
        col += 1
    row += 1
    print()
