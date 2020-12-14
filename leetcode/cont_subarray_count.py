def count_subarrays(arr):
  # Write your code here
  stack = []
  N = len(arr)
  res_a = [0 for _ in arr]
  for i in range(0, N): # O(N)
    while stack and arr[stack[-1]] < arr[i]:
      res_a[i] += res_a[stack.pop()]
    stack.append(i)
    res_a[i] += 1
  stack.clear()
  res_b = [0 for _ in arr]
  for i in range(N-1, -1, -1): # O(N)
    while stack and arr[stack[-1]] < arr[i]:
      res_b[i] += res_b[stack.pop()]
    stack.append(i)
    res_b[i] += 1
  return [a + b - 1 for a,b in zip(res_a, res_b)]



print(count_subarrays([2, 4, 7, 1, 5, 3]))
