def disp(st):
    count=0
    num=int(input("Enter the position"))
    print("Num is", num)
    calc=int(num/3)
    rem=num%3
    
    if rem is 0:
        rem=2
        calc-=1
        print("Calc is", calc)
        print("Rem is", rem)
    else:
        rem=rem-1
        print("Calc is", calc)
        print("Rem is", rem)
    if b[calc][rem].find("X") is -1 and b[calc][rem].find("O") is -1:
        b[calc][rem]=st
        a[calc][rem]="   "
        for x in a:
            print("-------------")
            print(" ".join(map(str,"|")), end="")

            print("|".join(map(str,x)), end="")
            print("|")
        print("-------------")
        for x in b:
            print("-------------")
            print(" ".join(map(str,"|")), end="")

            print("|".join(map(str,x)), end="")
            print("|")
        print("-------------")
        if calc==0:
            if (b[calc+1][rem].find(st) is not -1 and b[calc+2][rem].find(st) is not -1):
                print("Congragulations {s} has won! Column1".format(s=st))
                return 2
        if rem==1:
            if (b[calc][rem-1].find(st) is not -1 and b[calc][rem+1].find(st) is not -1):
                print("Congragulations {s} has won! Row 2".format(s=st))
                return 2
        if calc==1:
            if (b[calc-1][rem].find(st) is not -1 and b[calc+1][rem].find(st) is not -1):
                print("Congragulations {s} has won! Column2".format(s=st))
                return 2
        if calc==2:
            if (b[calc-1][rem].find(st) is not -1 and b[calc-2][rem].find(st) is not -1):
                print("Congragulations {s} has won! Column3".format(s=st))
                return 2
        if rem==2:
            if (b[calc][rem-1].find(st) is not -1 and b[calc][rem-2].find(st) is not -1):
                print("Congragulations {s} has won! Row 3".format(s=st))
                return 2
        if rem==0:
            if (b[calc][rem+1].find(st) is not -1 and b[calc][rem+2].find(st) is not -1):
                print("Congragulations {s} has won! Row2".format(s=st))
                return 2
        if calc==0 and rem==0:
            if (b[calc+1][rem+1].find(st) is not -1 and b[calc+2][rem+2].find(st) is not -1):
                print("Congragulations {s} has won! Right diagonal".format(s=st))
                return 2

        if calc==1 and rem==1:
            if (b[calc-1][rem-1].find(st) is not -1 and b[calc+1][rem+1].find(st) is not -1):
                print("Congragulations {s} has won! Right diagonal".format(s=st))
                return 2

        if calc==2 and rem==2:
            if (b[calc-1][rem-1].find(st) is not -1 and b[calc-2][rem-2].find(st) is not -1):
                print("Congragulations {s} has won! Right diagonal".format(s=st))
                return 2
        if calc==0 and rem==2:
            if (b[calc+1][rem-1].find(st) is not -1 and b[calc+2][rem-2].find(st) is not -1):
                print("Congragulations {s} has won! Left Diagonal".format(s=st))
                return 2

        if calc==2 and rem==0:
            if (b[calc-1][rem+1].find(st) is not -1 and b[calc-2][rem+2].find(st) is not -1):
                print("Congragulations {s} has won! Left Diagonal".format(s=st))
                return 2
        if calc==1 and rem==1:
            if (b[calc-1][rem+1].find(st) is not -1 and b[calc+1][rem-1].find(st) is not -1):
                print("Congragulations {s} has won! Right diagonal".format(s=st))
                return 2
            
        count+=1
        if (count==9):
            print("End of the game")
            return 5
        else:
            print("Continue")
            return 1
            
    else:
        if(count==9):
            print("End of the game")
            return 5
        else:
            print("Wrong choice")
            disp(st)


a=[[" 1 "," 2 ", " 3 "],[" 4 ", " 5 ", " 6 "], [" 7 ", " 8 ", " 9 "]]
b=[["   ","   ", "   "],["   ", "   ", "   "], ["   ", "   ", "   "]]
for x in a:
    print("-------------")
    print(" ".join(map(str,"|")), end="")

    print("|".join(map(str,x)), end="")
    print("|")
print("-------------")
for x in b:
    print("-------------")
    print(" ".join(map(str,"|")), end="")

    print("|".join(map(str,x)), end="")
    print("|")
print("-------------")
for i in range(0,100):
    
    if (i%2==0):
        num=disp(" X ")
        if num==1:
            continue
        else:
            break
    else:
        num=disp(" O ")
        if num==1:
            continue
        else:
            break

        
    
