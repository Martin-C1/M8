#Martin C
#November 14

import M8_resources
#Problem 1
def equal():
    A = input("enter text: ")
    B = input("enter text: ")
    if A == B:
        print("A is equal to B")
    else:
        print("A and B are not equal")
equal()

#Problem 2
def check_sum():
    Num1 = int(input("enter a number: "))
    Num2 = int(input("enter a second number: "))
    sum = Num1 + Num2
    if sum == 10:
        print("The sum is equal to 10")
    elif sum < 10:
        print("The sum is less than 10")
    else:
        print("The sum is greater than 10")
check_sum()

#problem 3
def check_list(lst):
    if 5 in lst:
        print("5 is in the list")
    else:
        print("5 is not in the list")
check_list([1, 2, 5, 7, 9, 11])

#problem 4
def check_leap(year):
    if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
        print("True, year is a leap year")
    else:
        print("False, year is not a leap year")
check_leap(2020) #2020 was a leap year so this will print true.
check_leap(2019) #2019 was not a leap year so this will print false.

#problem 5- For problem 5, see M8_resources.py

#problem 6
def inspect_items(number):
    print(f"My weapons are {M8_resources.Martin.weapons}")
    if number == 1:
        #for every item I need, I want to see if it is in weapons
        for item in ['rope','coat', 'first aid kit']:
            if item not in M8_resources.Martin.weapons:
                print(f"you don't have {item}")
                return False
        print("you have everything you need, good luck")
        print(['rope','coat', 'first aid kit'])
    elif number == 2:
        for item in ['pan','groceries']:
            if item not in M8_resources.Martin.weapons:
                print(f"you don't have {item}")
                return False
        print("you have everything you need, good luck")
        print(['pan', 'groceries'])
    elif number == 3:
        for item in ['pen','paper', 'idea']:
            if item not in M8_resources.Martin.weapons:
                print(f"you don't have {item}")
                return False
        print("you have everything you need, good luck")
        print(['pen', 'paper', 'idea'])

inspect_items(1)
