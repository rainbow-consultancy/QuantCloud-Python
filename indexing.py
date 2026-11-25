# string indexing (index starts from 0 and goes till n number)

course_name = "Python" # P-0, y-1, t-2, h-3, o-4, n-5

# Syntax
# [start:end-1:step=1]

print(course_name[0])
print(course_name[5])

print(course_name[0:2])
print(course_name[0:3])

print(course_name[0:5])
print(course_name[0:5:2])

print(course_name[:])
print(course_name[::2])
print(course_name[::1])
print(course_name[::])

print(course_name[3:5])
print(course_name[3:6])


course_name = "Python" # P-0, y-1, t-2, h-3, o-4, n-5
# n -1, o -2, h -3, t -4, y -5, p -6

print(course_name[-1])
print(course_name[-1:-4:-1])
# print(course_name[-1:-4])

print(course_name[-1:-7:-1])
print(course_name[::-1])
