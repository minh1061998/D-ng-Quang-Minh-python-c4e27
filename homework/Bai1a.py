
clothlis = ['T-shirts', 'Sweater' ]
print("K.Show items")
print("C.Insert items")
print("U.Update items")
print("D.Delete items") 

while True:
    button = input("Welcome to our shop, what do you want? ") 
      
    if (button == "K"):
        print ((clothlis))
    elif (button == "C"):
        add = input("Insert item: ")
        clothlis.append(add)
        print((clothlis))
    elif (button == "U"):
        pos = int(input("Update position: "))
        new = input("New item: ")
        if pos<=len(clothlis):
            clothlis[pos-1]=new
            print(clothlis)
    elif (button=="D"):
         pos2 = int(input("Delete position: "))
         
         if pos2<=len(clothlis):
            del clothlis[pos2]
            print(clothlis)
          

         

    
     
     

