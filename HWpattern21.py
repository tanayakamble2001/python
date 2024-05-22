row=1
while row<=4:
    col=1
    while col<=5:
        if (row==1 and col==1) or (row==1 and col==5) or (row==4 and col==1)or (row==4 and col==5):
            print("O",end=" ")
        elif (row==2 and col==1)or (row==2 and col==5)or (row==3 and col==1)or (row==3 and col==5):
            print("|",end=" ")
        elif (row==2 and col==2) or (row==2 and col==3) or (row==2 and col==4):
            print(" ",end=" ")
        elif (row==3 and col==2)or (row==3 and col==3) or (row==3 and col==4):
            print(" ",end=" ")
        else:
            print("-",end=" ")
        col+=1
    row+=1
    print()
            
