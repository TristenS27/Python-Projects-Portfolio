#Author: Tristen Smith
#---
#The football csv file contains information from a database that includes 
#Georgia Tech's entire football history.
#---
#This problem opens the football csv file and sorts the data based on ...
#~~~1. Who was the first team Georgia Tech ever played against?
#~~~2. How many points has Georgia Tech scored all-time against Auburn?
#~~~3. How many points has Auburn scored all-time against Georgia Tech?
#~~~4. What is Georgia Tech's all-time record in home games?
#~~~5. What was Georgia Tech's record in all games played in the 2009 calendar year?
#~~~6. What is Georgia Tech's all-time record in the month of October?
#~~~7. Georgia Tech played in the SEC from 1933 to 1963. What was its record during this time?
#~~~8. Against what team has Georgia Tech scored the most points?
#Read README.md from DB task 2 and follow the instructions
football_file = open('football sample.csv', 'r')
def game(file):
    game_list = []
    read_file = football_file.readlines()
    for i in read_file:
        i = i.split(",")
        game_list.append(i)
    game_list.sort()
    first_game = "Georgia Tech's first game ever played was against " + str(game_list[0][1])
    #---
    points = 0
    anti_points = 0
    for i in game_list:
        if i[1] == "Auburn":
            points += int(i[3])
            anti_points += int(i[4])
    points_vs_auburn = "Georgia Tech has scored " + str(points) + " points all time against Auburn"
    points_vs_tech = "Auburn has scored " + str(anti_points) + " points all time against Georgia Tech"
    #---
    wins_home = 0
    wins_2009 = 0
    wins_oct = 0
    losses_home = 0
    losses_2009 = 0
    losses_oct = 0
    ties_home = 0
    ties_2009 = 0
    ties_oct = 0
    for i in game_list:
        if i[2] == "Home":           
            if int(i[3]) == int(i[4]):
                ties_home += 1
            elif int(i[3]) > int(i[4]):
                wins_home += 1
            elif int(i[4]) > int(i[3]):
                losses_home += 1
        if i[0][:4] == "2009":
            if int(i[3]) == int(i[4]):
                ties_2009 += 1
            elif int(i[3]) > int(i[4]):
                wins_2009 += 1
            elif int(i[4]) > int(i[3]):
                losses_2009 += 1    
        if i[0][5:7] == "10":
            if int(i[3]) == int(i[4]):
                ties_oct += 1
            elif int(i[3]) > int(i[4]):
                wins_oct += 1
            elif int(i[4]) > int(i[3]):
                losses_oct += 1        
    record_home = str(wins_home) + "-" + str(losses_home) + "-" + str(ties_home)
    record_home = "Georgia Tech's all time record in home games is: " + record_home
    record_2009 = str(wins_2009) + "-" + str(losses_2009) + "-" + str(ties_2009)
    record_2009 = "Georgia Tech's all time record in 2009 was: " + record_2009
    record_oct = str(wins_oct) + "-" + str(losses_oct) + "-" + str(ties_oct)
    record_oct = "Georgia Tech's all time record in the month of October is: " + record_oct
    #---
    wins_sec = 0
    losses_sec = 0
    ties_sec = 0
    for i in game_list:
        for k in range(33, 64):
            if i[0][2:4] == str(k):
                if int(i[3]) == int(i[4]):
                    ties_sec += 1
                elif int(i[3]) > int(i[4]):
                    wins_sec += 1
                elif int(i[4]) > int(i[3]):
                    losses_sec += 1    
    record_sec = str(wins_sec) + "-" + str(losses_sec) + "-" + str(ties_sec)
    record_sec = "Georgia Tech's all time record from '33 to '63 was: " + record_sec
    #---
    points_list = []
    for i in game_list:
        points_list.append(int(i[3]))
    points_list.sort()
    high = points_list.pop()
    for i in game_list:
        if int(i[3]) == high:
            team = i[1]
            team = "Georgia Tech has scored the most points(222) against the team of: " + team
    return first_game + "\n\n" + points_vs_auburn + "\n\n" + points_vs_tech + "\n\n" + record_home + "\n\n" + record_2009 + "\n\n" + record_oct + "\n\n" + record_sec + "\n\n" + team
print(game(football_file))