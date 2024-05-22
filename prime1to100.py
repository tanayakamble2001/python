for i in range(1,101,1):
    for j in range(2,101,1):
        if i%j == 0:
            break;
    if i == j:
        print(i)
        
