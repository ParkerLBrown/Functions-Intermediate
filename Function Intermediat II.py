# Assignment: Functions Intermediate II

# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.


# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#    1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#  {        x[0]       }  {         x[1]       }
# [ [5,      2,      3],   [10,      8,      9] ]
# x[0][0] x[0][1] x[0][2] x[1][0] x[1][1] x[1][2]

x[1][0] = 15   # targets the second list in the parent list, changes 10 to 15
print(x[1][0]) # prints the value of 15 
print(x[1])    # prints the second list in x
print(x)       # prints the entirety of x

#    2. Change the last_name of the first student from 'Jordan' to 'Bryant'

#             {                    students[0]                   } {                  students[1]                   }
# students = [ {'first_name':  'Michael', 'last_name' : 'Jordan'},  {'first_name' : 'John', 'last_name' : 'Rosales'} ]
# targeting      dictname[0][keyname]       dictname[0][keyname]     dictname[1][keyname]     dictname[1][keyname]
# value                Michael                     Jordan                    John                    Rosales

students[0]['last_name'] = 'Bryant' #targets last_name key in first dict in students
print(students[0]['last_name'])
print(students)

#    3. In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Anfres' 
print(sports_directory['soccer'][0])
print(sports_directory)

#    4. Change the value 20 in z to 30

z[0]['y'] = 30
print(z[0]['y'])
print(z)


# 2. Iterate Through a List of Dictionaries

# THIS IS THE ONE I NEED HELP WITH

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
# For example, given the following list:



my_dict = { "name": "Noelle", "language": "Python" }
for v in my_dict:
    print(v)
# output: name, language

for k, v in my_dict.items():
    print(k, v)


studentsTwo = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print(studentsTwo[0])

print('example:')
dataList = [{'a': 1, 'd': 2}, {'b': 3, 'e': 4}, {'c': 5, 'f': 6}]
for index in range(len(dataList)):
    for key in dataList[index]:
        print(dataList[index][key])

# def iterateDictionary(some_list):

#     for k, v in some_list #.items() ??? :
#         print(k, v)


# # def iterateDictionary(some_list):
#     for k in some_list:
#         print k
# def iterateDictionary(some_list):


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3. Get Values From a List of Dictionaries



# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

def iterateDictionary2(key_name, some_list):
    for d in some_list:
        print(d[key_name])


# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

iterateDictionary2('first_name', studentsTwo)


# And iterateDictionary2('last_name', students) should output:
# Jordana
# Rosales
# Guillen
# Tonel



iterateDictionary2('last_name', studentsTwo)


# 4. Iterate Through a Dictionary with List Values

# EDIT: THIS IS THE FUNCTION I HAVENT STARTED WORKING ON


#    Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
#    and then prints the associated values within each key's list. For example:

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# # output:

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank


# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printInfo(some_dict):
    #pull number of locations in list
    #print
    #pull number of instructors in list
    #print