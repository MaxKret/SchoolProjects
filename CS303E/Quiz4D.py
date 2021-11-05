# CS 303E Quiz 4D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Classified Correspondence
def classifiedCorrespondence(str):
    # replace pass with your solution for Problem 1
    result=""
    for c in str:
        if(ord(c)>=65 and ord(c)<=90):
            result+="X"
        elif(c.isdigit()):
            result+="X"
        else:
            result+=c
    return result


# Problem 2: Adjacent Products
def adjacentProducts(lst):
    # replace pass with your solution for Problem 2
    lstR = []
    for i in range(len(lst)-1):
        lstR.append(lst[i] * lst[i+1])
    return lstR


if __name__ == "__main__":
    # uncomment the following lines to run the given test cases

    #print(classifiedCorrespondence("operative name: JAMES BOND, code: 007"))
    #print(classifiedCorrespondence("address: 2317 Speedway, Austin, TX 78712"))
    #print(classifiedCorrespondence("phone: (512) 471-7316"))

    #print(adjacentProducts([29, 15, 13, 20, 21, 1, 29, 6, 27, 28, 1, 6]))
    #print(adjacentProducts([1, 2, 4, 8, 16]))
    #print(adjacentProducts([5, 6]))
    pass
