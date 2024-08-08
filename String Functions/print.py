
def ls(arr,key,size):
    if(size==0):
        return -1
    elif(arr[size-1]==key):
        return size
    else:
        return ls(arr,key,size-1)
aman=[]
for i in range(5):
    aman.append(int(input()))
m=int(input(" the number to find "))
a=ls(aman,m,len(aman))    
if(a==-1):
    print("the number not found ")
else:
    print("the number is found at",a)