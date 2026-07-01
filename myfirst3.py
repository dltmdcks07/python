##num1 = float(input("첫 번째 숫자 입력: "))
##num2 = float(input("두 번째 숫자 입력: "))
##print(f"num1 > num2 = {num1 > num2}")
##print(f"num1 < num2 = {num1 < num2}")
##print(f" num1 >= num2 = {num1 >= num2}")
##print(f" num1 <= num2 = {num1 <= num2}")
##print(f" num1 == num2 = {num1 == num2}")
##print(f" num1 != num2 = {num1 != num2}")
##num = int(input(" 숫자 입력: "))
##print(f"{num < 100}")
##num = int(input(" 숫자 입력: "))
##print(f"{30<=num<=60}")

##num1 = 15
##if num1 ==15:
##    print("이 숫자는 15입니다")
##num1 = 15
##if num1 != 15:
##    print(" 이 숫자는 15가 아닙니다. ")
##print("위 문장은 출력되지 않습니다.")

##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##print(f"둘 다 양수? =  {num1>0 and num2 > 0}")
##print(f"하나라도 양수? = {num1 > 0 or num2 > 0}")
##print(f" num1은 0인가? = {not num1}")
##print(f" num2은 0인가? = {not num2}")
##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##print(f"""둘 다 0이 아니고 곱하면 양수인가?
##={num1 != 0 and num2 != 0 and num1*num2 > 0}""")
##print(f"""num1, num2 또는 둘의 합이 10의 배수인가?
##={num1 % 10 == 0 or num2 % 10 ==0 or
##(num1 + num2) %10 == 0}""")

##num = int(input("숫자 입력: "))
##print( num ==0 or num ==10 or num ==100)

##num = int(input("숫자 하나 입력: "))
##print(f"{num !=0 and num%2!=0 or num%8==0}")

##str1 = "Python is Simple"
##if "is" in str1:
##    print("이 문장에는 is가 있음.")
##level = int(input("레벨을 입력해 주세요 : "))
##if level >= 10:
##    print("현재 레벨은 10을 넘습니다.")
##if level <= 20:
##    print("현재 레벨은 20보다 작습니다.")
##level = int(input("레벨을 입력해 주세요: "))
##if level ==15:
##    print("현재 레벨은 15입니다.")
##if level !=15:
##    print("현재 레벨은 15가 아닙니다.")
##level = int(input("레벨을 입력해주세요: "))
##if level >10:
##    print("현재 레벨은 10을 넘습니다.")
##if level <20:
##    print("현재 레벨은 20보다 작습니다.")
##print("loding...")
##answer = "이샘_코딩_학원"
##word = input("단어를 입력해주세요 : ")
##if word in answer:
##    print("해당 단어가 포함되어 있습니다.")
##if word not in answer:
##    print("해당 단어가 포함되어 있지 않습니다.")
##level = int(input("레벨을 입력해 주세요: "))
##if level <30:
##    print("레벨이 모자릅니다.")
##if 30<= level <+40:
##    print("적정 레벨입니다.")
##if level >40:
##    print("레벨이 너무 높습니다.")
##level = int(input("레벨을 입력해주세요: "))
##if level <10:
##    print("씨앗 레벨입니다.")
##if level > 10 and level <=25:
##    print("새싹 레벨입니다.")
##if level >25 and level <=40:
##    print("꽃 레벨입니다.")
##if level >40 and level <60:
##    print("나무 레벨입니다.")
##month = int(input("몇 월인지 입력해주세요 :"))
##if month >=3 and month <=5 :
##    season = "봄"
##if month >=6 and month <=8 :
##    season = "여름"
##if month >=9 and month <=11 :
##    season = "가을"
##if month ==12 or month <=2 :
##    season = "겨울"
##print(f"지금 계절은 {season}입니다.")
##number = int(input("숫자를 입력해주세요: "))
##if number %3 ==0 or number %5 ==0:
##    print("{}는 3이나 5의 배수입니다.".format(number))


##number = int(input("숫자를 입력해주세요."))        문제 1
##if number %2==0:
##    print(f"{number}는 짝수입니다.")
##tem = int(input("온도를 입력해주세요: "))
##print("날씨 상태: ", end='')
##if tem <25:
##    print("시원한 날씨")
##if tem >=25 and tem <30:
##    print("따뜻한 날씨")
##if tem >=30:
##    print("더운 날씨")
##Str = input("문자열을 입력하세요: ")
##if ' ' in Str:
##    print("공백이 포함되어 있습니다.")
##if ' ' not in Str:
##    print("공백이 포함되어 있지 않습니다.")
##year = int(input("나이를 입력하세요: "))
##if year >=15:
##    print("15세 관람가")
##if year >=12:
##    print("12세 관람가")
##print("전체 관람가")
##number =3
##if number ==15:
##    print("이 숫자는 15입니다.")
##else:
##    print("이 숫자는 15가 아닙니다.")
##number =3
##if number ==15:
##    print("이 숫자는 15입니다.")
##elif number ==3:
##    print("이 숫자는 3입니다.")
##else:
##    print("이 숫자는 3도 15도 아닙니다.")
##apple = int(input("사과의 개수를 입력해주세요:"))
##if apple >0:
##    print("사과가 있습니다.")
##else:
##    print("사과가 없습니다.")
##apple = int(input("사과의 개수를 입력해주세요:"))
##if apple ==10:
##    print("사과는 10개 있습니다.")
##elif apple ==0:
##    print("사과는 하나도 없습니다.")
##text = input("문장을 입력하세요: ")
##if ' 'in text:
##    print("공백이 포함되어 있습니다.")
##else:
##    print("공백이 포함되어 있지 않습니다.")
##string = input("문자를 입력하세요: ")
##if string.isalpha():
##    print("알파벳 혹은 한글입니다.")
##elif string.isnumeric():
##    print("숫자입니다.")
##else:
##    print("특수 문자입니다.")
##height = 170
##if height >150:
##    print("키가 150 이상입니다.")
##if height >160:
##    print("키가 160 이상입니다.")
##height = 170
##if height >150:
##    print("키가 150 이상입니다.")
##elif height >160:
##    print("키가 160 이상입니다.")
##height = int(input("키를 입력해주세요: "))
##if height>160:
##    print("키가 160 이상입니다.")
##elif height>150:
##    print("키가 150 이상입니다.")
##else:
##    print("키가 150 미만입니다.")
##height = int(input("키를 입력해주세요: "))
##if height > 170:
##    print("키가 170 이상입니다.")
##elif height >160:
##    print("키가 160 이상입니다.")
##elif height > 150:
##    print("키가 150 이상입니다. ")
##else :
##    print("키가 150 미만입니다.")
##num1 = float(input("첫 번째 숫자: "))
##num2 = float(input("두 번째 숫자: "))
##num3 = float(input("세 번째 숫자: "))
##average = (num1 + num2+ num3)/3
##if average >= 50:
##    print("평균이 50 이상입니다.")
##else:
##    print("평균이 50 미만입니다.")
##email = input("이메일 주소를 입력해주세요: ")
##if '@' in email and '.' in email:
##    print("유효한 이메일 주소입니다.")
##elif '@' in email:
##    print("'.'가 없습니다.")
##elif '.' in email:
##    print("'@'가 없습니다.")
##else:
##    print("유효하지 않은 이메일 주소입니다.")
##url = input("URL을 입력하세요: ")
##
##if url.find("http://")>=0:
##    print("HTTP프로토콜입니다.")
##elif url.find("https//")>=0:
##    print("HTTPS 프로토콜입니다.")
##elif url.find("ftp://")>=0:
##    print("FTP 프로토콜입니다.")
##else:
##    print("알 수 없는 프로토콜입니다.")
Str = input("방향키를 입력해주세요(w/a/s/d): ")
if 'w' in Str:
    print("위 방향키를 입력하셨습니다.")
if 'a' in Str:
    print("좌 방향키를 입력하셨습니다.")
if 's' in Str:
    print("아래 방향키를 입력하셨습니다.")
if 'd' in Str:
    print("우 방향키를 입력하셨습니다.")
if 'w'not in Str:
    print("잘못 입력하셨습니다.")
    















