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