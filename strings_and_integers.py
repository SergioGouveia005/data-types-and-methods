#-----Strings and Integers-----
#--Task--
name = "Sergio"
age = 18
hobby = "Badminton"
number_of_units = 5

print("My name is {}, I am {} years old.\n".format(name, age) +
      "My hobby is {}.\nThis year I am enrolled in {} units".format(hobby, number_of_units))

print("-"*50)

#-----Strings Methods-----
#--Task--
my_text = "I have an apple, you have an apple"
my_text = my_text.replace("apple", "orange")
print(my_text)

my_text = "      I have an apple, you have an apple.       "
my_text = my_text.strip(" ")
print(my_text)

my_text = "Python Java C++"
my_text = my_text.split(' ')
for word in my_text:
    print(word)

my_text = "Bananas are great source of Potassium"
print("The letter a appears", my_text.count("a"), "times")

print("-"*50)

#-----Advanced Exercises-----
#--Task--
number = int(input("Enter an integer: "))
for i in range(1, number + 1):
    print(" "*(number - i) + (str(i)*i))

#--Task--
number = int(input("Enter an integer: "))
if number < 0:
    number *= -1
print(f"The first digit of {number} is {(str(number))[0]}")

#--Task--
import random as rand

def fill_with_random_vals(list, no_of_values):
    list.clear()
    for i in range(no_of_values):
        list.append(rand.randint(1,100))
    return list

def selection_sort(list):
    difference = 0
    index = -1
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                if abs(list[i] - list[j]) > difference:
                    #print("--", list[i]) #This is the current item it's looking at
                    #print("--", list[j], "\n") #These are the items it is being compared to
                    difference = abs(list[i] - list[j])
                    index = j
        if difference > 0: #Check if a swap is required
            temp = list[i]
            list[i] = list[index]
            list[index] = temp
            difference = 0
            #print(list) #Displays the list after each swap
    return list

#list = [29, 72, 98, 13, 87, 66, 52, 51, 36]
list = []
list = fill_with_random_vals(list, 10)
print(list) #Before sort
list = selection_sort(list)
print(list) #After sort