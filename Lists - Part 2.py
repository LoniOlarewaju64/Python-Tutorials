# Adding Files
items = ["a", "b"] #Adds to the end of the list.
items.append('c') #Inserts "x" at position 2. 
items.insert(2, "x") 
items.extend(["d", "e"])

#Removing Items
items = ["apples", "bananas,", "cherries", "mangoes"] 
items.remove("apples") #Remove the first occurence of the item in the list.
sold_out_item = items.pop # Remove and return the last item on the list. 
items.clear 
print(items)

#To delete specific items from the list by index.
fruit_list = ["mangoes", "pineapples", "kiwis"]
del fruit_list[2]
print(fruit_list)

#Utility & Ordering Methods
nums = [4, 2, 9, 1, 5]

nums.sort() # Default ascending to descending.
nums.sort(reverse=True) # Descending to ascending.
nums.reverse() # This reverses the list.
print(nums)
print(nums.count(4)) # This is used to count how many times an item appears. 
print(nums.index(9)) # This gets the index of an item. 



#LISTS: Built-in Functions
scores = [10, 20, 30, 40]

print(len(scores)) # This returns the number of the items in the list.
print(max(scores)) # This'll give the maximum item in the list.
print(min(scores)) # This will give the minimum item in the list. 
print(sum(scores)) # This'll print the sum of all values in the list. 
