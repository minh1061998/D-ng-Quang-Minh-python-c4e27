def get_even_list(l):
    l2=[]
    for i in range(len(l)):
        if l[i]%2==0:
            l2.append(l[i])
    return l2        
get_even_list([1,2,3,4,5,6])
print(get_even_list([1,2,3,4,5,6]))