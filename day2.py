##string = "Python Upper Loswer"
##print(string.upper())
##print(string.lower())
##dessert = "초코케이크 녹차마카롱 모카라떼"
##cake, macaron, coffee = dessert.split(" ")
##print("[오늘 먹을 간식 목록]")
##print("케이크 :", cake)
##print("마카롱 :", macaron)
##print("커피 :", coffee)
##n1,n2 = input("int 둘 입력 : ").split()
##print(n1)
##print(n2)
##print(n1+n2)
##print(int(n1)+int(n2))
##a,b,c = input("알파벳 셋 입력: ").split()
##print(c,b,a,sep=">")

##r1,r2 = input("float 둘 입력 : ").split()
##r1 = float(r1)
##r2 = float(r2)
##print(r1*r2)
##message = """대공원에 봄 벚꽃 놀이는
##낮 봄 벚꽃 놀이보다
##밤 봄 벚꽃 놀이니라."""
##print(message.replace("벚꽃", "개나리"))
##win = "WindowXP"
##update = win.replace("XP","11")
##print(update, "로 없데이트 됐습니다.")
##japangi = """이 자판기 안에는
##포도맛 사이다,
##포도맛 쥬스,
##포도맛 슬러쉬
##가 있습니다."""
##taste = input("무슨 맛 자판기로 바꿀까요 : ")
##print(japangi.replace("포도", taste))
##message = input("영어로 문장을 적어주세요 : ")
##print(message.upper())
##print(message.lower())
##message = "abcD 1234 ..@@!!!"
##trans = message.upper()
##print(trans)


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


##string = "이 문장안에 있는 글자 수는 몇개일까요?"
##print(len(string))
##string = "파이썬 {0}번 복습하기".format(10)
##print(string)
##string2 = f"문자열도 {10:8.2f}번 복습하기"
##print(string2)
##tips = "len 함수로 문자열의 갯수를 세봅시다."
##print(len(tips))
##number = 15335
##print(len(number))
##year = input("태어난 해를 입력해주세요 : ")
##month = input("태어난 월을 입력해주세요 : ")
##day = input("태어난 일을 입력해주세요 : ")
##date = " {}년 {}월 {}일".format(year,month,day)
##print("당신의 생일은 " + date + "입니다. Happy birthday!")
##num1 = f'{10}/{20}'
##num2 = f'[{10.10}/{20.20}]'
##print(num1)
##print(num2)
##pi = 3.14
##num3 = f'[{pi:4.1f}/{pi:010.0f}]'
##print(num3)
##str1 = "Python"
##str2 = f'[{str1:10s}/{str1:010s}]'
##print(str2)


##a = input("영화 제목을 입력하세요: ")         #문제 1
##b = input("개봉 연도를 입력하세요: ")
##c = input("주연 배우를 입력하세요: ")
##print("{}은(는) {}년에 개봉한 {}의 영화입니다.".format(a,b,c))


##a = input("아이디를 입력해주세요(6글자 이상): ")          #문제 2
##print("암호화된 아이디", a[:3]+"*****")

















