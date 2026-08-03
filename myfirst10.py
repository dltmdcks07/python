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


##List=[]
##while True:
##    Input =int(input("1.추가 2.삭제 3.확인 4.선택추가 5.종료 : "))
##    if Input ==1:
##        A = input("추가할 문자열을 입력해주세요: ")
##        List.append(A)
##        print(List)
##    if Input ==2:
##        i = len(List)-1
##        del List[i]
####        List.remove(A)
##        print(List)
##    if Input ==3:
##        print(List)
##    if Input ==4:
##        B = input("추가할 문자열을 입력해주세요: ")
##        C = int(input("추가할 위치를 입력해주세요: "))
##        List. insert(C,B)
##        print(List)
##    if Input ==5:
##        break
##    print()


##list1 = ['H','E','L','L','O']
##tuple1=()
##tuple2 = ('혼자',)
##tuple3 = (5,6,7)
##tuple4 = tuple(list1)
##
##print(tuple2[0])
##print(tuple4[1:3])
##print(len(tuple3))


##list1 = ['G','O']
##tuple1 = ('안','녕')
##str1 = 'Bye'
##l1,l2 = list1
##t1,t2 = tuple1
##s1,s2,s3 = str1
##print(l1,l2, sep = '>')
##print(t1,t2, end ='!')
##print(s3,s2,s1, sep='-')


##empty_tuple = ()
##single_tuple = (10,)        #요소가 1개일때 쉼표 왜?
##print(single_tuple)
##multi_tuple = (10,20,30)
##print(multi_tuple)


##n_tuple = (10,20,30,40,50)
##n_tuple[0] = 100
##del n_tuple[0]


##t= tuple(range(5))
##print(t)
##t2= tuple(range(9,20))
##print(t2)
##t3 = tuple(range(-10,5,2))
##print(t3)
##
##t= 10,20,30,40
##print(t,type(t))
##t2 = 10,"이십",30,40
##print(t2,type(t2))


##single_tuple=(3,)
##print(single_tuple)
##
##
##t = tuple(range(0,9,2))
##print(t)


##lunch = ("샐러드", "햄버거","돈까스","뷔페")
##dinner = ("만두","국밥","초밥","마라탕")
##menu = lunch +dinner
##dinner = dinner[3:]+("삼겹살",)+dinner[:1]
##
##print(menu)
##print(dinner)


##fruits = ('사과','귤','파인애플','메론')
##reverse_fruits = fruits[::-1]
##print(reverse_fruits)
##snack = ('감자칩','새우깡','초콜렛')
##print(snack)
##potato, shrimp, chocolate = snack
##print(potato)
##print(shrimp)
##print(chocolate)


##snack = ('감자칩','새우깡','초콜렛')
##print(snack, type(snack),sep="\n")
##list_snack = list(snack)
##print(list_snack, type(list_snack),sep = "\n")


##t1 = (10,20,30,40,50)
##t2 = (1,2,3,4,5)
##t3 = t1+t2
##t4=t1*2
##print(t3)
##print(t4)


##tuple1 = (5,6,7,5,9,5,7)
##c1 = tuple1.count(5)
##print(c1)


##tuple1 = (11,34,87,523)
##num1 = tuple1.index(87)
##print(num1)


##ice2 = ("메로나","메로나","엔초","민트초코","호두마루")
##print(ice2)
##tmp = ice2.count("메로나")
##print("메로나가 {0}개 있습니다." .format(tmp))


##ice = ("죠스바","메로나","돼지바","호두마루")
##txt = "메로나가 "
##txt+=f"{ice.index("메로나")+1}번째에 있습니다."
##print(txt)
##print("ice에 총", len(ice),"개 있습니다.")


##Tuple = (11,22,31,44,23,59)
##print("31은 {0}번째에 있습니다.".format(Tuple.index(31)))


##fruits = ('사과','귤','파인애플','메론')
##reverse_fruits = fruits[::-1]
##print(reverse_fruits)
##snack = ('감자칩','새우깡','초콜렛')
##print(snack)
##potato, shrimp, chocolate = snack
##print(potato)
##print(shrimp)
##print(chocolate)


##ice2 = ("메로나","메로나","엔초","민트초코","호두마루")
##List = list(ice2)
##for i in List[1::2]:
##    print(i)


##multi_tuple = ('a','b','c')
##print(multi_tuple)
##multi_tuple = multi_tuple[0:1] + ("B",) + multi_tuple[2:]
##print(multi_tuple)


##empty = set()
##s = {1,2,3,5,7,11,13,17,19}
##print(s)
##s = set([3,4,5,2,1,2,2,3,6,4,5])
##print(s)


##s = {6,3,7,2,9}
##print(s)
##s.add(8)
##s.add(6)
##print(s)
##s.remove(7)
##print(s)


##s = {1,2,3,4,5}
##print(s)


##import random
##empty = set()
##for i in range(20):
##    a= random.randint(1,20)
##    empty.add(a)
##print(empty)


##empty_2 = set()
##empty_3 = set()
##empty_5 = set()
##i=0
##for i in range(30+1):
##    if i%2==0:
##        empty_2.add(i)
##    if i%3==0:
##        empty_3.add(i)
##    if i%5==0:
##        empty_5.add(i)
##print(empty_2)
##print(empty_3)
##print(empty_5)


##set1 = {9,4,6,2,1}
##print(set1)
##if 6 in set1:
##    print("set1안에 6이 있습니다.")
##if 10 in set1:
##    print("set1안에 10이 있습니다.")
##for el in set1:
##    if el % 2 ==0:
##        print(el)
    
    
##set1 = {9,4,6,2,1}
##set2 = {8,4,7,3,2}
##
##set5 = set1.difference(set2)
##print(set5)
##
##set6 = set2.difference(set1)
##print(set6)


##set1 = {9,4,6,2,1}
##set2 = {8,4,7,3,2}
##set3 = set1.union(set2)
##print(set3)
##set4 = set1.intersection(set2)
##print(set4)


##set1 = {'가','나','다','라'}
##set2 = {'가','나','다'}
##if set2.issubset(set1):
##    print("set1안에 set2를 포함!")
##if set1.issuperset(set2):
##    print("set2는 set1에 포함!")


##set1 = {1,3,2,5,7}
##set2 = {3,8,4,5}
##
##print("집합1의 구성", set1)
##print("집합2의 구성", set2)
##print()
##print(set1.union(set2))
##print(set1.intersection(set2))
##print("집합1 - 집합2 차집합",set1.difference(set2))
##print("집합2 - 집합1 차집합",set2.difference(set1))


##set1 = {1,3,2,5,7}
##set2 = {3,8,4,5}
##
##print("집합1의 구성", set1)
##print("집합2의 구성", set2)
##print()
##print(set1.union(set2))
##print(set1.intersection(set2))
##print("집합1 - 집합2 차집합",set1.difference(set2))
##print("집합2 - 집합1 차집합",set2.difference(set1))


##set1 = {1, 3, 2, 5, 7}
##set2 = {3, 8, 4, 5}
##
##print("집합1의 구성", set1)
##print("집합2의 구성", set2)
##print()
##
##if set1.issubset(set2):
##    print("집합1은 집합2의 부분집합입니다.")
##else:
##    print("집합 1은 집합 2에 포함되지 않음")
##    
##if set2.issubset(set1):
##    print("집합2는 집합1의 부분집합입니다.")
##else:
##    print("집합 2는 집합 1에 포함되지 않음")
##print()
##
##setA = set1.difference(set2)
##setB = set2.difference(set1)
##print("대칭차집합",setA.union(setB))



##set1 = set()
##Input = input("문자열을 입력해주세요: ")
##
##for i in Input:
##    if 'a' <= i <= 'z':
##        set1.add(i)
##    elif 'A' <= i <='Z':
##        set1.add(i)
##print(set1)


##List1 = [1,2,4,8,16]
##List2 = [1,2,3,4,5]
##set1 = List1
##set2 = List2
##List3 = set1.union(set2)
##print(List3)




##List1 = [1, 2, 4, 8, 16]
##List2 = [1, 2, 3, 4, 5]
##print("리스트1의 구성", List1)
##print("리스트2의 구성", List2)
##print()
##set1 = set(List1)
##set2 = set(List2)
##setA = set1.difference(set2)
##setB = set2.difference(set1)
##print("리스트3",list(setA.union(setB)))

##empty = set()
##i=0
##while True:
##    Input = int(input("1~30사이의 숫자를 입력해주세요: "))
##    if Input >30:
##        print("다시 입력해주세요.")
##        
##    else:
##        empty.add(Input)
##        i+=1
##    if i<=5:
##        break
##print(empty)
        




##empty = set()
##
##while True:
##    if len(empty) == 5:
##        break
##        
##    Input = int(input("1~30사이의 숫자를 입력해주세요: "))
##    
##    if Input < 1 or Input > 30:
##        print("다시 입력해주세요.")
## 
##    elif Input in empty:
##        print("다시 입력해주세요.")
##
##    else:
##        empty.add(Input)
##
##print("최종 입력된 숫자:", empty)





























