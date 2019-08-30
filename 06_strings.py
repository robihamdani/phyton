# string literals
# print('Hello')
# print("Hello")

# assign to new variable
# a = "hello"
# print(a)

# multiline setting
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# strings array
# a = "Hello, World!"
# print(a[1])


# slicing
# b = "Hello, World!"
# print(b[2:5])

# negative indexing
# b = "Hello, World!"
# print(b[-5:-2])

# string length
# a = "Hello, World!"
# print(len(a))

# string method
# a = " Hello, World! "
# print(a.strip())

# a = "HELLO WORLD!"
# print(a.lower())

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(","))


# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" in txt
# print(x)

# string contatination
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# string format
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
