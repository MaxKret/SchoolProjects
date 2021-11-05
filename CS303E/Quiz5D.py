# CS 303E Quiz 5D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Verbose Vocabulary
def verboseVocabulary(A, B, C):
    abCount=0
    bcCount=0
    acCount=0
    abSim = set()
    bcSim = set()
    acSim = set()
    for ele in A:
        if(ele in B):
            abSim.add(ele)
            abCount+=1
    for elem in B:
        if(elem in C):
            bcSim.add(elem)
            bcCount+=1
    for eleme in C:
        if(eleme in A):
            acSim.add(eleme)
            acCount+=1
    if(abCount > bcCount and abCount > acCount):
        return abSim
    elif(bcCount > abCount and bcCount > acCount):
        return bcSim
    else:
        return acSim
        



# Problem 2: Get Grades
import math
def getGrades(lst):
    # replace pass with your solution for Problem 2
    avgGradesFinal = {}

    if lst == []:
        return {}

    for elem in lst:
        threeAvg = math.floor((elem[1]+elem[2]+elem[3])/3)
        if(threeAvg > elem[4]):
            avgGradesFinal[elem[0]] = threeAvg
        else:
            avgGradesFinal[elem[0]] = math.floor(elem[4])
    return avgGradesFinal
        



if __name__ == "__main__":
    # uncomment the following lines to run the given test cases

    #  print(
    #      verboseVocabulary(
     #         {"apple", "orange", "lemon", "grape"},
      #        {"apple", "kiwi", "strawberry"},
       #       {"strawberry", "lemon", "orange", "pineapple", "kiwi", "grape"},
        #  )
    #  )
    #  print(verboseVocabulary({"a", "b"}, {"c", "e"}, {"a", "b", "c", "d"}))
    #  print(verboseVocabulary({"x", "y", "z"}, {"x"}, {"y", "x"}))

    # print(
    #     getGrades(
    #         [
    #             ("Spongebob", 84, 87, 92, 82),
    #             ("Patrick", 25, 30, 20, 25),
    #             ("Sandy", 96, 95, 100, 99),
    #         ]
    #     )
    # )
    # print(getGrades([]))
    # print(getGrades([("Squidward", 80, 90, 65, 0), ("Plankton", 20, 20, 100, 100)]))
    pass