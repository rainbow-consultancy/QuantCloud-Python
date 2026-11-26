# conditional statements in python

# num = int(input("Enter a num: "))

# syntax
# if condition:
#     code
# else:
#     code

# if num%2 == 0:
#     print(f"{num} is a even number")
# else:
#     print(f"{num} is a odd number")


# logical conditions - valid number (num>100 and num should be even)

# if num > 100 and num%2 == 0:
#     print(f"{num} is a valid number")
# else:
#     print(f"{num} is not a valid number")
    
# logical conditions - fav number (num > 100 or num should be odd)

# if num > 100 or num%2 != 0:
#     print(f"{num} is a fav number")
# else:
#     print(f"{num} is not a fav number")
    
# logical conditions -  fav number (num should be odd)

# if not num%2 == 0:
#     print(f"{num} is a fav number")
# else:
#     print(f"{num} is not a fav number")

# if num > 20:
#     print("A")
# elif num > 5:
#     print("B")
# else:
#     print("C")


# nested conditional statements
# bonus eligibility - employee exp >= 5 and if his salary <= 50k

exp = int(input("Enter Experience: "))
salary = int(input("Enter Current Salary: "))


if exp >= 5:
    if salary <= 50_000:
        print("Eligible for bonus")
    else:
        print("Not Eligible")
else:
    print("Minimum exp required is 5 years")

    


    
