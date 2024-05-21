row=101
while row>=97:
    col=97
    while col<=row:
        print(chr(row),end=" ")
        col+=1
    row-=1
    print()
