# Steps
# Input a string as a list of characters
# delete at least 2 characters
# Reverse the result

# takes input and print it back to confirm
string = input("Enter your string of at least 5 characters:")
print("Your string:", string)

# creates an empty list
strList = []
# single line fill the list with individual characters from the string
strList[:0] = string

print("String as list:", strList)

# removing character at index 0
strList.pop(0)
# remove character at index 3 (which was previously index 4)
strList.pop(3)

# it wasn't clarified how to select which characters should be removed
print("String with 1st and 5th character removed:", strList)

# There's a built in function to reverse a list
strList.reverse()

print("Reversed list:", strList)

# Create a blank string then iterate though strList
newStr = ""
for i in strList:
    # appends the list values to the string
    newStr = newStr+i

print("Resulting string:", newStr)

