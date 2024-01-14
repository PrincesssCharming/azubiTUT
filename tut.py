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
colors = ("red", "green", "blue")
print(colors[1])

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