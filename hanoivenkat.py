def hanoi(n,source,target,auxiliary):
    if n==1:
        print(f"move disk 1 from{source} to {target}")
    else:
        hanoi(n-1,source,auxiliary,target)
        print(f"move disk{n} from {source} to {target}")
        hanoi(n-1,auxiliary,target,source)
n=int(input("enter no of disks;"))
hanoi(n,'A','C','C')