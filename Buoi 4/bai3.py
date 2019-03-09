print('Answer the following algebra question: ')
print("If x = 8, then what is the value of 4(x+3)")
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
else:
    print(":(")  
    

       