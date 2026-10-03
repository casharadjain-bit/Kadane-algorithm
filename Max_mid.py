def max_mid(n):
    arr=[-1,n,-1]
    current=best=arr[0]
    for i in arr[1:]:
        if current<0:
            current=i
        else:
            current+=i
        if current>best:
            best=current

    return best

print("subarray in 3",max_mid(3))
print("subarray in 4",max_mid(4))




    
        
