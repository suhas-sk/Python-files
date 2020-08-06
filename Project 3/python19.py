# Insertion sort
def insertion_Sort(arr):

    for i in range(1,len(arr)):
         key = arr[i]

         # moving elements on arr[0,1,2] to one position ahead from their current position that are greter than the key
         j = i-1
         while j>=0 and  key<arr[j]:
             arr[j+1] = arr[j]
             j -= 1
         arr[j+1] = key

arr=[1, 2, 4, 9, 3, 7, 11,0]
insertion_Sort(arr)
print(arr)


