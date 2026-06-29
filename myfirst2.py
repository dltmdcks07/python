##a,b,c= input("전화번호 입력 : ").split("-")         #문제 1
##print(a)
##print(b)
##print(c)


##a = input("파일명을 입력해주세요 : ")           #문제 2
##b = a.replace("jpg","png")
##print(a, "파일을 ",b,"파일로 변경하였습니다.")



##a = "Hello, Python! Hello, String!"         #문제 3
##print(a.upper())
##print(a.lower())



##a = input("영화 제목을 입력하세요: ")         #문제 1
##b = input("개봉 연도를 입력하세요: ")
##c = input("주연 배우를 입력하세요: ")
##print("{}은(는) {}년에 개봉한 {}의 영화입니다.".format(a,b,c))



##ID = input("아이디를 입력해주세요(6글자 이상): ")          #문제 2
##print("암호화된 아이디", ID[:3],"*"*(len(ID)-3))



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
##인테져가 뭐야





##egg = int(input("계란 개수 입력: "))
##tmp = egg
##tmp %= 30
##egg //= 30
##print("계란 {0}판, 나머지 {1}개".format(egg, tmp))
##first = int(input("피자를 몇 등분할까? : "))
##second = int(input("한 조각을 몇 등분할까? : "))
##pizza = 100
##pizza /= first
##pizza /= second
##print(f"이 조각은 피자 한 판의 {pizza:.2f}%")
##num_ori = 1357      # % = 나머지 , // = 몫 
##num = num_ori
##num %=10
##print(num)
##
##num_ori //=10
##num = num_ori
##num %=10
##print(num)
##
##num_ori //=10
##num = num_ori
##num %=10
##print(num)
##
##num_ori //=10
##num = num_ori
##num %=10
##print(num)


##num1 = int(input(" 숫자 입력: "))         ##문제4 1차 
##num2 = int(input(" 숫자 입력: "))
##num3 = int(input(" 숫자 입력: "))
##num4 = int(input(" 숫자 입력: "))
##num5 = int(input(" 숫자 입력: "))
##print(f"{(num1+num2+num3+num4+num5)/5:.3f}")

##num = input("숫자 5개를 입력해주세요 : ").split(" ")      ##문제 4
##num1 = int(num[0])
##num2 = int(num[1])
##num3 = int(num[2])
##num4 = int(num[3])
##num5 = int(num[4])
##print(f"{(num1+num2+num3+num4+num5)/5:.3f}")


##Str = input("문자열을 입력해주세요 : ")
##split_str = Str.split(" ")
##Str1 = Str[0]
####print(Str.upper())
##print(Str1)
##print(Str1.upper())


##Str = "h ello world!"
##str1, str2, str3 = Str.split(" ")
##print(str1.upper()+str2, str3)


##Str = input("문자열을 입력해주세요 : ")
##str1, str2 = (Str.split(" "))
##str3 = str1[0]
##str4 = str2[0]
##print(str3.upper()+str1[1:], str4.upper()+str2[1:])


##num1 = float(input("첫 번째 숫자 입력 : "))
##num2 = float(input("두 번째 숫자 입력 : "))
##print(f"num1 > num2 = {num1 > num2}")
##print(f"num1 < num2 = {num1 < num2}")
##print(f"num1 >= num2 = {num1 >= num2}")
##print(f"num1 <= num2 = {num1 <= num2}")
##print(f"num1 == num2 = {num1 == num2}")
##print(f"num1 != num2 = {num1 != num2}")














