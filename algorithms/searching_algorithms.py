#Searching Algorithms
print("Searching Algorithms")
Numarray=[25,27,2,0,9,42,3,12,8,3]
print(Numarray)

#Linear search Algorithm
def linear_search_algo(target,array):
    array_length=len(array)
    print("Array length: ",array_length)
    if array_length >= 1:
        if target in array:
            for i in range(array_length):
                if array[i]==target:
                    print("Element is found at index ",i)
                    return i
        else:
            print("Element is not found")
                
#print("Linear Search Algorithm")        
#linear_search_algo(3,Numarray)  
#linear_search_algo(16,Numarray)

#Binary search Algorithm
def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
         
sorted_array = [1, 5, 9, 12, 20, 26, 32, 45, 56, 78, 88, 99, 120]
print(sorted_array)

def iterative_binary_search_algo(list, target):
    print("target ",target)
    first = 0
    last = len(list) - 1
    if target in list:
        while first <= last:
            midpoint = (first + last)//2
            print("midpoint ",list[midpoint])
            if list[midpoint] == target:
                print("index ",midpoint)
                return midpoint
            elif list[midpoint] < target:
                print("the target is greater than the midpoint")
                first = midpoint+1
            else:
                print("the target is smaller than the midpoint")
                last = midpoint-1
    else:
        print("element not found")
        return -1
#print("Iterative Binary Search Algorithm") 
#iterative_binary_search_algo(sorted_array,200)


def recursive_binary_search_algo(list, target, start=0, end=None):
    print("target ",target)
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1
    if target in list :
        mid = (start + end) // 2
        print("midpoint ",list[mid])
        if target == list[mid]:
            print("index ",mid)
            return mid
        else:
            if target < list[mid]:
                print("the target is smaller than the midpoint")
                return recursive_binary_search(list, target, start, mid-1)
            else:
                print("the target is greater than the midpoint")
                return recursive_binary_search(list, target, mid+1, end)
    else:
       print("element not found")
       return -1 

#print("Recursive Binary Search Algorithm") 
#recursive_binary_search_algo(sorted_array,20)



#Simple Search Algorithm code
def search_algo(list, target):
    if target in list:
        print("target is found in index : ",list.index(target))
    else:
        print("element not found")
        return -1
#print("Simple Search Algorithm") 
#search_algo(sorted_array,20)
