def is_inside(l1,l2):
    if(list(l2)[0]<list(l1)[0]<(list(l2)[2]+list(l2)[0]) and list(l2)[1]<list(l1)[1]<(list(l2)[3]+list(l2)[1])):
        return True
    else: 
        return False    
   
if is_inside([200,120],[140,60,100,200]):
    print("Điểm nằm trong hcn ")
else:
    print("Điểm k nằm trong hcn")    

#diem1(x1,y1)
#hcn(x2,y2,rong,cao)
#x2<x1<rong
#y2<y1<cao