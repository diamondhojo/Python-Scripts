def bubbleSort(arr):
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i]>arr[i+1]:
                x = arr[i]      #stores the first number in comparison temporarily
                arr[i] = i+1    #overwrites the first number as the second number
                arr[i+1] = x    #overwrites the second nubmer as the first nubmer

arr = [4,1,8,5,10,3,9]

print("Original: " + str(arr))
bubbleSort(arr)
print("Sorted array is: " + str(arr))
