#-----Comparison Operators-----
#--Task--
a = 11
b = 5
result =  a < b
type_result = type(result)
print(f"Result = {result} and its data type is {type_result}")
print(f"Result = {a < b} and its data type is {type(a < b)}") #Alternate version
print(f"Result = {a > b} and its data type is {type(a > b)}")
print(f"Result = {a <= b} and its data type is {type(a <= b)}")
print(f"Result = {a >= b} and its data type is {type(a >= b)}")
print(f"Result = {a == b} and its data type is {type(a == b)}")
print(f"Result = {a != b} and its data type is {type(a != b)}") 

print("-"*50)

#-----Overwriting Variables-----
#--Task--
x = 5
x = 12
print(x)

a = "Hello"
a = "Bye"
print(a)

m = "String"
m = 15
print(m)

print("-"*50)

#-----String Exercise-----
#--Worked Example--
unit_name = "Level 4 Programming"
print("This unit is: ", unit_name)
print("The 1st character is: ", unit_name[0])
print("The 4th character is: ", unit_name[3])
print("The 8th character is: ", unit_name[7], "\n")

#--Task--
greeting_string = "Welcome to Programming unit! This is level 4 unit :)"
print(greeting_string)
print("The 1st character is: ", greeting_string[0])
print("The 5th character is: ", greeting_string[4])
print("The first five characters are: ", greeting_string[:5])
print("The last character is: ", greeting_string[-1:])
print("The last four characters are: ", greeting_string[-4:])
#greeting_string[0] = "X" Raises error as string is immutable

print("-"*50)

#-----Types of Variables-----
#--Task--
a = 11
print(type(a)) #int
a = 11.0
print(type(a)) #float
a = "11"
print(type(a)) #string
a = "11" + "11"
print(type(a)) #string
a = "a"
print(type(a)) #string
a = True
print(type(a)) #boolean
a = "False"
print(type(a)) #string

#-----Type Conversion-----
x = 10.5
print(type(x)) #float

#--Task--
x = int(x)
print(x)
print(type(x)) #int

#--Task--
x = "String"
y = 15
z = 6.8

print("The data type of x = ", type(x))
print("The data type of y = ", type(y))
print("The data type of z = ", type(z))

print(f"The result of y + z is {y + z}, its data type is {type((y + z))}")
print(f"The result of y + int(z) is {y + int(z)}, its data type is {type(y + int(z))}")
print(f"The result of z + float(y) is {z + float(y)}, its data type is {type(z + float(y))}")

print("The data type of str(z) = ", type(str(z)))

print(f"The result of x + str(y) + str(z) is {x + str(y) + str(z)}, its data type is {type(x + str(y) + str(z))}")

#print(x + y) You cannot add x to y as y is not a string and therefore cannot concatenate
print(x + str(y)) #This would concatenate

#-----Illegal Variable Assignment-----
#--Task--
my_var = 1 #Only this identifier would work without error

