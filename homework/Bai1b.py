# sheep =[5, 7, 300, 90, 24, 50, 75]
# print ("My name is Minh and these are my sheeps sizes: ",sheep)
# maxweight = max(sheep)
# print ("Now my biggest sheep has size ",maxweight ,"let's shear it")
# index = sheep.index(maxweight)
# sheep.insert(index, 8)
# sheep.remove(maxweight)
# print("After shearing, here is my flock: ",sheep)
# sheep = [x+50 for x in sheep]
# print("One month hass passed, now here is my flock: ", sheep)
# -----------------------------------------------------------------------------

# sheep =[5, 7, 300, 90, 24, 50, 75]
# print ("My name is Minh and these are my sheeps sizes: ",sheep)
# for i in range (1,4):
#     sheep = [x+50 for x in sheep]
#     print('MONTH',i)
#     print("One month hass passed, here is my flock: ", sheep)
#     maxweight = max(sheep)
#     print("Now my biggest sheep has sized",maxweight,"let shear it")
#     index = sheep.index(maxweight)
#     sheep.insert(index, 8)
#     sheep.remove(maxweight)
#     print("After shearing, here is my flock: ",sheep)

# -----------------------------------------------------------------------

sheep =[5, 7, 300, 90, 24, 50, 75]
print ("My name is Minh and these are my sheeps sizes: ",sheep)
maxweight = max(sheep)
print ("Now my biggest sheep has size ",maxweight ,"let's shear it")
index = sheep.index(maxweight)
sheep.insert(index, 8)
sheep.remove(maxweight)
print("After shearing, here is my flock: ",sheep)
for i in range (1,3):
    sheep = [x+50 for x in sheep]
    print('MONTH:',i)
    print("One month hass passed, here is my flock: ", sheep)
    maxweight = max(sheep)
    print("Now my biggest sheep has sized",maxweight,"let shear it")
    index = sheep.index(maxweight)
    sheep.insert(index, 8)
    sheep.remove(maxweight)
    print("After shearing, here is my flock: ",sheep)
sheep=[x+50 for x in sheep]
print("MONTH 3: ")
print("One month hass passed, now here is my flock: ",sheep)
print("My flock has sized in total: ",sum(sheep))    
money = sum(sheep) * 2
print("i would get",sum(sheep),"*2$ = ",money,"$")
    
  

