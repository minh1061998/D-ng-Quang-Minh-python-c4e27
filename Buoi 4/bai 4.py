print('Answer the following algebra question: ')
print("If x = 8, then what is the value of 4(x+3)")
ca = 0
ls=[]
choice ={
    '1.':35,
    "2.":36,
    "3.":40,
    "4.":44
}
for i, j in choice.items():
    print(i,j)
n = int(input("Your choice: "))
if n == 4:
    print("Bingo")
    ca+=1  
else:
    print(":(")  
    
print("Estimate this answer (exact calculation not needed): ")
print("Jack scored these mark in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")

choice2 ={
    '1.':'About 55',
    '2.':'About 65',
    '3.':'About 75',
    '4.':'About 85'
}
for x,y in choice2.items():
    print(x,y)
n2 =int(input("Your choice: "))
if n2==2:
    print("Bingo")
    ca+=1
else:
    print(":(")    
ls.append(choice)
ls.append(choice2)    
print("Your correct answer",ca,"out of",len(ls),"questions")

