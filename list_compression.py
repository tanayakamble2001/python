even=[x for x in range(2,101,2)]
odd=[i for i in range(1,101,2)]
'''for i in range(1,101,1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
'''
print(even)
print(odd)

a=['robert','anuj','abc']
capital=[i.upper() for i in a]
print(capital)

print([i for i in a if 'b' in i])




