import random
'''
1 for rock
-1 for paper
0 for scissor'''
computer=random.choice([1,-1,0])
youstr=input("Enter your choice : ")
youDict={"r":1 , "p":-1 , "s":0}
you=youDict[youstr]
reverseDict={1:"rock" , -1:"paper" , 0:"scissor"}
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("TIE")
else:
    if(computer==-1 and you==1):
        print("you wins")

    elif(computer==-1 and you==0):
        print("you loss!")

    elif(computer==1 and you==-1):
        print("you loss!")

    elif(computer==1 and you==0):
        print("you win")

    elif(computer==0 and you==-1):
        print("you win")

    elif(computer==0 and you==1):
        print("you loss!")

    else:
        print("something went wrong")

        


    
    
    
    



