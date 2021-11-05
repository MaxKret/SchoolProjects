def splitter(arr, limit):

    split_arr = []
    temp_list_holder = []
    team_weight = 0

    for person in arr:
        team_weight += person[0] 
        temp_list_holder.append(person)     
        if team_weight > limit:
            split_arr.append(temp_list_holder)
            temp_list_holder = []
            team_weight = 0

    if temp_list_holder:
        split_arr.append(temp_list_holder)
    return split_arr

arr = [[60], [50], [50]]

arr = sorted(arr)

team_weight = sum(x[0] for x in arr )

splmitt = team_weight // 2

print(arr)

print(team_weight)

print(splmitt)

spl = splitter(arr, splmitt)

import pprint 

pprint.pprint(spl)