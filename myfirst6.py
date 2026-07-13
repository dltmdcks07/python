##user1 = input("유저1 (가위/바위/보): ")
##user2 = input("유저2 (가위/바위/보): ")
##
##if user1 == user2:
##    print("비겼습니다.")
##
##elif (user1 == "가위" and user2 == "보"):
##    print("유저1이 이겼습니다.")
##elif (user1 == "바위" and user2 == "가위"):
##    print("유저1이 이겼습니다.")
##elif (user1 == "보" and user2 == "바위"):
##    print("유저1이 이겼습니다.")
##
##else:
##    print("유저2가 이겼습니다.")
##import random
##count =0
##while count <5:
##    print(random.randint(10,101))
##    count +=1
##import random
##count =0
##while count <5:
##    print(random.randrange(10,101,10))
##    count +=1


##import random           #문제 1
##count =0
##while count <20:
##    print(random.randint(3,11))
##    count +=1

##import random             #문제 2
##count=0
##while count <7:
##    print(random.randrange(2,100,5))
##    count +=1

##import random           ##문제 3
##Random = random.randint(1,100)
##while True:
##    Input=int(input("1~100 사이 숫자를 입력해 주세요: "))
##    if(Input > Random):
##        print("더 낮은 숫자가 정답입니다.")
##    elif(Input < Random):
##        print("더 높은 숫자가 정답입니다.")
##    else:
##        print("정답입니다")
##        break

##import random           ##문제 4
##time =0
##Random = random.randint(1,1000)
##while True:
##    time +=1
##    Input=int(input("1~1000 사이 숫자를 입력해 주세요: "))
##    if(Input > Random):
##        print("더 낮은 숫자가 정답입니다.")
##    elif(Input < Random):
##        print("더 높은 숫자가 정답입니다.")
##    else:
##        print("정답입니다")
##        break
##print("현재 입력 횟수는",time,"입니다")

##import random         #문제 5
##while True:
##    Random1 = random.randint(0,9)
##    Random2 = random.randint(0,9)
##    Random3 = random.randint(0,9)
##    if Random1 != Random2 and Random1 != Random3 and Random2 != Random3 :
##        break
##print("{0}{1}{2}".format(Random1 ,Random2 ,Random3))

##import random             #문제 6
##
##Random1 = random.randint(0,9)
##Random2 = random.randint(0,9)
##Random3 = random.randint(0,9)
####print("{0}{1}{2}".format(Random1 ,Random2 ,Random3))
##while True:
##    numbers = input("세자리 숫자를 입력해주세요: ")
##    n1 = int(numbers[0])
##    n2 = int(numbers[1])
##    n3 = int(numbers[2])
##
##    strike =0
##    ball =0
##    if n1 == Random1:
##        strike +=1
##    else:
##        ball +=1
##        
##    if n2 == Random2:
##        strike +=1
##    else:
##        ball +=1
##        
##    if n3 == Random3:
##        strike +=1
##    else:
##        ball +=1
##        
##    if strike == 3:
##        print("정답!")
##        break
##    
##    print("{0}strike, {1}ball".format(strike, ball))    

##format_a = "{}만원".format(5000)      #교재 136p
##format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
##format_c = "{} {} {}".format(3000,4000, 5000)
##format_d = "{} {} {}".format(1, "문자열", True)
##print(format_a)
##print(format_b)
##print(format_c)
##print(format_d)

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print("#기본")
print(output_a)
print("#특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)sss


























