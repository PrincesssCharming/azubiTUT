'''i = 1
while True:
    if i%3 == 0:
        break
    print (i)

x = int(input("first number: "))
y = int(input("second number: "))
sum = x + y
print(x + y)

def add_numbers(num1, num2):
    sum_result = num1 + num2 
    return sum_result 
# Input from the user 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
# Call the function and display the result 
result = add_numbers(num1, num2) 
print(f"The sum of {num1} and {num2} is: {result}")'''

#variables
'''pi = 22/7
print(pi ,  "circle formulae")

x = 'awesome'

def myfunc():
    print("Python is " + x)

myfunc()'''

#lists and arrays
'''names = ['Chantal', 'Tullio']
print(len(names)) #get the number of items
names.insert(0, 'Seth') #insert before index
print(names)
names.append('Nalani') #add to end
print(names)
names.sort() #sorts alphabetically
print(names)'''

#tuples
'''colors = ("red", "green", "blue")
print(colors[1])
#n/b we can have tuples inside tuples

name = input("First name: ")
surname = input("Surname: ")
phone = input("Phone number: ")
age = input("Age: ")

employee = (name, surname, phone, age)

print(employee)

#len(tuple) - get the number of elements in a tuple
#tuple.count(x) - number of elements in the tuple with value x
#tuple.index(x) - index of the first element with value x, if x doesn't exist, an error will be shown

numbers = (1, 2, "trois", "four", "V", 6)
print(numbers[2:4]) #slicing
print(len(numbers))
print(numbers.count(1))
print(numbers.index("V"))'''

#dictionaries - used for student data, students and student IDs
'''person = {'name': 'John', 'age': 30, 'city': 'Nairobi'} #key:value 9tuple can be used  as a key, lists can't
person['profession'] = 'Doctor' #an easy way to add to the dictionary, the end of the list | modify content
print(person)
print(person['name'], person['age']) #print specific detail

german_colours = {'red': 'rot', 'green': 'grun', 'blue': 'blau', 'yellow': 'gelb'}
print(german_colours)

eng_color = input("Name another English colour: ")
germ_translation = input("Please enter the german translation of " + eng_color + ": ")

german_colours[eng_color] = germ_translation
print(german_colours)

user_input = input("Which colour do you want translated? ")
if user_input in german_colours:
    print("The German translation for ", user_input, "is ", german_colours[user_input])'''

#dictionaries and lists
'''mary = {}
mary['first'] = 'mary'
mary['last'] = 'jane'

john = {}
john['first'] = 'john'
john['last'] = 'doe'

people = []
people.append(mary)
people.append(john)
#you can add dictionaries in lists
people.append({
    'nationality': 'Kenyan', 'race': 'black'
})

print(people)'''

#Tuples

'''my_tuple = (1, 2, 3, "he", "they", "mangoes")

gender = "binary" "non-binary" #concatenated string

gender = "binary", "non-binary" #tuple

print(len(my_tuple)) #find out the length of the tuple

the_list = [1,2,3,4]
the_tuple = tuple(the_list) #changes the list to a tuple

if "she" in my_tuple: #finding an item in a tuple
    print(True)
else:
    print(False)'''

#how to update tuples - convert to list, change then convert back. 
'''p1 = ("blue", "24", "red")
p2 = list(p1)
p2[1]= "teal"
p1= tuple(p2)
print("green" in p1) #find an item in tuple
# print(p2)
# print(p1)

p3 = list(p1)
p3.append("maroon") #adds to list
p3.remove("green") #removes any specified item
p3.pop() #removes the last item on the list
p1= tuple(p3)
del p3
print(p1)

#looping through tuples
#for loop can be used to access individual elements of a tuple
address = (52066, "Aachen", "Eupener Str. 70", "0241-6009-12345")

for address_part in address:
    print(address_part)'''


#DICITONARIES


#if...else statements
'''name = input("Who are you? ")

if name == "Faith":
    print(f"Hello {name}, welcome!")
elif name == "Jane":
    print(f"Hello {name}, enjoy!")
else:
    print("Access denied")'''

#loops
'''i = 1
while i <=5 :
    print(i)
    if i == 3:
        break #stops the while loop
    i += 1

#loops and conditions make up a program

storedEmail = 'name@gmail.com'
storedPass = '12345'

failedLogIn = 0

while failedLogIn < 3:
    email = input("Enter your email: ")
    passw = input("Enter your password: ")

    failedLogIn += 1
    remainingattempts = failedLogIn + 1

    if email == storedEmail and passw == storedPass:
        print("Login successful")
    
    else:
        print(f"Incorrect email or Password. {remainingattempts} attempts left")#find out what's causing the error, fix it!!

else:        
    print("You have exceeded the maximum number of attempts.")
    print("Program terminated.")

#import json
names = ["chantal", "ayobami", "regina"]

selectedNames = []

for name in names:
    namess = selectedNames.append(name)

    if name == "Regina":
        break

    print(selectedNames)'''

#a student makes gonour roll if their average is >=85
#and their lowest grade is not below 70

'''gpa = float(input("What was your Grade Point Average? ")) #nesting functions, turns the 'str' input to a float
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= .85 and lowest_grade >= .70:
    print("Congratulations, you made the honor roll!")
else:
    print("Sorry, you did not make the honor roll this time around.")

#if you need to check if student's on honour roll, you can use boolean
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
    print(honour_roll)'''

#for loop
'''for name in ['Christopher', 'Sam']:
    print(name)'''

# range loops a number of times
'''for index in range(0, 2): #prints from 0 up to and nto including 2; 0,1
    #for i in range(5): #prints 5 objects - 0,1,2,3,4
    #for i in range(20, 30, 2): #start, stop+1, step size (from 20 until (not inclluding) 30, step size of 2)
    #for i in range(30, 20, -1): #prints backwards
    print(index)'''

#while
'''names = ['Jane', 'Kate']
index = 0
while index < len(names):
    print(names[index])
    index +=1 #must change condition in a while loop'''

#modules and packages
#module-python file with functions, classes and other components
#package-folder that contains multiple modules. Used for organizing code
#packages - published collections of modules, can be found on the internet with a search
#the best code is borrowed code
'''Importing a module
1. import module as namespace
    import helpers #module name is helpers.py
    helpers.display('Not a warning') #display is the function name
2. import all into current namespace
    from helpers import *
    display('Not a warning')
3. import specific items into current namespace
    from helpers import display
    display('Not a warning)'''

