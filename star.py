# for i in range (1,21):
#     print("* ", end ="")
# -----------------------

# n = int(input("Nhap n:"))
# for i in range (1, n+1):
#     print("* ", end= "")
# -------------------------    

# for i in range(1):
#     print("x *"*4,end=" ")
#     print("x")
# ----------------------------

n= int(input("Nhap n :"))
if n%2 ==0:
    a= int(n/2)
    for i in range (1):
        print("x * " *a, end="")
else:
    b=int((n+1)/2)
    for i in range(1):
        print("x * " *b, end="")
        print("x")
# ------------------------------

# for i in range(3):
#     for x in range(7):
#         print("*", end="")
#     print()
# ---------------------

# n = int(input("Nhap so cot: "))
# m = int(input("Nhap so hang: "))
# for m in range (1, m+1):
#     for n in range (1, n+1):
#         print("*", end = "")
#     print()    
# ------------------------------