# You are given an array of numbers (non-negative). Find a continuous subarray of the list which adds up to a given sum.

## Brute-Force
  def subarray_sum1(arr, target):
      n = len(arr)
      for i in range(n):
          for j in range(i, n+1):
              if sum(arr[i:j]) == target:
                  return i, j
      return None, None
  
  # Better BruteForce
  def subarray_sum2(arr, target):
    n = len(arr)
    for i in range(n):
        s = 0
        for j in range(i, n+1):
            if s == target:
                return i,j
            s += arr[j]
    return None, None
  
  
  # Greedy Algorithm
  def subarray_sum3(arr, target):
    n = len(arr)
    i, j, s = 0, 0, 0
    while i < n and j <= n:
        if s == target:
            return i, j
        elif s < target:
            s += arr[j]
            j += 1
        elif s > target:
            s -= arr[i]
            i += 1
    return None, None
