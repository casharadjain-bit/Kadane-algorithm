def max_after(n):
    arr=[-n]+[1]*n
    current=best=arr[0]
    for x in arr[1:]:
        if current<0:
            current=x
        else:
            current+=x
        if current>best:
            best=current

    return best

print("sub array in 3",max_after(3))
print("sub array in 4",max_after(4))
