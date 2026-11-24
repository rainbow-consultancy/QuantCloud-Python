# string functions in Python

course_name = " PYTHONNN "

# Upper
print(course_name.upper())

# Lower
print(course_name.lower())

# len()
print(len(course_name))

# replace
print(course_name.replace("n", "*"))

# capitalize
print(course_name.capitalize())

# count
print(course_name.count("N"))

# endswith
print(course_name.endswith("N"))  # True

print(course_name.endswith("A"))  # False

# strip
print(course_name.strip())

# concat
first_name = "Ratan"
last_name = "Tata"

full_name = first_name + "_" + last_name
print(full_name)

full_name = f"{first_name}_{last_name}"
print(full_name)
