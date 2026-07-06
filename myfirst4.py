##Str = input("방향키를 입력해주세요(w/a/s/d): ")
##if 'w' == Str:
##    print("위 방향키를 입력하셨습니다.")
##elif 'a' == Str:
##    print("좌 방향키를 입력하셨습니다.")
##elif 's' == Str:
##    print("아래 방향키를 입력하셨습니다.")
##elif 'd' == Str:
##    print("우 방향키를 입력하셨습니다.")
##else:
##    print("잘못 입력하셨습니다.")
##a= input("문자열 입력: ")
##b= input("문자열 입력: ")
##print(a,b)
##temp = a
##a=b
##b=temp
##print(a,b)


##num = int(input("숫자를 입력해주세요: "))
##if num == 0:
##    print("number은 0입니다")
##elif num < 0:
##    print(num,"은/는 음수입니다")
##else 
##    print(num,"은/는 양수입니다")
##
##if num %2==0:
##    print(num,"은/는 짝수입니다")
##else
##    print(num,"은/는 홀수입니다")


##num = int(input("숫자를 입력해주세요: "))
##if 10<=num <=99:
##    print("두자리 숫자입니다.")
##else:
##    print("두자리 숫자가 아닙니다.")


##num = int(input("숫자를 입력해주세요: "))
##if num % 3 ==0:
##    print("이 숫자는 3의 배수입니다.")
##if num % 6 ==0:
##    print("이 숫자는 6의 배수입니다.")
##if num % 9 ==0:
##    print("이 숫자는 9의 배수입니다.")


##Input = input("알파벳을 입력해주세요: ")
##if 'a' <= Input <= 'z' :
##    print("소문자입니다.")
##elif 'A' <= Input <= 'Z' :
##    print("대문자입니다.")
##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = int(input())
##number2 = int(input())
##if number1> number2:
##    print("숫자 1이 숫자2보다 큽니다.")
##else:
##    if number1<number2:
##        print("숫자 2가 숫자 1보다 큽니다.")
##    else:
##        print("숫자 1과 숫자2가 같습니다.")
##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = int(input())
##number2 = int(input())
##if number1 > number2:
##    print("숫자 1이 숫자2보다 큽니다.")
##elif number1 < number2:
##    print("숫자 2가 숫자 1보다 큽니다.")
##else:
##    print("숫자 1과 숫자 2가 같습니다.")
##score = 75
##if score > 90:
##    print("성적은 A등급입니다.")
##elif score > 80:
##    print("성적은 B등급입니다.")
##elif score > 70:
##    print("성적은 C등급입니다.")
##elif score > 60:
##    print("성적은 D등급입니다.")
##else:
##    print("성적은 F등급입니다.")
##weight = int(input("무게를 입력해주세요: "))
##express = input("특송여부(y/n) : ")
##domestic = input("국내 배송 여부 (y/n): ")
##if weight <=2 and (express =='y' or domestic == 'y'):
##    print("무료 배송입니다.")
##elif weight <=5 and (express =='y' or domestic == 'y'):
##    print("유료 배송입니다.")
##else:
##    print("배송 불가합니다.")
##player_atk = int(input("현재 공격력: "))
##player_exp = 10
##monster_atk = 100
##if monster_atk > player_atk:
##    print("몬스터의 승리!")
##    print("경험치를 잃었다...")
##    player_exp -=5
##elif monster_atk < player_atk:
##    print("플레이어의 승리!")
##    print("경험치를 얻었다!!")
##    player_exp +=5
##else:
##    print("몬스터와 무승부..")
##    print("아무런 일도 일어나지 않았다.")
##print(f"현재 경험치: {player_exp} / 다음 레벨업까지: {100 - player_exp}")

##print("[계산기 프로그램]")
##choice = input("연산자를 입력해주세요. (+,-,*,/): ")
##num1 = float(input("첫 번째 숫자: "))
##num2 = float(input("두 번째 숫자: "))
##if choice == "+":
##    result = num1+num2
##    print(f"결과: {num1} + {num2} = {result}") 
##elif choice == "-":
##    result = num1-num2
##    print(f"결과: {num1} - {num2} = {result}")
##elif choice == "*":
##    result = num1*num2
##    print(f"결과: {num1} * {num2} = {result}")
##elif choice == "/":
##    if num2 !=0:
##        result = num1/num2
##        print(f"결과: {num1} + {num2} = {result}")
##    else:
##        print("오류: 0으로 나눌 수 없습니다.")
##else:
##    print("연산자를 잘못 입력하셨습니다.")

##num = int(input("숫자를 입력해주세요.(0~100): "))
##if 45<= num <= 55:
##    print("Perfect!!")
##elif 35<= num <= 65:
##    print("Excellent!!")
##else:
##    print("Good!!")

##year = int(input("연도를 입력해주세요: "))
##if year % 4 ==0 and year % 100 != 0 or year %400 ==0:
##    print("윤년입니다.")
##else:
##    print("윤년이 아닙니다.")
##num1 = int(input("첫번째 숫자를 입력해주세요: "))
##num2 = int(input("두번째 숫자를 입력해주세요: "))
##num3 = int(input("세번째 숫자를 입력해주세요: "))
##if num1> num2 and num1>num3:
##    print(num1, end=' ')
##    if num2 > num3:
##        print(num2,num3)
##    else:
##        print(num3,num2)  
##elif num2 > num1 and num2> num3:
##    print(num2, end=' ')
##    if num1 > num3:
##        print(num1, num3)
##    else:
##        print(num3, num1)
##else:
##    print(num3, end =' ')
##    if  num1 > num2:
##        print(num1, num2)
##    else:
##        print(num2, num1)

##num1 = int(input("첫번째 숫자를 입력해주세요: "))
##num2 = int(input("두번째 숫자를 입력해주세요: "))
##num3 = int(input("세번째 숫자를 입력해주세요: "))
##if num1 -1 ==num2 or num1+1 == num2 and num1 +1 ==num3 or num2 +1==num3:
##    print("스트레이트")
##else:
##    print("X")

##count =0
##while count <3:
##    print("{0}번째의 while문!".format(count))
##    count +=1
##count= 0
##while count<3:
##    print("{0}번째의 while문!".format(count))
##while True:
##    print("반복중~")
##while True:
##    print("무한 반복중...")
##count = 0
##while count <3:
##    print("{0}회 반복 중...".format(count))
##    count +=1
##count =0
##while count <100:
##    if count %3 ==0:
##        print("3의 배수: {0}".format(count))
##    count +=1
##while False:
##    print("False라면 출력이 되지 않습니다...")
##count =3
##while count >0:
##    print("{0}...".format(count))
##    count -=1
##number =10
##while number <= 1000000:
##    print(f"{number}")
##    number *=10


##num=0                     ##answer1
##while num <5:
##    print("파이썬")
##    num +=1

##num =1                      ##answer2
##total =0
##while num<=10:
##    total += num
##    num +=1
##print(total)

##num =0                    #answer3
##while num <=200:
##    print(num, end =' ')
##    num +=5

##num = 5
##i = 0
##while num <=200:
##    i +=1
##    print(num, end = ' ')
##    num +=5
##    if i %5==0:
##        print('')
##count =3
##while True:
##    print("숫자가 점점 작아져갑니다...")
##    count -=1
##    if count <0:
##        break
##count =0
##while count <5:
##    count +=1
##    if count %3 ==0:
##        continue
##    print(f"{count}번째 반복중")
##count =0
##while True:
##    print("{}번째 반복중...".format(count))
##    count +=1
##    if count >=5:
##        break
##count =0
##while count <13:
##    count +=1
##    if count %2 ==0 and count %3 ==0:
##        continue
##    print(f"{count}는 6의 배수가 아닙니다.")
##total =0
##while True:
##    number = int(input("양수를 입력해주세요 : "))
##    if number ==0:
##        break
##    elif number <0:
##        print("음수를 입력하셨습니다.")
##        continue
##    total +=number
##    print("현재까지의 양수의 합은 {0}입니다.".format(total))
##word = "Hellowhile"
##count =0
##while count < len(word):
##    if count %2 ==1:
##        count +=1
##        continue
##    print(word[count], end = '')
##    count +=1




































