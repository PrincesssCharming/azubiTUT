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
print(colors[1])'''

#dictionaries
'''person = {'name': 'John', 'age': 30, 'city': 'Nairobi'}
person['profession'] = 'Doctor' #an easy way to add to the list, the end of the list
print(person)
print(person['name'], person['age']) #print specific detail'''

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
print(p1)'''

#DICITONARIES


#if...else statements
name = input("Who are you? ")

if name == "Faith":
    print(f"Hello {name}, welcome!")
elif name == "Jane":
    print(f"Hello {name}, enjoy!")
else:
    print("Access denied")