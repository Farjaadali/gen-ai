#variables
message = "Hello, World!"
firstName = "Farjaad"
lastName = "Mazhar"
my_age = 27

# printing Hello, World!
print(message)

#printing First Name
print(firstName)

#printing Full Name
print(f"{firstName} {lastName}")

#printing numbers
print(1, 2, 3)

#using special characters
print("Hello,\nWorld!")
print("Hello,\tWorld!")

#using print sep parameter
print("apple", "banana", "cherry", sep=', ')
print(1,2,3, sep='-')

#using print end parameter
print("Welcome to", end = ' ')
print("Python")

#printing number on separate lines
print(1, end = '')
print(2)

#using escape character
print("He Said \"Hello\"")
#OR
print('He Said "Hello!"')
print("This is a backslash: \\")

#printing string and number together
print(f"My age is : {my_age}")
print(f"The number is : {5}")

#using loop to print numbers upto 5
i = 1
while i <= 5:
    print(i)
    i += 1