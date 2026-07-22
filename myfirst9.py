##list_a = [1,2,3]
##list_b = [4,5,6]
##print("#리스트")
##print("list_a =", list_a)
##print("list_b =", list_b)
##print()
##print("# 리스트 기본 연산자")
##print("list_a + list_b =", list_a+ list_b)
##print("list_a *3=",list_a*3)
##print()
##print("#길이 구하기")
##print("len(list_a)=",len(list_a))


##list_a = [1,2,3]
##print("#리스트 뒤에 요소 추가하기 ")
##list_a.append(4)
##list_a.append(5)
##print(list_a)
##print()
##print("#리스트 중간에 요소 추가하기")
##list_a.insert(0,10)
##print(list_a)


##list_a = [0,1,2,3,4,5]
##print("#리스트의 요소 하나 제거하기")
##del list_a[1]
##print("del list_a[1]:",list_a)
##list_a.pop(2)
##print("pop(2): ", list_a)


##time=0
##for y in range(10,300+1,10):
##    time+=1
##    print(y, end=" ")
##    if time ==5:
##        print(" ")
##        time=0


##num=5
##for y in range(1,num+1):
##    for x in range(0,y):
##        print(chr(ord('A')+y+x-1),end=" ")
##    print()

##for i in range(1,10):
##    print(2,"*",i,"=",2*i)
##for i in range(1,10):
##    print("2 * %d = %d " %(i,2*i))
##for i in range(1,10):
##    print("{0} * {1} = {2}".format(2,i,2*i))

##for i in range(1,10):
##    print("{0}*{1}={2}".format(2,i,2*i))
##for i in range(1,10):
##    print("{0}*{1}={2}".format(3,i,3*i))
##for i in range(1,10):
##    print("{0}*{1}={2}".format(4,i,4*i))
##for i in range(1,10):
##    print("{0}*{1}={2}".format(5,i,5*i))

##dan =2
##for i in range(1,10):
##    print("{0} * {1} = {2}".format(dan,i,dan*i))
##dan+=1
##for i in range(1,10):
##    print("{0} * {1} = {2}".format(dan,i,dan*i))
##dan+=1
##for i in range(1,10):
##    print("{0} * {1} = {2}".format(dan,i,dan*i))
##dan+=1
##for i in range(1,10):
##    print("{0} * {1} = {2}".format(dan,i,dan*i))

##for dan in range(2,10):
##    for i in range(1,10):
##        print("{0} * {1} = {2}".format(dan,i,dan*i))
##for dan in range(2,10):
##    print("===={0}단====".format(dan))
##    for su in range(1,10):
##        print("{0} * {1} = {2}".format(dan,su,dan*su))

##for su in range(1,10):
##    for dan in range(2,10):
##        print(f"{dan:d} * {su:d} = {dan*su:-2d}",end="  ")
##    print()

##for su in range(1,10):
##    for dan in range(2,10):
##        if dan %2 ==0:
##            continue
##        print(f"{dan:2d} * {su:2d} = {dan*su:-3d}",end="  ")
##    print()


##for dan in range(2,10,3):
##    for su in range(1,10):
##        for dan_2 in range(dan,dan+3):
##            print(f"{dan_2:2d} * {su:2d} = {dan_2*su:-3d}",end="   ")
##        print()
##    print()


##start = int(input("몇단부터? : "))
##end = int(input("몇단까지? : "))
##for start in range(start,end+1):
##    print()
##    for i in range(1,10):
##        print("{0} * {1} = {2}".format(start,i,start*i))
    

##num =int(input("몇개씩? : "))
##end = int(input("몇단까지? : "))
##for dan in range(2,end+1,num):
##    for su in range(1,10):
##        for dan_2 in range(dan,dan+num):
##            if dan_2>end:
##                break
##            print(f"{dan_2:2d} * {su:2d} = {dan_2*su:-3d}",end="   ")
##        print()
##    print()

##for i in range(1, 6):
##    print("*",end = "")

##for i in range(1,6):
##    for j in range(1,6):
##        print("*",end="")
##    print()

##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end="")
##    print()

##for i in range(1, 6):
##    for j in range(i,6):
##        print("*",end="")
##    print()

##for out in range(1, 6):
##    for blank in range(1,out+1):
##        print(" ",end="")
##    for star in range(out,6):
##        print("*",end="")
##    print()


##for out in range(1, 6):
##    for blank in range(out,6):
##        print(" ",end="")
##    for star in range(1,out+1):
##        print("*",end="")
##    for star_2 in range(2,out+1):
##        print("*",end="")
##    print()


##for out in range(1, 6):              ##문제1
##    for blank in range(out,6):
##        print(" ",end="")
##    for star in range(1,2*out+1,2):
##        print("*",end="")
##    for star_2 in range(2,out+1):
##        print("*",end="")
##    print()
##
##
##starcnt = 1                        ##문제1
##for out in range(1, 6):
##    for blank in range(out,6):
##        print(" ",end="")
##    for star in range(1,starcnt +1):
##        print("*",end="")
##    starcnt+=2
##    print()
##
##
##for out in range(1, 6):           ##문제1
##    for blank in range(out,6):
##        print(" ",end="")
##    for star in range(1,2*out-1 +1):
##        print("*",end="")
##    print()


##for out in range(1, 6):
##    for blank in range(out,6):
##        print(" ",end="")
##    for star in range(1,2*out-1 +1):
##        print("*",end="")
##    print()
##for out in range(6,0,-1):
##    for blank in range(out,6):
##        print(" ",end="")
##    for star in range(1,2*out-1 +1):
##        print("*",end="")
##    print()


##s="PYTHON"
##for y in range(len(s)):
##    for x1 in range(len(s)-y-1):
##        print(" ",end="")
##    for x2 in range(2*y+1):
##        print(s[x2%len(s)],end="")
##    print()






























