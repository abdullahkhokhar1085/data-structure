def linearsearch(arr , target , ind):
    if ind==len(arr):
        return False
    if arr[ind] == target:
        return True
    elif arr[ind]!=target and ind<= len(arr)-1:
        return linearsearch(arr , target , ind+1)
    
arr = [1,2,3,4,5]
target = -5

print(linearsearch(arr,7,0))
