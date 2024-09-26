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
# add new cars in list
cars.append("Honda")
print(cars)
# print out the list of cars in an f-string
# that says "The cares in the list are: "
print(f"The cars in the list are: {cars}")
cars[-1] = "Toyota"
# print out the list of cars in a f-string
print(f'The cars in the list are: {cars}')
# replace the 3rd element in the list with another car
cars[2] = "austin martin"
print(f'The cars in the list are: {cars}')
# insert a new car in the 2nd position 
cars.insert(1, "volkswagen")
print(f'The cars in the list are: {cars}')
# remove the 3rd element in the list
cars.remove("Vovlo")
print(f'The cars in the list are: {cars}')
# check if the list contains the car "ford"
print("Ford" in cars)

