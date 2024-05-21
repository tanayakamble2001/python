print("Welcome to our Restaurant")
types=input("Which type of Food looking for veg/non-veg:")
'''veg=types
non_veg=types'''
if types=='veg':
    print("1.Paneer Tikka")
    print("2.Paneer Burji")
    print("3.Paneer Masala")
    food= input("Which dish would you like to order:")
    if food=='paneer-tikka':
        print("\n Paneer Tikka \n Price: 300 \n Butter Roti :4")
    elif food=='paneer-burji':
        print("\n Paneer Burji \n Price: 150 \n Butter Roti: 2")
    elif food=='paneer-masala':
        print("\n Paneer Masala \n Price: 200 \n Butter Roti: 4")
    else:
        print("\n Please Order")
elif types=='non_veg':
    print("\n 1. Chicken Tikka \n 2. Chicken 65 \n 3. Chicken Tandoor")
    food= input("Which dish would you like to order:")
    if food=='chicken-tikka':
        print("\n Chicken Tikka \n Price: 350 \n Butter Roti :4")
    elif food=='chicken-65':
        print("\n Chicken 65 \n Price: 200 \n Butter Roti: 4")
    elif food=='chicken-tandoor':
        print("\n Chicken Tandoor \n Price: 300 \n Butter Roti: 4")
    else:
        print("\n Please Order")
