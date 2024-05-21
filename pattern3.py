#print(ord("a"))
col=97
while col<=101:
    row = 97
    while row <= col:
        print(chr(row),end=" ")
        row+=1
    col+=1
    print()
