import math as m

fint = int(input("insert first two-digit number under 100: "))
sint = int(input("insert second two-digit number under 100: "))
#I didn't put anything here to raise errors for bad inputs

def getfirst(x,y = 1):
    first=(x*y)//10
    return first

def getsecond(x,y = 1):
    second=(x*y)%10
    return second

ff = getfirst(fint)
fs = getsecond(fint)
sf = getfirst(sint)
ss = getsecond(sint)

line1=getfirst(ff,sf)
line2=getsecond(ff,sf)+getfirst(fs,sf)+getfirst(ff,ss)
#"carrying over" like in elementary school
print(line2)
if line2>9:
    line1 = 1 + line1
    line2 = line2 - 10
line3=getfirst(fs,ss)+getsecond(fs,sf)+getsecond(ff,ss)
print(line2)
#"carrying over" like in elementary school
if line3>9:
    line2 = 1 + line2
    line3 = line3 - 10
print(line3,line2)
line4=getsecond(fs,ss)

digits=[line1,line2,line3,line4]
answ=0

for i in range(len(digits)):
    answ = answ + digits[i]*10**(3-i)
    print(digits[i]*10**(3-i))
print(answ)
