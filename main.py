#Prints Welcome Text
print("Welcome to SMR V1")
tournament_type = input("Do u Want Round Robin(6-10 players) Type 1 to select it")
number_of_player_s= input("Enter the No of Players :")
number_of_player = int(number_of_player_s)
if type =='1' and number_of_player < 6:
    print("Robin round wont work")
    exit()
names = input("Enter the Names").split()
score = input("Enter the score").split()
score_n = []

for x in score:
    score_n.append(int(x))
print(score_n)


#Converts List Names into a dictionary with name and points stored together
player_detail = { 
    index: {'name': name, 'score': 0}
    for index, name in enumerate(names)
}

for x in player_detail:
    player_detail[x]['score'] = score_n[x] 


#just test variables
for x in player_detail:
    player_detail[x]['score'] += 0


#sorting thing(descending order)
sorted_list = {k:v for k,v in sorted(player_detail.items(),key = lambda v:v[1]['score'] , reverse=True)}
print(sorted_list)
#Round Robin Structure
#paring players Higher Initial points paired together
match number_of_player:
    case 6:

        game1 = [sorted_list[5],sorted_list[4]]
        game2 = [sorted_list[3] , sorted_list[2]]
        game3 = [sorted_list[1] , sorted_list[0]]
        ans1 = input("Who Won Game-1 Press 1 for 5 and Press 2 for 4 ")
        if(ans1 == '1'):
            game1win = [sorted_list[5]]
            sorted_list[5]['score'] += 10
            sorted_list[4]['score'] -= 20
        elif(ans1 == '2'):
            game1win = [sorted_list[4]]
            sorted_list[4]['score'] += 10
            sorted_list[5]['score'] -= 20
        ans2  = input("Who won game-2 press 1 for 3 and 2 for 2")
        if(ans2 == '1'):
            game2win = [sorted_list[3]]
            sorted_list[3]['score'] += 10
            sorted_list[2]['score'] -= 20
        elif(ans2 == '2'):
            game2win = [sorted_list[2]]
            sorted_list[2]['score'] += 10
            sorted_list[3]['score'] -= 20
        ans3  = input("Who won game-3 press 1 for 1 and 2 for 0")
        if(ans3 == '1'):
            game3win = [sorted_list[1]]
            sorted_list[1]['score'] += 10
            sorted_list[0]['score'] -= 20
        elif(ans3 == '2'):
            game3win = [sorted_list[0]]
            sorted_list[0]['score'] += 10
            sorted_list[1]['score'] -= 20
    case 7:
        game1 = [sorted_list[6],sorted_list[5]]
        game2 = [sorted_list[4] , sorted_list[3]]
        game3 = [sorted_list[2] , sorted_list[1]]
        sorted_list.pop(0)
        ans1 = input("Who Won Game-1 Press 1 for 6 and Press 2 for 5 ")
        if(ans1 == '1'):
            game1win = [sorted_list[6]]
            sorted_list[6]['score'] += 10
            sorted_list[5]['score'] -= 20
        elif(ans1 == '2'):
            game1win = [sorted_list[5]]
            sorted_list[5]['score'] += 10
            sorted_list[6]['score'] -= 20
        ans2  = input("Who won game-2 press 1 for 4 and 2 for 3")
        if(ans2 == '1'):
            game2win = [sorted_list[4]]
            sorted_list[4]['score'] += 10
            sorted_list[3]['score'] -= 20
        elif(ans2 == '2'):
            game2win = [sorted_list[3]]
            sorted_list[3]['score'] += 10
            sorted_list[4]['score'] -= 20
        ans3  = input("Who won game-3 press 1 for 2 and 2 for 1")
        if(ans3 == '1'):
            game3win = [sorted_list[2]]
            sorted_list[2]['score'] += 10
            sorted_list[1]['score'] -= 20
        elif(ans3 == '2'):
            game3win = [sorted_list[1]]
            sorted_list[1]['score'] += 10
            sorted_list[2]['score'] -= 20

    



    




#check win or loss and print ranking
update_sorted_list = {k:v for k,v in sorted(sorted_list.items(),key=lambda final:final[1]['score'] , reverse=True)}
print("The final rank List is : ")
print(update_sorted_list)