num=int(input("enter no of terms in a series:"))
f1,f2=0,1
print("fibonacci sequence")
print(f1,f2,sep='\n')
for i in range(2,num+1):
    f=f1+f2
    f1=f2
    f2=f
    print(f)