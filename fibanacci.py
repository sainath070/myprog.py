n = int(input("Enter a number :"))
f1 = 0
f2 = 1
print("fibanacci serise :")
print(f1,f2,sep="\n")
for i in range(2,n+1):
    f=f1+f2
    f1=f2
    f2=f
    print(f)