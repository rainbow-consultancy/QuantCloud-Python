# python lists - mutable datatype | ordered datatype

values = [1, 2, 2, 2, "Lokesh", True, 45.60, [1, 2, 3, 4], (0, 2, 4)]
values.append(100)
print(values)

values.remove("Lokesh")
print(values)

values.pop()
print(values)

print(values.count(2))

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

num1.extend(num2)
print(num1)

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

num1.append(num2)
print(num1)

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

num1.reverse()
print(num1)

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

num1.insert(0, 10000)
print(num1)

num1 = [1, 2, 3, 4, 5]
num1[0] = 20000
print(num1)

print(num1[0:3])
