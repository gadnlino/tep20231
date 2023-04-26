import math

def partition(arr, l, r):
      
    x = arr[r]
    i = l
    for j in range(l, r):
          
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
  
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
  
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)
  
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
  
        # If position is more, recur 
        # for left subarray 
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
  
        # Else recur for right subarray 
        return kthSmallest(arr, index + 1, r, 
                            k - index + l - 1)

ntests = int(input())

for __ in range(ntests):
    numbers = list(map(lambda x : int(x), str(input()).split(" ")))

    nneigh = numbers[0]
    neigh = numbers[1:]

    k = math.ceil(nneigh/2)

    kth = kthSmallest(neigh, 0, nneigh-1, k)

    dist = 0

    for n in neigh:
        dist += abs(n - kth)

    print(dist)