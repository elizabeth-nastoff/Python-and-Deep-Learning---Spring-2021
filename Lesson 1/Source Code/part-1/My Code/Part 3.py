# Steps
# takes sentence as input
# replace each occurrence of "python" with "pythons

#takes input as string
sen = input("Enter your sentence:")

# makes an empty list
senList = []
# assigns each word to be its own value in the list
senList = sen.split(" ")

# another new list
newList = []

#iterates through old list to find any values "python"
i = 0
while i < len(senList):
    if senList[i] == "python":
        newList.append("pythons")
        # if found, adds to list
        # else, adds original word
    else:
        newList.append(senList[i])
    i+=1

# changes list back to a string
strSen = ""
for word in newList:
    strSen = strSen+word+" "

print(strSen)