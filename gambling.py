import random
for x in range (1):
    x=random.randint(1,101)

point=int(0)

savings = int(input("Enter your total amount of money you have in your wallet"))

betmoney = int(input("Enter the money you are betting"))

num = int(input("Enter a number between 1 and 100"))

bef = (savings - betmoney)

if num == x:
    print ("You did it! Your earnings just got multiplied by 6")
    point = point + 6

    import random
    for x in range (1):
        x=random.randint(1,101)

    if num % 2 == 0:
        print("Even Steven buddy! you get double your money back")
        point = point + 2
    else:
        point = point + 0

    for i in range(2,num):
        if (num % i) == 0:
            point = point +0
            break
    else:
        point = point + 0
else:
    print("Sucks to suck! Dont bet anymore. Find Jesus.")


win = (point * betmoney)
aft = (bef + win)
print ("Your wallet after playing is now" , aft)
print ("You have won" , win)

print ("btw the mystery number was" , x)