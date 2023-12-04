# Like bubbles on water, each element
# from the bottom will be popped upto
# its right position

# We compare each element to the next one, so in one iteration the bigest
# one will reach the end
# So we will run the child loop till
# size-i-1 since the alrady sorted elements
# need not be compared

arr = [4, 89, 25, 3, 7, 20, 65]
size = len(arr)

for i in range(size - 1):
    for j in range(size - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array is:", arr)
