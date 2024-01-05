#Author: Tristen Smith
#---
#Each line of the csv file is a record of a single ride at a 
#specific Marta station (Atlanta's subway system). Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#---
#This problem opens the marta csv file and sorts the data based on ...
#~~~1. Finds the station with the closest # of taps to the average
#~~~2. Finds the station with the least # of taps
#~~~3. Finds the average # of taps per station
#Read README.md from DB task 1 and follow the instructions
marta_file = open('marta sample.csv', 'r')
def marta(file):
    read_file = marta_file.readlines()
    dict = {}
    list = []
    new_list = []
    count = 0
    diff = 0
    average = 0
    above = 0
    below = 0
    least_traffic = 0
    for line in read_file:
        line = line.split(",") #turns each line into a list of values
        if not line[3] in dict:
            dict[line[3]] = [] #creates list of taps# for station, 71 total
            dict[line[3]] = 0
        dict[line[3]] += 1 #+1 for already keyed station/newly created station
    for key in dict.keys():
        count += 1 #number of stations
        average += dict[key] #adds all the number of taps per station together
    average /= count #creates the average number of taps per station
    for value in dict.values(): 
        diff = abs(value - average)   
        list.append(diff) 
        if (value - average) < 0:
            new_list.append(value) 
    new_list.sort() #sorts low-high so we can find the lowest value
    least_traffic = new_list[0] #station with the least amount of traffic
    list.sort() #sorts low-high so we can find the lowest value
    lowest = list[0] #smallest # in difference compared to average
    above = average + lowest #this is the smallest difference between # of taps vs avg
    below = average - lowest #this is the smallest difference between # of taps vs avg
    #we will use above and below in order to match them to their keys for closest to avg
    for key in dict: 
        if round(above) == round(dict[key]) or round(below) == round(dict[key]):
            closest = "The station ID with the closest to the average is: " + str(key)
        if least_traffic == dict[key]: #if this value matches key, = station
            least = "The station ID with the least amount of traffic is: " + str(key)
    average = "The average number of taps per station is: " + str(round(average))
    return closest + "\n\n" + least + "\n\n" + average   
print(marta(marta_file))