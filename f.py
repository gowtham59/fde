g1=int(input())
flag2=0
if(g1>2):
    for i in range(2,int(g1/2)+1):
        if g1%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or g1==2:
    print("no")
