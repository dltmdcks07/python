##for i in range(5):
##    print(str(i) + "=반복 변수")
##print()
##
##for i in range(5,10):
##    print(str(i) + "=반복 변수")
##print()
##
##for i in range(0,10,3):
##    print(str(i) + "=반복 변수")
##print()

##array = [273,32,103,57,52]
##for i in range(len(array)):
##    print("{}번째 반복: {}".format(i,array[i]))

##for i in range(4,0-1,-1):
##    print("현재 반복 변수: {}".format(i))

##for i in reversed(range(5)):
##    print("현재 반복 변수: {}".format(i))

##output =""
##for i in range(1,10):
##    for i in range(0,i):
##        output +="*"
##    output +="\n"
##print(output)

##output =""
##for i in range(1,15):
##    for j in range(14,i,-1):
##        output +=' '
##    for k in range(0,2*i-1):
##        output +='*'
##    output +='\n'
##print(output)

##while True:
##    print(".", end = "")

##i=0
##while i<10:
##    print("{}번째 반복입니다.".format(i))
##    i+=1

##for num in range(5):
##    print(num, end= " ")
##for num in range(1,20):
##    print(num, end = ' ')
##for num in range(1,18,3):
##    print(num , end=' ')
##for i in range(10):
##    print("안녕",i, "번째")
##for i in range(1,10):
##    print("안녕",i, "번째")
##for i in range(1,11):
##    print("안녕",i, "번째")
##for i in range(2,101,2):
##    print(i, end = " ")
##for i in range(1,100,2):
##    print(i, end=" ")
##for i in range(10,0-1):
##    print(i, end=" ")
##total =0
##for i in range(1,101):
##    total +=i
##    print(total)
##for i in range(5,100+1,5):  #문제1
##    print(i)
##total=0
##for i in range(3,99+1,3):
##    total+=i
##print("3의 배수의 합: ",total)
##for i in range(1,11):
##    if i%2==0:
##        print("짝수번 안녕")
##    elif i %2 ==1:
##        print("홀수번 안녕")
##first_num =int(input("시작값 입력: "))
##last_num = int(input("끝값 입력: "))
##for i in range(first_num,last_num+1):
##    if i%2==0:
##        print("짝수: ",i)
##    elif i%2==1:
##        print("홀수: ",i)
##print("시작값 입력: ")
##first_num=int(input())
##print("끝값 입력: ")
##last_num = int(input())
##for i in range(first_num,last_num+1):
##    if i%2==0:
##        print("짝수: ",i)
##    elif i%2==1:
##        print("홀수: ",i)


##first= int(input("시작값 입력: "))     #문제 3
##last = int(input("끝값 입력: "))
##for i in range(first,last+1,1):
##    if i%3==0 and i%5==0:
##        print(i, end=" ")

##for num in range(1,100):
##    if num>55:
##        break
##    print(num,end=" ")
##for num in range(7):
##    power =2**num
##    if power >64:
##        break
##    print(power, end=" ")
##sum_odd=0
##for i in range(1,1000,2):
##    if i %13==0:
##        continue
##    print(i,end=" ")
##    sum_odd +=i
##    if sum_odd>500:
##        break
##odd =1
##for num in range(1,20):
##    if num%2==0:
##        continue
##    odd *=num
##    print(f"{num}={odd}")

##odd=1
##num=int(input("숫자를 입력해주세요: "))
##for i in range(2,100):
##    odd =num**i
##    if odd>10000:
##        break
##    print(odd)

##num =int(input("숫자를 입력해주세요: "))
##division=0
##print(num,"의 약수:",end=" ")
##for i in range(1,num+1):
##    division+=1
##    if num % division ==0:
##        print(division, end=" ")
##turn=3
##for i in range(100+1):
##    if i %15==0:
##        continue 
##
##    if i %3==0:
##        if turn==3:
##            print(i, end=" ")
##            turn =5
##    elif i %5==0:
##        if turn==5:
##            print(i, end=" ")
##            turn=3
##    
##    if i > 100:
##        break
##            
##count=0
##for i in range(100+1):
##    if count ==5:
##        break
##    elif i%3==0 and "7" in str(i):
##        count +=1
##        print(i, end=" ")







































