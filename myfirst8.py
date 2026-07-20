##for num in range(97,104):
##    print(chr(num))
##text = "ABCDEFG"
##for character in text:
##    print(ord(character))
##text = "HelloPython"
##for character in text:
##    if character.isupper():
##        print(character.lower(),end=" ")
##    elif character.islower():
##        print(character.upper(), end=" ")
##text = "Hello World! How are you doing today?"
##vowels = "aeiouAEIOU"
##count = 0
##for char in text:
##    if char in vowels:
##        count +=1
##print(f"모음의 개수: {count}")
##text = "abcdefghijklmnopqrstuvwyxz"
##shift = 3
##shifted_text = ""
##for character in text:
##    if character.isalpha():
##        shifted_char = chr((ord(character)+shift))
##        shifted_text +=shifted_char
##print(shifted_text)



##Input = int(input("숫자 하나 입력: "))        #문제8
##total=0
##i=0
##while(1):
##    i+=1
##    total+=i
##    if Input == i:
##        break
##print("합산: ",total)



##Input = input("문장을 입력하세요: ")
##count=0
##number = "1234567890"
##for char in Input:
##    if char in number:
##        count+=1
##print("숫자의 개수: ", count)



##i=0
##for num in range(97,123):
##    if i==0:
##        print("{0}({1})".format(num,chr(num)), end=" ")
##        i=1
##        continue
##    if i==1:
##        print("{0}({1})".format(chr(num),num), end=" ")
##        i=0
##        continue
    


##Input = input("문장을 입력하세요: ")
##print("변형된 문장: ",end=" ")
##i=0
##count=0
##vowels = "aeiouAEIOU"
##
##for char in Input:
##    if char in vowels:
##        print("*",end='')
##        count+=1
##        i+=1
##        continue
##    print(Input[i],end='')
##    i+=1
##    
##print(" ")
##print("모음의 개수: ", count)
####i=3
####a="dltmdcks"
####print(a[i])



##import random
##print("추천 비밀번호:",end=" ")
##for i in range(6):
##    a= random.randint(0,1)
##    if a ==0:
##        num = random.randint(0,9)
##        print(num,end="")
##        continue
##        
##    if a==1:
##        alphabet = random.randint(ord('A'),ord('Z'))
##        print(chr(alphabet),end="")
##        continue

##for num1 in range(2):
##    print("바깥쪽 반복문")
##    for num2 in range(3):
##        print("안쪽 반복문")
##for num1 in range(0,4):
##    print(f"안쪽 : {num1}")
##    for num2 in range(0,num1):
##        print(f"\t 바깥쪽 : {num2}")
##    print("="*20)
##cnt =0
##for y in range(1,6):
##    for x in range(1,6):
##        cnt +=1
##        print(cnt)
##for hour in range(1,13):
##    for minute in range(1,61):
##        print(f"{hour}시 {minute}분")
##for day in range(1,8):
##    print(f"{day}일차")
##    for time in range(1,4):
##        if time==1:
##            print("아침",end=" ")
##        if time ==2:
##            print("낮",end=" ")
##        if time==3:
##            print("밤")
##for y in range(5):
##    sentence = ' '
##    for x in range(5):
##        sentence +=str(y)
##    print(sentence)
##for y in range(1,5):
##    pyramid=''
##    for x in range(y):
##        pyramid +=str(y)
##    print(pyramid)
##i=1
##txt=''
##while i<4:
##    j=1
##    txt+=f"{i}학년 "
##    while j<6:
##        txt+=f"{j}반 "
##        j+=1
##    i+=1
##    txt+="\n"
##print(txt)
##num=10
##cnt=0
##for y in range(1,num+1):
##    for x in range(1,num+1):
##        cnt +=1
##        print(cnt,end=' ')
##    print()
##num = int(input("숫자를 입력해주세요 : "))
##cnt =0
##for y in range(1, num+1):
##    for x in range(1,y):
##        cnt+=1
##        print(cnt,end=' ')
##    print()
##for y in range(5):
##    for x in range(5):
##        print(chr(ord('A')+x+y),end=" ")
##    print()
##string = "abcd"
##for y in range(len(string)):
##    for x in range(y,len(string)):
##        print(string[y:x+1])


















