#bubble sorting
def bubble_sort(arr,size):
   for i in range(size-1):
     for j in range(size-1-i):
          if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

arr=[9,5,8,4,7,3,6]
bubble_sort(arr,len(arr))
print(arr)