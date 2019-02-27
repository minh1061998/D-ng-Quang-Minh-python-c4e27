# for v in [1, 2, 3]:
#     print(v)

# for v in 'hello':
#     print(v)

# Cấu trúc vòng lặp for: for <biến đk> in <danh sách>:
#                           <các lệnh>
# Chuỗi là 1 mảng các ký tự

# for x in range (0,1000):
#     y=3*x**2+2*x+1
#     print(y)

# for v in range(1,1):
#     print(v)

# range ([start], stop, [step])

# print(list (range(10)))


# t =0
# for i in range (1,11,1): 
#     t = t + i 
# print(t)   

# tong = 0
# for i in range (1,11):
#     tong = tong + i**2
# print (tong)    
  

# for i in range (1, 11):
#     x = (i)**2 + (i+1)**2
# print (x)    

n = int(input("Nhap n:"))
tong = 0
for i in range (1,n+1):
    tong = tong + i
print (tong)    