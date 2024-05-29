a=[[['robert','mishraji','Anuj','Rajith','Jadhav']]]
#Using for loop
print("Using for Loop")
for i in a[0][0]:
    print(i)
#Using while loop
print()
print("Using While Loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        k=0
        while k<len(a[i][j]):
            print(a[i][j][k])
            k+=1
        j+=1
    i+=1



#print numbers
b=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Using for loop
print()
print("Using for Loop")
for i in b:
    for j in i:
        print(j)

#Using while loop
print()
print("Using While Loop")
i=0
while i<len(b):
    j=0
    while j<len(b[i]):
        print(b[i][j])
        j+=1
    i+=1
