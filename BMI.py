h =float(input("Nhap vao chieu cao: "))
h1 = h*0.01
w =float(input("Nhap vao can nang: "))
bmi = w/(h1*h1)
print("Chi so BMI: ",bmi)

if bmi<16:
    print("Severly underweight")
elif 16<=bmi<18.5:
        print("Underweight")
elif 18.5<=bmi<25:
        print("Normal")
elif 25<=bmi<30:
        print("Overwieght")
else: print("Obese")                    
