#Merge sort
# sorting 2 list and merging
def Merge_Sort(arr1,arr2):
    tem=[]
    a=len(arr1)
    b=len(arr2)
    i=j=0
    while i<a and j<b:
        if arr1[i]<= arr2[j]:
            tem.append(arr1[i])
            i+=1
        else:
            tem.append(arr2[j])
            j+=1
    while i< a:
        tem.append(arr1[i])
        i += 1

    while j< b:
         tem.append(arr2[j])
         j += 1

    return tem
arr1=[4,8,19,25,45]
arr2=[9,10,16,52,99]
arr3=Merge_Sort(arr1,arr2)
print(arr3)