#Main Types of Data Structures in Python
'''----------------------------------------------'''
#! 1. List
#? Ordered collection of items
#? Mutable (you can change values)
#? Written in square brackets []

#* Example:

fruits = ["apple", "banana", "mango","coconut","papaya"]
'''
print(fruits[0]) #output:apple
print(fruits[0:4])#output:['apple', 'banana', 'mango', 'coconut']
print(fruits[::2])#output:['apple', 'mango', 'papaya']
print(fruits[-1])#output:papaya

'''
#print(help(fruits))
# print(len(fruits)) #output:5
# fruits[0]="dragon fruit"
# fruits.append("kiwi")
# print(fruits)
# fruits.remove("dragon fruit")
# print(fruits)
# fruits.insert(0,"pineapple")
# print(fruits)
# fruits.sort()
# print(fruits)

#.reverse()
#.clear()
#.index()
#.count()
#! 2. Tuple
#? Ordered collection
#? Immutable (cannot change values)
#? Faster than lists
#? Written in ()
#* Example:
# point = (10, 20)

#! 3. Set
#? Unordered collection
#? No duplicate values
#? Written in {}

#* Example:
# unique_nums = {1, 2, 3, 3}
# # Output: {1, 2, 3}

#! 4. Dictionary
# ?Stores data in key–value pairs
# ?Very fast lookups
#? Written in {key: value}
#* Example:
# person = {"name": "Sangam", "age": 20}
# print(person["name"])  # Sangam

capitals = {"USA": "Washington", "China": "Beiging", "Nepal": "Kathmandu","UAE":"Dubai"}

#capitals.update({"USA":"Newyork"})
#capitals.pop("China")#this removes china
#capitals.popitem() #removes the last key value pair
#capitals.clear() #removes every elem
#keys = capitals.keys()# gives every key
#values = capitals.values()# gives every value
#items=capitals.items() #prints every key value pair in the form of tuples
#print(items) #[('USA', 'Washington'), ('China', 'Beiging'), ('Nepal', 'Kathmandu'), ('UAE', 'Dubai')]

