#Single line comments with #
'''I am multiline comments
I have not yet finished'''

print("hello Python") # single comments

x=5
y= "Saba"

print(x)
print(y)

x=5
x="Sana"

print(x)

# int, float, string 

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)

x = 5
y = "John"
print(type(x))
print(type(y))

x="Saba"
y='Sana'

print(x)
print(y)

x= "My father's name is John"
print(x)

a=5
A=5
print(a)
print(A)

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

#Multi Words Variable Names

'''
Camel Case
Each word, except the first, starts with a capital letter
myVariableName 

Pascal Case
MyVariableName 

Snake Case
my_variable_name = "John"
'''
#Many Values to Multiple Variables
x,y,z="Nazrul","Nargis", "saba"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "Python"
y = "is"
z = "awesome"
print(x+y+z)


x = "Python"
y = "is"
z = "awesome"
print(x+ ' '+ ' '+ y+' '+z)

x = 5
y = 10
print(x + y)

x = 5
y = "w"
print(x , y)

print('Hello','World')

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

y="Good"
def myFirstFunc():
    print("Python is " + y)
    
myFirstFunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
    
#If you use the global keyword, the variable belongs to the global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = 'awesome'
def myfunc():
  global x 
  x= 'fantastic'
myfunc()
print('Python is ' + x)

x = ("apple", "banana", "cherry")
print(type(x))

#Addition, substraction, Multiply, Divide

a=4
b=5

add=a+b
sub=b-a
prd= a*b
divd = a/b

print("The addition is : ", add)
print(sub)
print(prd)
print(divd)

a= int(input("Enter the value of a : "))
b= int(input("Enter the value of b : "))

add=a+b
sub=b-a
prd= a*b
divd = a/b

print("The addition is : ", add)
print(sub)
print(prd)
print(divd)