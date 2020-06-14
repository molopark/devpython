'''
Created on 2018. 11. 8.

@author: molo
'''

'''
i = 0
j = 10
print(i+j)

#--------------------------

l1 = [1, 2, 'a', 'b']
# del l1[0]
if 3 in l1:
    print(l1)

#--------------------------

money = 2000
card = 1
if money > 5000 or card:
    print("True")
else:
    print("False")

#--------------------------

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("Taxi")
else :
    print("Walk")

#--------------------------

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#--------------------------

prompt = """
1. Add
2. del
3. List
4. Quit

Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    if number == 4:
        print("Bye~~~")
'''
#--------------------------

a = 0
while a<10:
    a=a+1
    if a%2==0: continue
    print(a)
