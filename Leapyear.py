# this is the solution to the leap year problem
year = int(input("Which year do you want to check? \n"))

if year % 4 == 0 or year & 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
else:
    print("Not a leap year")
#this is Dr.Yu solution to the leap year exercise

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("if Leap year.")
    else:
        print("Leap Year.")
else:
    print("Not a leap year.")