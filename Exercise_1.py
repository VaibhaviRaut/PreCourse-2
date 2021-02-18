# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1

"""
RECURSIVE: 

def binarySearch(arr, l, r, x):
  low = l
  high = r
  # first find if the array is sorted
  if(l > r):
      return -1
  mid = int(low + (high - low) / 2)
  print("mid: ", mid)
  if arr[mid] == x:
      return mid
  elif x < arr[mid]:
      return binarySearch(arr,l,mid-1,x)
  else:                                        # elif x > arr[mid]: on the higher side of numbers
      return binarySearch(arr,mid+1,r,x)
"""
'''
ITERATIVE:
'''
def binarySearch(arr, l, r, x):
    # write your code here
    low  = l
    high = r
    while low<=high:
        mid = int(low + (high - low) / 2)
        print("mid: ", mid)
        if arr[mid]==x:
            return mid
        elif low < mid:
            if arr[mid]> x:
                high = mid - 1;
            else:
                low = mid + 1
        else:
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print ("Element is present at index ", result)
else:
    print("Element is not present in array")
