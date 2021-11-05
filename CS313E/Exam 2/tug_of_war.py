#  File: tug_of_war.py

#  Description: Given a list of each student’s body weight as non-zero integers and an integer threshold T, 
#				determine if it is possible for these students to separate into two teams 
#				where the strength difference between the two teams is lower than the threshold.

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


def permuter (lst, idx, permutations):
	'''
	recursively finds all permutations of lst
	returns all permutations of lst, storing them in permutations
	'''
	hi = len(lst)
	if (idx == hi):
		if lst not in permutations:
			permutations.append(lst[:])
		return permutations
	else:
		for i in range (idx, hi):
			lst[idx], lst[i] = lst[i], lst[idx]
			permuter(lst, idx + 1, permutations)
			lst[idx], lst[i] = lst[i], lst[idx]
		return permutations


def allocate_teams(arr, limit):
	'''
	allocates people into two teams
	returns teams in an array and the total weights for each team
	'''
	teams_arr = []
	temp_team_holder = []
	team_weight = 0
	team_weights = []

	for i in range(len(arr)):
		person = arr[i]
		team_weight += person
		temp_team_holder.append(person)     
		if team_weight > limit:
			teams_arr.append(temp_team_holder)
			temp_team_holder = []
			team_weights.append(team_weight)
			team_weight = 0

	if temp_team_holder:
		teams_arr.append(temp_team_holder)
		team_weights.append(team_weight)
	return teams_arr, team_weights


# Input: weight_lst: is a list of integers which represent the weight of each student
#		 T: is the threshold
# Output: Boolean. True means that it is possible for these students 
#		to separate into two teams where the strength difference 
#		between the two teams is lower than the threshold. 
def tugofwar(weight_lst, T):
	weight_lst = sorted(weight_lst)
	total_weight = sum(weight_lst)
	limit = total_weight/2

	permutations = []
	permutations = permuter(weight_lst, 0, permutations)

	for perm in permutations:

		teams_arr, team_weights = allocate_teams(perm, limit)
		if abs(team_weights[1] - team_weights[0]) <= T:
			return True

	return False
	


if __name__ == '__main__':


	# Read input list of weight
	weight_str = sys.stdin.readline().split()
	weight_lst = [ int(x) for x in weight_str ]

	# Read threshold
	T = int(sys.stdin.readline())

	# Output
	result = tugofwar(weight_lst, T)

	print(result)


	

