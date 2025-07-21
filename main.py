#Prints Welcome Text
print("Welcome to SMR V1")
number_of_player_s= input("Enter the No of Players :")
number_of_player = int(number_of_player_s)
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
player_detail[0]['score'] += 0
player_detail[1]['score'] += 0
player_detail[2]['score'] += 0
player_detail[3]['score'] += 0





#sorting thing(descending order)
sorted_list = {k:v for k,v in sorted(player_detail.items(),key = lambda v:v[1]['score'] , reverse=True)}
print(sorted_list)

#paring players Higher Initial points paired together
game1 = [sorted_list[3] , sorted_list[0]]
game2 = [sorted_list[2] , sorted_list[1]]


#check win or loss and print ranking
ans1 = input("Who Won Game1 Press 1 for 3 and Press 2 for 0 ")
if(ans1 == 1):
    game1win = [sorted_list[3]]
    sorted_list[3]['score'] += 10
    sorted_list[0]['score'] -= 20
else:
    game1win = [sorted_list[0]]
    sorted_list[0]['score'] += 10
    sorted_list[3]['score'] -= 20
ans2 = input("Who Won Game2 Press 1 for 2 and 2 for 1")
if(ans2 == 1):
    game2win = [sorted_list[2]]
    sorted_list[2]['score'] += 10
    sorted_list[1]['score'] -= 20

else:
    game2win = [sorted_list[1]]
    sorted_list[1]['score'] += 10
    sorted_list[2]['score'] -= 20

update_sorted_list = {k:v for k,v in sorted(sorted_list.items(),key=lambda final:final[1]['score'] , reverse=True)}
print("The final rank List is : ")
print(update_sorted_list)