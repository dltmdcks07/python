##s = "시간을달려서" 
##n = len(s)
##for y in range(n):
##    for x in range(n):
##        if y <= x and y <=n-1-x or y>=x and y>= n-1-x:
##            print(s[x], end="")
##        else:
##            print("  ", end="")
##    print()


##s= "테두리를만들자"
##n=7
##for y in range(n):
##    for x in range(n):
##        if y ==0 or y == n-1 or x == 0 or x == n-1:
##            print(s[(x+y)%len(s)],end="")
##        else:
##            print("  ",end="")
##    print()


##s= "빙글빙글돌아가는파이썬"
##n=15
##for y in range(n):
##    for x in range(n):
##        min_dist = min(y,x,n-1-y,n-1-x)
##        print(s[min_dist % len(s)], end=" ")
##    print()



##s= "문자열로V자그리기"
##rows =5
##for y in range(rows):
##    for x in range(len(s)):
##        if y ==0 or y ==rows-1:
##            if x % (2*rows-2) ==y:
##                print(s[x], end ="")
##            else:
##                print(" ",end="")
##        elif x % (2 * rows -2)==y or x%(2 * rows -2) == (2 * rows -2 -y):
##            print(s[x],end="")
##        else:
##            print(" ", end="")
##    print()



##s1= "파이썬은 즐거워"
##s2 = "파이썬은 재밌어"
##common =""
##for letter1 in s1:
##    for letter2 in s2:
##        if letter1 == letter2 and letter1 not in common:
##            common +=letter1
##print(f"공통문자: {common}")


##s = "AABBCCCC"
##compressed = ""
##i=0
##while i< len(s):
##    count =1
##    for j in range(i+1,len(s)):
##        if s[j] == s[i]:
##            count +=1
##        else:
##            break
##    if count >1:
##        compressed +=str(count) + s[i]
##    else:
##        compressed +=s[i]
##    i +=count
##print(f"압축된 문자열: {compressed}")


##s = "ABABABABABA"
##pattern = "ABA"
##for i in range(len(s) - len(pattern)+1):
##    match = True
##    for j in range(len(pattern)):
##        if s[i+j] != pattern[j]:
##            match = False
##            break
##    if match:
##        print(f"패턴 발견 위치: {i}")


##Input = input("영어로 문자열을 입력해주세요. : ")      #포기
##i=0
##for i in range (len(Input)):
##    
##    common =""
##    for letter1 in Input:
##        for letter2 in Input:
##            if letter1 == letter2 and letter1 not in common:
##                common +=letter1
##print(f"공통문자: {common}")


##Input = input("영어로 문자열을 입력해주세요. : ")
##List= []
##for i in Input:
##    if i not in List:
##        if Input.count(i)>1:
##            print(f"{i}: {Input.count(i)}")
##        List.append(i)


##count =5
##while count > 0:
##    print(count)
##    count -= 1
##for count in range(5,0,-1):
##    print(count)


##i=2
##while i <=10:
##    print(i)
##    i+=2
##for i in range(2,11,2):
##    print(i)


##num_list = [10,20,30,40,50]
##print("num_list : ",num_list)
##print("num_list의 길이 : ",len(num_list))
##
##test_list = ["하나",2,3.0]
##print(test_list[0], type(test_list[0]))
##print(test_list[1], type(test_list[1]))
##print(test_list[2], type(test_list[2]))


##sample = [1,1,2,3,5,8,13,21,34,55,89,144]
##print(sample[1])
##print(sample[-1])
##print(sample)
##print(sample[0:len(sample)])
##print(sample[::-1])
##
##txt = list("테스트 중")
##print(txt)
##txt[4] = "끝"
##print(txt)


##sample = []
##sample1 = list()
##sample2 = list("예시문장입니다.")
##print(sample)
##print(sample2[2:4])
##print(sample2[1:5:2])


##phone = [[1,2,3],[4,5,6,],[7,8,9],["#",0,"*"]]
##print(phone)
##print(phone[0])
##print(phone[1])
##print(phone[2])
##print(phone[3])
##print(phone[0][0])
##print(phone[1][1])
##print(phone[2][0])
##print(phone[3][1])


####for i in range(3,21,3):
####    print(i)
##i=3
##while(i <21):
##    print(i)
##    i+=3


##dan =7
##i=9
####while i>=1:
####    print(f"{dan} * {i} = {dan*i}")
####    i -=1
##for i in range(9,0,-1):
##    print(f"{dan} * {i} = {dan*i}")



####import random
####count = 10
####while count >0:
####    count -=2
####    num = random.randint(1,10)
####    if num == 7:
####        print("7이 나와서 중간에 ",end="")
####        break
####    print(num)
####print("종료합니다.")
##import random
##for i in range(10,0,-2):
##    num = random.randint(1,10)
##    if num == 7:
##        print("7이 나와서 중간에 ",end="")
##        break
##    print(num)
##print("종료합니다.")



####import random
####i=1
####even_count =0
####while i<=10:
####    num = random.randint(1,50)
####    if num % 2 ==0:
####        even_count +=1
####        print(f"{i}번째: {num} (짝수)")
####    i+=1
####print("짝수 개수:", even_count)
##import random
##even_count=0
##for i in range(1,10+1,1):
##    num = random.randint(1,50)
##    if num % 2 ==0:
##        even_count +=1
##        print(f"{i}번째: {num} (짝수)")
##print("짝수 개수:", even_count)


##test = [1,2,3]
##print(test[2])
##test.append(4)
##print(test)
##del test[1]
##print(test)


##animals = ["고양이","너구리","강아지","사자"]
##search = input("동물 이름을 입력하세요 :")
##if search in animals:
##    print("해당 동물이 리스트에 있습니다.")
##else:
##    print("해당 동물이 리스트에 없습니다.")


##test = [1,2,3]
####test[3] =4
##test.insert(0,5)
##print(test)
##test.remove(2)
##print(test)
##temp = test.pop(2)
##print(temp,test)


##List = [3,4,5,6,7]
##print(f"리스트 안에 {List}이 있습니다.")
##
##
##array= []
##for i in range(1,3+1):
##    Input = input("데이터를 입력해주세요 : ")
##    array.append(Input)
##print(array)


##alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWYXZ")
##print(alphabet)
##char_6 = alphabet.pop(6)
##print(char_6)
##print(alphabet)


##alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWYXZ")
##index_ch = alphabet.index("B")
##print(index_ch, alphabet[index_ch])
##ch = input("알파벳을 입력하세요: ")
##index_ch = alphabet.index(ch)
##print(ch,"는",index_ch+1,"번째 알파벳",sep ="")


##Input = input("문자열을 입력해주세요 : ")         #문제1
##i = len(Input)
##while True:
##    print(Input[i-1], end="")
##    i -=1
##    if i ==0:
##        break


####List=[]
####for i in range(1,100+1):
####    List.append(i)
####print(List)



##List=[]
##for i in range(1,100+1):
##    List.append(i)
##    
##for i in range(100+1,1,-1):
##    if i%2==0 and i != 2:
##        List.remove(i)
##del List[0]
##print(List)


##List=[]
##for i in range(1,100+1):
##    List.append(i)
##    
##for i in range(100+1,1,-1):
##    if i%2==0 and i != 2 or i%3==0 and i!=3:
##        List.remove(i)
##del List[0]
##print(List)


##List=[]
##for i in range(1,100+1):
##    List.append(i)
##    
##for i in range(100+1,1,-1):
##    if i%2==0 and i != 2 or i%3==0 and i!=3 or i%5 ==0 and i!=5:
##        List.remove(i)
##del List[0]
##print(List)


##List=[]
##for i in range(1,100+1):
##    List.append(i)
##    
##for i in range(100+1,1,-1):
##    if i%2==0 and i !=2 or i%3==0 and i !=3 or i%5 ==0 and i!=5 or i% 7==0 and i !=7:
##        List.remove(i)
##del List[0]
##print(List)



##List=[]                                                   #포기
##for i in range(2,100+1):
##    List.append(i)
##for i in List:
##    for j in range(2,i):
##        if i % j ==0:
##            List.remove(i)
##
##print(List)


##List = []
##for i in range(2,100+1):
##    List.append(i)
##for i in List[2:]:
##    for j in range(2,i):
##        if i % j ==0:
##            List.remove(i)
##            break
##print(List)



##while True:       ##문제 8
##    print("1.추가 2.삭제 3.확인 4.종료 : ", end="")
##    Input = int(input())
##    if Input ==4:
##        break

List=[]

while True:
    print("1.추가 2.삭제 3.확인 4.종료 : ", end="")
    Input = int(input())
    if Input ==1:
        A = input("추가할 문자열을 입력해주세요: ")
        List.append(A)
        print(List)
    if Input ==2:
        List.remove()
    if Input ==4:
        break



















