amount = 3000
if amount%100==0:
    print(amount)
    if amount>=500:
        notes = amount//500
        print("500 Rs Notes are",notes)
        amount = amount%500
    if amount>=200:
        notes = amount//200
        print("200 Rs Notes are",notes)
    if amount>=100:
        amount = amount%200
        notes = amount//100
        print("100 Rs Notes are",notes)
else:
    print("Amount Should be Multiple of 100")
