import random
words = ['robert','berort','mishraji','mijirash','rajit','arjit','krushna','rushank','tanaya','yatana','shradha','dhashra','namita','manita','netra','terna','ashish','shisha','abhishek','shakebhi','vishal','shalvi']
score = 0
while True:
    for wr in range(3):
        lett= list(random.choice(words))
        print("Guess Correct Word By given Word :=> ","".join(lett))
        user = input("Enter Correct word or '(quit)' :")
        
        
        if user!= "".join(lett):
            valid=True
            for letter in user:
                if letter in lett:
                    lett.remove(letter)
                else:
                    valid=False
                    break
            if valid and user in words:
                score = score+ len(user)
                print(f"Correct and Your Score is {score}")
            else:
                print("Wrong Word Enter By You")
            if user != "".join(lett):
                break
        else:
            print("You Enter Same Word Which We Provided")
    
    else:
        score= score - len(user)
        print(f"We Have Reducted Your {len(user)} Score Because You Enter Same Word 3 Times,Your Total Score is {score} ")
    if user == 'quit':
            break
print("Thnak You For Playing.....")

