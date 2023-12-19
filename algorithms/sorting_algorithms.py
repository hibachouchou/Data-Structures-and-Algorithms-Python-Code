#Sorting Algorithms
print("Sorting Algorithms")

def swapp(a,b):
    if a>b:
        c=a
        a=b
        b=c
    #return a , b
    #print(a,b)
 
#swapp(15,2)


# Bubble sort Algorithm
def buble_sort_algo(array):
    array_length=len(array)
    print("Array length: ",array_length)
    if array_length > 1:
        print("Array is not empty ! ",array)
        # loop to access each array element
        for i in range(array_length):
             # loop to compare array elements
             for j in range(0, array_length - i - 1):
                 # compare two adjacent elements
                 if array[j] > array[j + 1]:
                     # swapping elements if elements
                     # are not in the intended order
                     #swapp(array[j],array[j + 1])
                     temp = array[j]
                     array[j] = array[j+1]
                     array[j+1] = temp
    print(array)

    
Numarray=[25,27,2,0,9,42,3,12,8,3]
print(Numarray)
#print("Buble Sort Algorithm")
#buble_sort_algo(Numarray)

                   
# Selection sort Algorithm
def selection_sort_algo(array):
    array_length=len(array)
  
    print("Array length: ",array_length)
    if array_length > 1:
        print("Array is not empty ! ",array)
        # loop to access each array element
        for i in range(array_length):
            # Assume the current index is the minimum
            index_min=i
            for j in range(i+1, array_length):
                # Check if the current element is smaller than the element at min_index
                if array[j]<array[index_min]:
                    index_min=j
                # Swap the found minimum element with the first element
                array[i], array[index_min] = array[index_min], array[i]
    print(array)
#print("Selection Sort Algorithm")    
#selection_sort_algo(Numarray)   

# Quick sort Algorithm
def quick_sort_algo(array):
    array_length = len(array)
    if array_length <= 1:
        return array

    else:
        pivot = array[0]
        print("pivot: ",pivot)
        hight_side = []
        low_side = []

        for i in range(1, array_length):
            if pivot >= array[i]:
                low_side.append(array[i])
                print("low_side1: ",low_side)
            elif pivot < array[i]:
                hight_side.append(array[i])
                print("hight_side1: ",hight_side)

        sorted_low = quick_sort_algo(low_side)
        print("low_side2: ",sorted_low)
        sorted_high = quick_sort_algo(hight_side)
        print("hight_side2: ",sorted_high)

        result = sorted_low + [pivot] + sorted_high
        print("Sorted Array: ",result)
        return result

#print("Quick Sort Algorithm")             
#quick_sort_algo(Numarray)

# Merge sort Algorithm
def merge_sort_algo(array):
    array_length = len(array)
    if array_length <= 1:
        return array

    else:
        midpoint_index = array_length // 2
        print("My MidPoint : ",array[midpoint_index])
        left_half = array[:midpoint_index]
        print("My Left Half1 : ",left_half)
        right_half = array[midpoint_index:]
        print("My Right Half1 : ",right_half)

        sorted_left = merge_sort_algo(left_half)
        print("My Left Half2 : ",sorted_left)
        sorted_right = merge_sort_algo(right_half)
        print("My Right Half2 : ",sorted_right)

        merged_array = merge(sorted_left, sorted_right)
        print("My Soted Array : ",merged_array)
        return merged_array

def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged
#print("Merge Sort Algorithm")
#merge_sort_algo(Numarray)

# Insertion Sort Algorithm
def insertion_sort_algo(array):
    array_length = len(array)

    if array_length <= 1:
        return array

    else:
        for i in range(1, array_length):
            key = array[i]
            j = i - 1

            while j >= 0 and key < array[j]:
                """ moves the element at index j one position to the right, creating space for the key to be inserted """
                array[j + 1] = array[j]
                """ This decrements the index j to continue checking the previous elements in the array """
                j -= 1
            """ This is the position where the key will be inserted """
            array[j + 1] = key

    print(array)
    return array 
#print("Insersion Sort Algorithm")
#insertion_sort_algo(Numarray)                  
            
