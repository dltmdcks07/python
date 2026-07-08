##result = ""
##while True:
##    word = input("단어를 입력하세요 ('end'를 입력하면 종료): ")
##    if word =="end":
##        break
##    if len(word) <3:
##        continue
##    result += word + " "
##print(f"입력된 단어들: {result}")
##while True:
##    sentence = input("10글자 이상의 문장을 입력하세요('quit'이 포함되면 종료): ")
##    if "quit" in sentence:
##        break
##    if len(sentence) <10:
##        print("10글자 미만입니다.")
##        continue
##    print(sentence[::-1])

##num = 1             #문제 1번 
##total=1
##while True:
##    if total <=5000:
##        num +=1
##        total *= num
##        continue
##    break
##print("num: ", num)
##print("total: " , total)

##num =0
##while num <49:
##    if num % 3 == 0 or num %5==0:
##        num+=1
##        continue
##    print(num, end=' ')
##    num+=1



##while True:
##    if num1 < num2-1:
##        num1 +=1
##        print(num1**2, end=' ')
##    elif num1-1> num2:
##        num2 +=1
##        print(num2**2, end=' ')


##num1 = int(input("숫자1: "))
##num2 = int(input("숫자2: "))
##start=0
##end=0
##if num1 > num2:
##    start = num2
##    end = num1
##else:
##    start = num1
##    end = num2
##while start < end-1:
##    start +=1
##    print(start **2, end=' ')



Input = input("문장을 입력해주세요: ")   #❁´◡`❁ ┬┬﹏┬┬
count=0
print("바뀐 문장: ", end=' ')
while count<len(Input):
    if count %2 ==1:
        print("■",end=' ')
    else:
        print(Input[count], end=' ')
    count +=1
        











































