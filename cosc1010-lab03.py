# Taylor Gili
# UWYO COSC 1010
# 9/26/2024
# Lab 03 
# Lab Section: 12
# Sources, people worked with, help given to: Donovan
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list

rockies = ('WYOMING', 'COLORADO', 'MONTANA')

#print the entire list

print(rockies)

#now print the first element in the list

print(rockies[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)

print(rockies[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

print(f'{rockies[1]} is south of {rockies[0]}')


print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
rockies = ["Wyoming", "Colorado", "Montana"]
rockies.append("Washington")
rockies.append("Oregon")
rockies.append("California")
print(rockies)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 

rockies.insert(5, "Maine")
print(rockies)

#Insert the state Texas to be the third element in the list, again printing your list

rockies.insert(2, "Texas")
print(rockies)

#Using the `del` statement remove the fourth item from the list, print your list 

del rockies[3]
print(rockies)

#Remove Texas using its value, print the list

del rockies[2]
print(rockies)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 

print(sorted(rockies))
print(rockies)

#Permanently sort your list in reverse order, printing it out

rockies.sort(reverse=True)
print(rockies)

#Using the reverse method reverse the list and print it

rockies.reverse()
print(rockies)