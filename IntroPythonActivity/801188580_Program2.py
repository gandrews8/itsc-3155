x = int(input("Enter lower number"))
y = int(input("Enter higher number"))
z = range(x,y+1)
print("Numbers in given range divisible by 7 but not by 5")
for n in z:
    if(n%7==0 and n%5!=0):
        print(n)
