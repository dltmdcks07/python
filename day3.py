##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##print(f"num1 + num2 = {num1 + num2}")
##print(f"num1 - num2 = {num1 - num2}")
##print(f"num1 * num2 = {num1 * num2}")
##print(f"num1 / num2 = {num1 / num2:.2f}")
##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##print(f"num1 //num2 = {num1//num2}")
##print(f"num1 % num2 = {num1 %num2}")
##print(f"num1 **num2 = {num1 **num2}")
##sec = int(input("초 입력 : "))
##min = sec //60
##sec = sec % 60
##hour = min // 60
##min = min % 60
##day = hour // 24
##hour = hour % 24
##print(f"{day}일{hour}시간{min}분{sec}초")
##number = int(input(" 세 자리 숫자 입력 : "))
##number1 = number % 10
##number = number // 10
##number10 = number % 10
##number = number // 10
##number100 = number % 10
##print(f"백의 자리 : {number100}")
##print(f"십의 자리 : {number10}")
##print(f"일의 자리 : {number1}")
##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##num3 = int(input("세 번째 숫자 입력 : "))
##print(f"10000 += num1 -> {10000 + num1}")
##print(f"10000 -= num2 -> {10000 - num2}")
##print(f"10000 *= num3 -> {10000 * num3}")
##txt = input("문자열 입력 : ")
##num = input("숫자 입력 : ")
##txt2 = txt
##txt += num
##txt2 *= int(num)
##print(txt)
##print(txt2)








































##num1 = int(input("숫자를 입력해주세요: "))     ##문제 1
##num2 = 50
##print(num1 + num2)
##print(num1 - num2)
##print(num1 * num2)
##print(f"{num1 / num2:.3f}")

##w1 = 3                                    ##문제 2
##w2 = 4
##h = 5
##print("사다리꼴의 넓이는({0}+{1})*{2}/{3}={4}".format(w1,w2,h,2,(w1+w2)*h/2))

##num1 = int(input("숫자 1개 입력: "))       ##문제 3
##print(num1 //4)
##print(num1 %4)
##print(num1**4)

##kg = int(input("몸무게를 입력하세요: "))     ##문제 4
##m = float(input("키를 입력하세요: "))
##print(f"BMI지수는 {kg/m**2:.2f}")

##money = 1000                                    ##문제 5
##price = int(input("사고싶은 물건의 가격: "))  
##money =money - price #800
##coin500 = money // 500
##money = money % 500
##
##coin100 = money // 100
##money = money % 100
##
##coin50 = money // 50
##money = money % 50
##
##coin10 = money // 10
##money = money % 10
##
##print(f"""500원 {coin500}개 
##100원 {coin100}개 
##50원 {coin50}개 
##10원 {coin10}개 """)

##number = int(input("다섯 자리 숫자 입력: "))          ##문제 6
##num10000 = number // 10000
##number = number % 10000
##num1000 = number // 1000
##number = number % 1000
##num100 = number // 100
##number = number % 100
##num10 = number // 10
##number = number % 10
##num1 = number
##print(f"""만의 자리 : {num10000}
##천의 자리 : {num1000}
##백의 자리 : {num100}
##십의 자리 : {num10}
##일의 자리 : {num1}""")

##num1,num2, num3 =map(int,input("숫자 3개 입력 : ").split())    ##문제 1
##print(100-(num1+num2+num3))                   ##질문(map)

##a = int(input("숫자를 입력하세요: "))             ##문제 2
##b = "삐약"
##print(b*a)
