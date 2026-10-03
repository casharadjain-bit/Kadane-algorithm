def max_front(n):
    arr=[1]*n + [-1]
    current=best=arr[0]
    for x in arr[1:]:
        if current<0:
            current=x
        else:
            current=current+x
        if current>best:
            best=current
    return best

print("sub arrray in 3",max_front(3))
print("sub array in 4",max_front(4))


