# TIC TAC TOE GAME

place = [1,2,3,4,5,6,7,8,9]
player = "X"
choice = 0
list1 = []
while(len(list1)!=9):
    print("\n\nTIC TAC TOE GAME\n\n")
    print(" {} | {} | {} ".format(place[0],place[1],place[2]))
    print("-----------")
    print(" {} | {} | {} ".format(place[3],place[4],place[5]))
    print("-----------")
    print(" {} | {} | {} ".format(place[6],place[7],place[8]))
    print("Player",player," : ",end="")
    choice = int(input())

    if(choice not in list1 and choice>0 and choice<10):
        list1.append(choice)
        place[choice-1] = player
        if( (place[0]==place[1] and place[1]==place[2]) or (place[3]==place[4] and place[4]==place[5]) or (place[6]==place[7] and place[7]==place[8]) or (place[0]==place[3] and place[3]==place[6]) or (place[1]==place[4] and place[4]==place[7]) or (place[2]==place[5] and place[5]==place[8]) or (place[0]==place[4] and place[4]==place[8]) or (place[2]==place[4] and place[4]==place[6]) ):
            print("\n\nPlayer "+player+" Win!")
            print(" {} | {} | {} ".format(place[0],place[1],place[2]))
            print("-----------")
            print(" {} | {} | {} ".format(place[3],place[4],place[5]))
            print("-----------")
            print(" {} | {} | {} ".format(place[6],place[7],place[8]))
            break
        if(player=="X"):
            player="0"
        else:
            player="X"
else:
    print("\n\nITS A DRAW MATCH!")
