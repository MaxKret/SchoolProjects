isLooping = True
inInt = int(input())
lastDig = 0
digSum = 0
while(isLooping):

    if(inInt<10):
        lastDig = inInt
    else:
        lastDig = inInt % 10
    
    digSum = digSum + lastDig
    
    if((inInt // 10) < 1):
        isLooping=False
    else:
        inInt = inInt // 10
print(digSum)