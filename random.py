import random
r=['swara','rahi','astha','anvi','shwet','aryan','shruti','pravara','vihan']
print(random.choice(r))
print(random.choices(r,k=3))
print(random.sample(r,k=2))
random.shuffle(r)
print(r)

print(random.randint(1,10))

#otp
print("".join(random.sample('1234567890',k=4))) #convert list into string
#print(random.sample('1234567890',k=4))

