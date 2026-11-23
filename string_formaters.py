# strings are basically text values - in Python, strings are immutable

import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year

print("Hey", name, "your current age is -", age)


# string formaters

# option 1: .format()
# print("Hey {0} how are you doing ?".format(name))
# print("Hey {a} how are you doing ?".format(a=name))

print("Hey {0} your current age is - {1}".format(name, age))
print("Hey {n} your current age is - {a}".format(n=name, a=current_year - birth_year))


# option 2: short hand notation
print(f"Hey {name} your current age is - {current_year - birth_year}")

