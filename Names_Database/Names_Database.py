#Author: Tristen Smith
#---
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls in the 2010's.
#The list is used to see what names are most common in a given year.
#---
#This problem opens the names csv file and sorts the data based on ...
#~~~1. How many total births are covered by the names in the database?
#~~~2. How many total names are listed in the database?
#~~~3. How many total babies were given names that both start and end with a vowel?
#~~~4. How many boys have names that begin with the letter Z?
#~~~5. What is the most common girl's name that begins with the letter Q?
#~~~6. What letter is the least common first letter of a baby's name?
#~~~7. How many babies were born with names starting with that least-common letter?
#~~~8. What letter is the most common first letter of a baby's name
#~~~9. How many babies were born with names starting with that most-common letter?
#Read README.md from DB task 3 and follow the instructions
names_file = open('names sample.csv', "r")
def names(file):
    read_file = file.readlines()
    name_count = 0
    birth_count = 0
    z_boy_count = 0
    vowel_birth_count = 0
    least_common_count = 0
    most_common_count = 0
    q_girl_dict = {}
    q_girl_list = []
    first_letter_dict = {}
    first_letter_list = []
    vowels = "AEIOU"
    for i in read_file: #goes over every line in the csv file
        name_count += 1 #total # of names
        i = i.split(",") #makes every line read become a list
        birth_count += int(i[1]) #total # of births
        if i[0][0] not in first_letter_dict: #**this will be used with code farther below**
            first_letter_dict[i[0][0]] = 0 #creates a dictio with the first letter as keys
        first_letter_dict[i[0][0]] += 1 #and how many names start with that letter as values
        if i[0][0] == "Z" and i[2][0] == "B":
            z_boy_count += 1 #total # of boy names starting with "Z"
        if i[0][0] in vowels and i[0][-1] in vowels.lower():
            vowel_birth_count += int(i[1]) #total # of names starting and ending with a vowel
        if i[0][0] == "Q" and i[2][0] == "G": #**this will be used with code farther below**
            if i[0] not in q_girl_dict:
                q_girl_dict[i[0]] = int(i[1]) #creates dictio with girl names starting with "Q"
    vowel_birth_count = "The total # of names starting and ending with a vowel is: " + str(vowel_birth_count)
    z_boy_count = "The total # of boy names starting with the letter Z is: " + str(z_boy_count)
    birth_count = "The total # of births in the database is: " + str(birth_count)
    name_count = "The total # of names in the database is: " + str(name_count)
    #---
    #this code block is the next step from the previous for loop's last conditional
    for value in q_girl_dict.values():
        q_girl_list.append(value)
    q_girl_list.sort() #sorts a list of the values of q_girl_dict
    common_q = q_girl_list.pop()
    for key in q_girl_dict: 
        if q_girl_dict[key] == common_q: #if the highest birth value matchs the key's value
            common_q = key #then this is the most common Q name for a girl 
    common_q = "The most common name that starts with the letter Q is: " + common_q
    #---
    #this code block is the next step from the first for loop's first conditional
    for value in first_letter_dict.values():
        first_letter_list.append(value)
    first_letter_list.sort() #sorts the list of least to most common first letters
    least_common = first_letter_list[0] #value for the least common first letter
    most_common = first_letter_list[-1] #value for the most common first letter
    for key in first_letter_dict: #runs through the dictionary to match the above values with their keys
        if first_letter_dict[key] == least_common:
            least_common = key
        if first_letter_dict[key] == most_common:
            most_common = key
    for i in read_file: #adds up how many births happened with the least/most common first names
        i = i.split(",")
        if i[0][0] == least_common:
            least_common_count += int(i[1])
        if i[0][0] == most_common:
            most_common_count += int(i[1])
    least_common = "The least most common first letter in the database is " + least_common + " with " + str(least_common_count) + " counts"
    most_common = "The most common first letter in the database is " + most_common + " with " + str(most_common_count) + " counts"
    #---
    return birth_count + "\n\n" + name_count + "\n\n" + vowel_birth_count + "\n\n" + z_boy_count + "\n\n" + common_q + "\n\n" + least_common + "\n\n" + most_common
print(names(names_file))