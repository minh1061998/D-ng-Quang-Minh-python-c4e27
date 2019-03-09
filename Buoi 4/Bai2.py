prices={
    'banana':4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
stock={
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
for i in prices:
    print(i)
    print('price: ',prices[i])
    print('stock: ',stock[i])

for x in stock:
    print(x)
    print('price: ',prices[x])
    print('stock:', stock[x])

total = 0
for i in prices:
    t=prices[i]*stock[i]
    print('Total of: ',i,'is: ',t)
    total = total +t
print('All: ',total)
# print('apple')
# print('price:',prices['apple'])
# print('stock:', stock['apple'])
# print('pear')
# print('price:',prices['pear'])
# print('stock:', stock['pear'])