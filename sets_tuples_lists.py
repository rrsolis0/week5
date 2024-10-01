# collection = single "variable" used to store multiple values
# Lists = [] ordered and changeable. Dupilcaqtes OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Typle = () ordered and unchangable. Dupilcates OK. FASTER

# fruits = ["apple", "orange" , "banana" , "coconut", "strawberry", "kiwi", "watermelon"]
# print(fruits[::2]) # gives me every second word/item
# print(fruits[2:]) #blank gives you the rest of the list
# print(fruits[::-1]) #puts it in backwards
# print(len(fruits)) # gives u length of list
# for fruit in fruits:
#     print(fruit)
# print(dir(fruits))  #gives you all the attributes for the list
# print(help(fruits)) it gives you all the help for documentation
# print("apple" in fruits) #it tells you if it is in the varaible
# print(fruits[0])
# for fruit in fruits:
    # print(fruit)

# fruits[0] = "pineapple" # changes the value and swaps them
# fruits.append("pineapple") # put something at the end of the list
# print(fruits)

# fruits.remove("apple") #removes only one thing
# # fruits.clear() #removes everything
# fruits.insert(0, "pineapple") #putting somehting in that spot and insterts it, pushes everything over
# fruits.sort() #puts everyhting in alphabetical order
# fruits.reverse()
# fruits.index("apple") #finds the index of the element
# for fruit in fruits:
#     print(fruit)

######################################################################

cars = ["Ford", "Vovlo", "BMW"]
# # add new cars in list
# cars.append("Honda")
# print(cars)
# # print out the list of cars in an f-string
# # that says "The cares in the list are: "
# print(f"The cars in the list are: {cars}")
# cars[-1] = "Toyota"
# # print out the list of cars in a f-string
# print(f'The cars in the list are: {cars}')
# # replace the 3rd element in the list with another car
# cars[2] = "austin martin"
# print(f'The cars in the list are: {cars}')
# # insert a new car in the 2nd position 
# cars.insert(1, "volkswagen")
# print(f'The cars in the list are: {cars}')
# # remove the 3rd element in the list
# cars.remove("Vovlo")
# print(f'The cars in the list are: {cars}')
# # check if the list contains the car "ford"
# print("Ford" in cars)

# for car in cars:
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f'The cars om the lsit are: {cars}')
#     if len(cars)== 10: 
#         print("You have reached the maximum number of cars")
#         break

#######################################################
# challanege
# create a lsit of freinds
# friends = ["Ruby"]
# # add 4 new friends
# # print out the list of friends in an f-string
# for freind in friends:
#     reqFriend = input("Enter a name: ")
#     friends.append(reqFriend)
#     if len(friends) == 5:
#         print(f"Your friends are: {friends}")
#     else:
#         print("")

# replace the last element in the list with another friend

# print out the list of friends in an f-string
# replace the 3rd element in the lsit with another friend
# print out the list of friends in an f-string
# insert a new friend in the 2nd position 
# print out the list of friends in an f-string

##################sets##################################
 # sets are unordered and unindexed
 # they are defined using curly brackets
 # they do not allow duplicates    
fruits = {"apple" ,"banana", "mango","cherry", "watermelon"}
print(fruits)
# print(dir(fruits)) #methods that can be used w sets
# print(help(fruits)) #documentation/methods that can be used with sets
# print(len(fruits)) #number of elements in a set
# print("vovlo" in fruits) #check if an element is in the set
# add an element to the set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)
# add mutiple elements to the set
print(fruits.update(["orange","kiwi","pineapple"]))
print(fruits)
# remove an element
print(fruits.remove("banana"))
print(fruits)
print(fruits.pop()) #removes the last element in the set
print(fruits)
print(fruits.clear()) #clears the set
print(fruits)
# when do we want to use sets?
# sets are useful when you want a store a collection of items that should not changed, and you do not care about the order of the items. 
# example: a collection of unique items
social_secruity_numbers = {123456789, 987654321, 123456789}
# remove the last element in this set
# print(social_secruity_numbers.pop())
print(social_secruity_numbers)
# add another social secruity number
print(social_secruity_numbers.add(678965478))
print(social_secruity_numbers)

########################## tuples ###########################
# tuples are immutable and are defined using paraenthesis
# create a tuple called mY_tuple wiht the following value: 
example_tuple = (1,2,3,4,5,6,7,8,9,10)
print(example_tuple)
print(example_tuple.count(2)) #count the number of times
# the value 2 appears in the tuple
print(dir(example_tuple)) #attributes that can be used with tuples
print(len(example_tuple)) # number of elements in the tuple
print(2 in example_tuple) #checkj if an element is in the tuple
# when are they useful?
# Tuples are useful when you want to store a collection of items that shpuld not be changed, such as days of the weeks, months of the year, etc. 
# if you want to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers peppers"
# # convert the string into a tuple
# # split it first 
# lymeric_tuple = tuple (lymeric.split())
# print(lymeric_tuple)
# # find how many times the letter "p" appears in the tuple
# print(lymeric_tuple.count())


# loops with tuples
for item in example_tuple:
    print(item)


#######docitionary###############]
#dictionaries are unordered, changeable, and indexed
# they are defined using curly brackets
# thye have keys and values
# a collection of {key:value} pairs, no duplicates
# keys are unique
    # values can be of any data type
capitals = { "Kenya":"Nairobi" , 
            "Uganda" : "Kampala",
            "Tanzania":"Dodoma",
            "Rwanda": "Kigali",
            "China":"Beijing",
            "USA": "Washington DC"}
print(capitals)
print(dir(capitals)) #attributes that can be used with dictionaries
print(help(capitals)) #documentation/methods that can be used with dictionaries
print(len(capitals)) #number of items in the dictionary
# if you want to check if a value of a key is in the dictionary
print(capitals(["Kenya"]))
print(capitals.get("Kenya"))
# add ab item to the dictionary #two ways
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria" : "Abuja"})
# add three more ciuntries and their capital to the dictionary
capitals.pop("China") #remove an item from idctionary
print(capitals)
# clear the dictionary
# captials.clear() #do not run this
# loop through the dicitionary
for key in capitals:
    print(f"These are {key}")

for value in capitals.values():
    print(value)

# prin they key valye pairs in the dictionary
items_all = capitals.items() # key valye pairs
for key, value in items_all:
    print(f"{key} is the capital of {value}")