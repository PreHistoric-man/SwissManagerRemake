from collections import defaultdict




#Prints Welcome Text
print("Welcome to SMR")
number_of_player_s= input("Enter the No of Players :")
number_of_player = int(number_of_player_s)
names = input("Enter the Names").split()
#Converts List Names into a dictionary with name and points stored together
player_detail = { 
    index: {'name': name, 'score': 0}
    for index, name in enumerate(names)
}


#just test variables
player_detail[0]['score'] += 30
player_detail[1]['score'] += 10
player_detail[2]['score'] += 20
player_detail[3]['score'] += 40





#sorting thing(descending order)
sorted_list = {k:v for k,v in sorted(player_detail.items(),key = lambda v:v[1]['score'] , reverse=True)}
print(sorted_list)

#paring players
game1 = [sorted_list[3] , sorted_list[0]]
game2 = [sorted_list[2] , sorted_list[1]]

